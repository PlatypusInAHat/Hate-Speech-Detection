#!/usr/bin/env python
"""
QUICK START GUIDE - Hate Speech Detection Model

Chạy script này để bắt đầu nhanh chóng.
"""

import os
import sys
import subprocess

def print_header(text):
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def run_command(cmd, description):
    print(f"▶ {description}...")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"✗ Failed: {description}")
        return False
    print(f"✓ Done: {description}")
    return True

def main():
    print_header("🎯 HATE SPEECH DETECTION - QUICK START")
    
    print("This guide will help you set up and run the model.\n")
    
    # Step 1: Check environment
    print("STEP 1: Check Environment")
    print("─" * 60)
    if run_command("python utils.py check", "Environment check"):
        pass
    else:
        print("⚠ Environment check failed. Please fix issues and try again.")
        return 1
    
    # Step 2: Data preparation
    print("\n\nSTEP 2: Prepare Data")
    print("─" * 60)
    
    if os.path.exists("data/train.csv") and os.path.exists("data/test.csv"):
        print("✓ Data files found")
        if run_command("python check_data.py", "Data validation"):
            pass
    else:
        print("ℹ Data files not found")
        print("Creating sample data for testing...")
        if run_command("python utils.py sample", "Create sample data"):
            if run_command("python check_data.py", "Data validation"):
                pass
    
    # Step 3: Install dependencies
    print("\n\nSTEP 3: Install Dependencies")
    print("─" * 60)
    if run_command("pip install -q -r requirements.txt", "Install packages"):
        pass
    else:
        print("⚠ Package installation failed")
        return 1
    
    # Step 4: Training
    print("\n\nSTEP 4: Train Model")
    print("─" * 60)
    print("\nOptions:")
    print("  1. Quick training (with sample data)")
    print("  2. Full training (with your data)")
    print("  3. Skip training")
    
    choice = input("\nSelect option (1-3): ").strip()
    
    if choice == "1" or choice == "2":
        if run_command("python run_training.py", "Model training"):
            print("\n✓ Training completed!")
        else:
            print("\n✗ Training failed")
            return 1
    elif choice == "3":
        print("Skipping training...")
    else:
        print("Invalid option")
        return 1
    
    # Step 5: Evaluation
    print("\n\nSTEP 5: Evaluate Model")
    print("─" * 60)
    
    if os.path.exists("saved_model"):
        user_eval = input("Run evaluation? (y/n): ").strip().lower()
        if user_eval == 'y':
            if run_command("cd src && python evaluate.py", "Model evaluation"):
                print("\n✓ Evaluation completed!")
    else:
        print("ℹ Saved model not found. Train model first.")
    
    # Step 6: Prediction
    print("\n\nSTEP 6: Make Predictions")
    print("─" * 60)
    
    if os.path.exists("saved_model"):
        user_pred = input("Make predictions? (y/n): ").strip().lower()
        if user_pred == 'y':
            if run_command("cd src && python predict.py", "Make predictions"):
                print("\n✓ Predictions completed!")
                print("Results saved to: predictions.csv")
    
    # Summary
    print_header("✅ SETUP COMPLETE")
    
    print("Next steps:")
    print("\n1. Training:")
    print("   python run_training.py")
    
    print("\n2. Evaluation:")
    print("   cd src")
    print("   python evaluate.py")
    
    print("\n3. Prediction:")
    print("   cd src")
    print("   python predict.py")
    
    print("\n4. Data validation:")
    print("   python check_data.py")
    
    print("\n5. Check environment:")
    print("   python utils.py check")
    
    print("\n" + "="*60)
    print("For more info, see: IMPROVEMENTS.md, CHANGELOG.md, FIXES_SUMMARY.md")
    print("="*60 + "\n")
    
    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n✗ Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
