#!/usr/bin/env python
"""
Utility functions for debugging and development.
"""

import os
import torch
import logging

logger = logging.getLogger(__name__)

def check_environment():
    """Check environment setup."""
    print("="*60)
    print("ENVIRONMENT CHECK")
    print("="*60 + "\n")
    
    # Python
    import sys
    print(f"Python: {sys.version}")
    
    # PyTorch
    print(f"PyTorch: {torch.__version__}")
    
    # GPU
    if torch.cuda.is_available():
        print(f"✓ GPU Available: {torch.cuda.get_device_name(0)}")
        print(f"  CUDA: {torch.version.cuda}")
        print(f"  cuDNN: {torch.backends.cudnn.version()}")
        print(f"  GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f}GB")
    else:
        print("✗ GPU not available (using CPU)")
    
    # Transformers
    try:
        import transformers
        print(f"Transformers: {transformers.__version__}")
    except:
        print("✗ Transformers not installed")
    
    # Other packages
    packages = ['datasets', 'sklearn', 'pandas', 'numpy', 'wandb']
    print("\nRequired packages:")
    for pkg in packages:
        try:
            mod = __import__(pkg if pkg != 'sklearn' else 'sklearn')
            version = getattr(mod, '__version__', 'installed')
            print(f"  ✓ {pkg}: {version}")
        except:
            print(f"  ✗ {pkg}: not installed")
    
    print("\n" + "="*60 + "\n")

def create_sample_data():
    """Create sample data for testing."""
    import pandas as pd
    
    print("Creating sample data...")
    
    # Sample data
    texts = [
        "Xin chào, bạn khỏe không?",
        "Tôi rất yêu thích bạn.",
        "Bạn là người tồi tệ nhất.",
        "Chúng ta hãy cùng nhau học tập.",
        "Tôi ghét cái thứ này.",
        "Bạn thật là đẹp.",
        "Kiếp cuộc này có ý nghĩa không?",
        "Tôi cảm thấy buồn.",
        "Bạn là một kẻ vô dụng.",
        "Chúng ta nên cùng nhau.",
    ]
    
    labels = [0, 0, 1, 0, 1, 0, 0, 0, 2, 0]  # 0: clean, 1: offensive, 2: hate
    
    df = pd.DataFrame({'text': texts, 'label': labels})
    
    os.makedirs('data', exist_ok=True)
    
    # Split into train/test
    train_df = df.iloc[:8]
    test_df = df.iloc[8:]
    
    train_df.to_csv('data/train.csv', index=False, encoding='utf-8')
    test_df.to_csv('data/test.csv', index=False, encoding='utf-8')
    
    print("✓ Sample data created:")
    print(f"  - data/train.csv ({len(train_df)} samples)")
    print(f"  - data/test.csv ({len(test_df)} samples)")

def print_model_size():
    """Print model size and parameter count."""
    try:
        from transformers import AutoModelForSequenceClassification
        
        model = AutoModelForSequenceClassification.from_pretrained(
            "vinai/phobert-base",
            num_labels=3
        )
        
        total_params = sum(p.numel() for p in model.parameters())
        trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
        
        print("="*60)
        print("MODEL SIZE")
        print("="*60)
        print(f"Total parameters: {total_params:,}")
        print(f"Trainable parameters: {trainable_params:,}")
        print(f"Model size: {total_params * 4 / 1e6:.1f}MB (approx)")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"Could not load model: {e}")

def estimate_training_time():
    """Estimate training time."""
    
    print("="*60)
    print("TRAINING TIME ESTIMATE")
    print("="*60)
    
    # Assumptions
    num_train_samples = 1000  # Adjust based on your data
    batch_size = 32
    num_epochs = 15
    seconds_per_batch = 2  # On GPU, adjust for your hardware
    
    total_batches = (num_train_samples / batch_size) * num_epochs
    total_seconds = total_batches * seconds_per_batch
    total_minutes = total_seconds / 60
    total_hours = total_minutes / 60
    
    print(f"Assumptions:")
    print(f"  Training samples: {num_train_samples:,}")
    print(f"  Batch size: {batch_size}")
    print(f"  Epochs: {num_epochs}")
    print(f"  Time per batch: {seconds_per_batch}s")
    
    print(f"\nEstimate:")
    print(f"  Total batches: {total_batches:.0f}")
    print(f"  Total time: {total_hours:.1f} hours ({total_minutes:.0f} minutes)")
    
    print("\n(This is a rough estimate. Actual time depends on GPU/CPU)")
    print("="*60 + "\n")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "check":
            check_environment()
        elif command == "sample":
            create_sample_data()
        elif command == "model":
            print_model_size()
        elif command == "estimate":
            estimate_training_time()
        else:
            print(f"Unknown command: {command}")
            print("Available commands: check, sample, model, estimate")
    else:
        print("Usage: python utils.py [check|sample|model|estimate]")
        print("\nExamples:")
        print("  python utils.py check      - Check environment")
        print("  python utils.py sample     - Create sample data")
        print("  python utils.py model      - Show model info")
        print("  python utils.py estimate   - Estimate training time")
