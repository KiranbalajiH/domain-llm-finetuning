"""
QLoRA Training Script for Mistral-7B / Llama-3-8B Fine-Tuning
Uses Hugging Face TRL (SFTTrainer), PEFT (LoRA), and bitsandbytes 4-bit quantization.
Follows Phase 3 & 4 of the Implementation Plan.
"""

import os
import sys
import yaml
import json
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def load_config(config_path: str = "training/config.yaml") -> Dict[str, Any]:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def format_instruction_prompt(sample: Dict[str, str]) -> str:
    """Formats standard JSONL sample into Mistral/Llama instruct prompt format."""
    instruction = sample.get("instruction", "").strip()
    user_input = sample.get("input", "").strip()
    output = sample.get("output", "").strip()
    
    if user_input:
        prompt_content = f"{instruction}\n\nContext/Input: {user_input}"
    else:
        prompt_content = instruction
        
    formatted = f"<s>[INST] {prompt_content} [/INST] {output}</s>"
    return formatted

def run_training(config_path: str = "training/config.yaml"):
    logger.info("Initializing QLoRA Fine-Tuning Pipeline...")
    cfg = load_config(config_path)
    
    try:
        import torch
        from transformers import (
            AutoModelForCausalLM,
            AutoTokenizer,
            BitsAndBytesConfig,
            TrainingArguments
        )
        from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
        from trl import SFTTrainer
        from datasets import load_dataset
    except ImportError as e:
        logger.error(f"Missing core training dependencies: {e}")
        logger.error("Run on Kaggle/Colab GPU or install with: pip install torch transformers peft bitsandbytes trl datasets accelerate")
        sys.exit(1)

    model_id = cfg["model"]["base_model_id"]
    logger.info(f"Target Base Model: {model_id}")

    # 1. 4-bit Quantization Config (bitsandbytes NF4)
    compute_dtype = getattr(torch, cfg["quantization"]["bnb_4bit_compute_dtype"])
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=cfg["quantization"]["load_in_4bit"],
        bnb_4bit_quant_type=cfg["quantization"]["bnb_4bit_quant_type"],
        bnb_4bit_use_double_quant=cfg["quantization"]["bnb_4bit_use_double_quant"],
        bnb_4bit_compute_dtype=compute_dtype
    )

    # 2. Load Tokenizer
    logger.info("Loading Tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    # 3. Load Quantized Base Model
    logger.info("Loading base model in 4-bit NF4 precision...")
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb_config,
        device_map=cfg["model"]["device_map"],
        trust_remote_code=True
    )
    model.config.use_cache = False
    model = prepare_model_for_kbit_training(model)

    # 4. LoRA Adapter Config
    logger.info("Configuring LoRA Adapter...")
    peft_config = LoraConfig(
        r=cfg["lora"]["r"],
        lora_alpha=cfg["lora"]["lora_alpha"],
        lora_dropout=cfg["lora"]["lora_dropout"],
        bias=cfg["lora"]["bias"],
        task_type=cfg["lora"]["task_type"],
        target_modules=cfg["lora"]["target_modules"]
    )
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()

    # 5. Load & Format Datasets
    logger.info("Loading train and evaluation datasets...")
    dataset = load_dataset(
        "json",
        data_files={
            "train": cfg["data"]["train_file"],
            "eval": cfg["data"]["eval_file"]
        }
    )

    def formatting_prompts_func(example):
        output_texts = []
        for i in range(len(example['instruction'])):
            text = format_instruction_prompt({
                "instruction": example['instruction'][i],
                "input": example['input'][i] if 'input' in example else "",
                "output": example['output'][i]
            })
            output_texts.append(text)
        return output_texts

    # 6. Training Arguments
    training_args = TrainingArguments(
        output_dir=cfg["training"]["output_dir"],
        num_train_epochs=cfg["training"]["num_train_epochs"],
        per_device_train_batch_size=cfg["training"]["per_device_train_batch_size"],
        per_device_eval_batch_size=cfg["training"]["per_device_eval_batch_size"],
        gradient_accumulation_steps=cfg["training"]["gradient_accumulation_steps"],
        learning_rate=cfg["training"]["learning_rate"],
        weight_decay=cfg["training"]["weight_decay"],
        warmup_ratio=cfg["training"]["warmup_ratio"],
        lr_scheduler_type=cfg["training"]["lr_scheduler_type"],
        logging_steps=cfg["training"]["logging_steps"],
        save_strategy=cfg["training"]["save_strategy"],
        save_steps=cfg["training"]["save_steps"],
        save_total_limit=cfg["training"]["save_total_limit"],
        eval_strategy=cfg["training"]["eval_strategy"],
        eval_steps=cfg["training"]["eval_steps"],
        fp16=cfg["training"]["fp16"],
        bf16=cfg["training"]["bf16"],
        optim=cfg["training"]["optim"],
        gradient_checkpointing=cfg["training"]["gradient_checkpointing"],
        report_to="none"
    )

    # 7. SFTTrainer
    logger.info("Initializing SFTTrainer...")
    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset["train"],
        eval_dataset=dataset["eval"],
        peft_config=peft_config,
        formatting_func=formatting_prompts_func,
        max_seq_length=cfg["model"]["model_max_length"],
        tokenizer=tokenizer,
        args=training_args
    )

    # 8. Fine-Tuning Execution
    logger.info("Starting training loop...")
    train_result = trainer.train()

    # 9. Save LoRA Adapter & Tokenizer
    output_dir = cfg["training"]["output_dir"]
    logger.info(f"Saving fine-tuned LoRA adapter to {output_dir}...")
    trainer.model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)

    metrics = train_result.metrics
    trainer.log_metrics("train", metrics)
    trainer.save_metrics("train", metrics)
    trainer.save_state()

    logger.info("Fine-tuning completed successfully! Adapter weights ready for serving.")

if __name__ == "__main__":
    run_training()
