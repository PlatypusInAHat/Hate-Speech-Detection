"""
VERIFICATION CHECKLIST - Hate Speech Detection Model v2.0

Run this to verify all fixes and improvements are in place.
"""

import os
import sys

def check_file_exists(filepath, description):
    """Check if file exists."""
    if os.path.exists(filepath):
        print(f"  ✓ {description}: {filepath}")
        return True
    else:
        print(f"  ✗ {description}: {filepath} (MISSING)")
        return False

def check_content_in_file(filepath, text, description):
    """Check if content exists in file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if text in content:
                print(f"  ✓ {description}")
                return True
            else:
                print(f"  ✗ {description} (NOT FOUND)")
                return False
    except Exception as e:
        print(f"  ✗ Error reading {filepath}: {e}")
        return False

def main():
    print("=" * 70)
    print("  VERIFICATION CHECKLIST - Hate Speech Detection Model v2.0")
    print("=" * 70 + "\n")
    
    all_checks = True
    
    # 1. Check files exist
    print("1️⃣  FILES EXISTENCE")
    print("─" * 70)
    
    files = [
        ("src/train.py", "Training script"),
        ("src/dataset.py", "Dataset loading"),
        ("src/evaluate.py", "Evaluation script"),
        ("src/predict.py", "Prediction script"),
        ("configs/config.yaml", "Configuration file"),
        ("requirements.txt", "Dependencies"),
        ("run_training.py", "Main training script"),
        ("check_data.py", "Data validation"),
        ("utils.py", "Utilities"),
        ("quickstart.py", "Quick start guide"),
        ("IMPROVEMENTS.md", "Improvements documentation"),
        ("CHANGELOG.md", "Changelog"),
        ("FIXES_SUMMARY.md", "Fixes summary"),
        ("README_QUICKSTART.txt", "Quick start README"),
    ]
    
    for filepath, description in files:
        if not check_file_exists(filepath, description):
            all_checks = False
    
    # 2. Check train.py fixes
    print("\n2️⃣  TRAIN.PY FIXES")
    print("─" * 70)
    
    train_checks = [
        ("src/train.py", "dataset, tokenizer = load_and_prepare_datasets", "Tokenizer loading fixed"),
        ("src/train.py", "input_ids", "Using tokenized columns"),
        ("src/train.py", "precision, recall", "Metrics improved"),
        ("src/train.py", "SEED = 42", "Seed for reproducibility"),
        ("src/train.py", "metric_for_best_model=\"f1\"", "F1-score as metric"),
        ("src/train.py", "BATCH_SIZE = 32", "Batch size tuned"),
        ("src/train.py", "LEARNING_RATE = 3e-5", "Learning rate tuned"),
        ("src/train.py", "EPOCHS = 15", "Epochs tuned"),
        ("src/train.py", "fp16=torch.cuda.is_available()", "Mixed precision training"),
    ]
    
    for filepath, content, description in train_checks:
        if not check_content_in_file(filepath, content, description):
            all_checks = False
    
    # 3. Check dataset.py fixes
    print("\n3️⃣  DATASET.PY FIXES")
    print("─" * 70)
    
    dataset_checks = [
        ("src/dataset.py", 'if train_path is None:', "Relative path handling for train"),
        ("src/dataset.py", 'if test_path is None:', "Relative path handling for test"),
        ("src/dataset.py", "train_df['label'].astype(int)", "Convert labels to int"),
        ("src/dataset.py", "tokens['label'] = examples['label']", "Labels preserved in tokens"),
        ("src/dataset.py", "return tokenized_datasets, tokenizer", "Return tokenizer"),
        ("src/dataset.py", "remove_columns=['text']", "Remove text to save memory"),
    ]
    
    for filepath, content, description in dataset_checks:
        if not check_content_in_file(filepath, content, description):
            all_checks = False
    
    # 4. Check evaluate.py completion
    print("\n4️⃣  EVALUATE.PY FIXES")
    print("─" * 70)
    
    eval_checks = [
        ("src/evaluate.py", "classification_report", "Classification report added"),
        ("src/evaluate.py", "confusion_matrix", "Confusion matrix added"),
        ("src/evaluate.py", "for i in range(0, len(texts), BATCH_SIZE)", "Batch processing"),
        ("src/evaluate.py", "evaluation_results.json", "JSON output"),
    ]
    
    for filepath, content, description in eval_checks:
        if not check_content_in_file(filepath, content, description):
            all_checks = False
    
    # 5. Check predict.py improvements
    print("\n5️⃣  PREDICT.PY IMPROVEMENTS")
    print("─" * 70)
    
    predict_checks = [
        ("src/predict.py", "softmax", "Confidence scores"),
        ("src/predict.py", "BATCH_SIZE = 32", "Batch size updated"),
        ("src/predict.py", "LABEL_MAP", "Label mapping"),
        ("src/predict.py", "predict_single_text", "Single text prediction"),
    ]
    
    for filepath, content, description in predict_checks:
        if not check_content_in_file(filepath, content, description):
            all_checks = False
    
    # 6. Check requirements.txt
    print("\n6️⃣  REQUIREMENTS.TXT")
    print("─" * 70)
    
    req_checks = [
        ("requirements.txt", "wandb", "Wandb package"),
        ("requirements.txt", "evaluate", "Evaluate package"),
    ]
    
    for filepath, content, description in req_checks:
        if not check_content_in_file(filepath, content, description):
            all_checks = False
    
    # 7. Check config.yaml
    print("\n7️⃣  CONFIG.YAML UPDATES")
    print("─" * 70)
    
    config_checks = [
        ("configs/config.yaml", "batch_size: 32", "Batch size configured"),
        ("configs/config.yaml", "epochs: 15", "Epochs configured"),
        ("configs/config.yaml", "learning_rate: 3e-5", "Learning rate configured"),
        ("configs/config.yaml", 'metric_for_best_model: "f1"', "F1 metric configured"),
        ("configs/config.yaml", "seed: 42", "Seed configured"),
    ]
    
    for filepath, content, description in config_checks:
        if not check_content_in_file(filepath, content, description):
            all_checks = False
    
    # Summary
    print("\n" + "=" * 70)
    if all_checks:
        print("  ✅ ALL CHECKS PASSED - System is ready!")
    else:
        print("  ⚠️  SOME CHECKS FAILED - Please review above")
    print("=" * 70 + "\n")
    
    return 0 if all_checks else 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
