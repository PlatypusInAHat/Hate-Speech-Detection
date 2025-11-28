#!/usr/bin/env python
"""
Script chính để chạy training model với các tuning tối ưu.
"""

import os
import sys
import torch
import yaml
import logging

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from train import trainer, logger as train_logger

def main():
    print("="*60)
    print("HATE SPEECH DETECTION MODEL TRAINING")
    print("="*60)
    
    # Check GPU availability
    if torch.cuda.is_available():
        print(f"✓ GPU Available: {torch.cuda.get_device_name(0)}")
        print(f"✓ CUDA Version: {torch.version.cuda}")
    else:
        print("⚠ GPU not available. Training will use CPU (slower).")
    
    # Check data files
    if not os.path.exists("data/train.csv"):
        print("✗ Error: data/train.csv not found")
        return 1
    if not os.path.exists("data/test.csv"):
        print("✗ Error: data/test.csv not found")
        return 1
    
    print("\n✓ Data files found")
    
    # Load config
    with open("configs/config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    print(f"✓ Config loaded from configs/config.yaml")
    print(f"✓ Model: {config['model']['name']}")
    print(f"✓ Batch Size: {config['training']['batch_size']}")
    print(f"✓ Epochs: {config['training']['epochs']}")
    print(f"✓ Learning Rate: {config['training']['learning_rate']}")
    
    print("\n" + "="*60)
    print("STARTING TRAINING...")
    print("="*60 + "\n")
    
    try:
        # Start training
        trainer.train()
        
        print("\n" + "="*60)
        print("TRAINING COMPLETED SUCCESSFULLY!")
        print("="*60)
        
        # Evaluate
        print("\nEvaluating model...")
        eval_results = trainer.evaluate()
        
        print("\nEvaluation Results:")
        for metric, value in eval_results.items():
            if not metric.startswith("epoch"):
                print(f"  {metric}: {value:.4f}" if isinstance(value, float) else f"  {metric}: {value}")
        
        print("\n✓ Model saved to ./saved_model")
        print("✓ Results saved to ./evaluation_results.json")
        print("✓ Training config saved to ./training_config.json")
        
        return 0
        
    except Exception as e:
        print(f"\n✗ Error during training: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
