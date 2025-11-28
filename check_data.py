#!/usr/bin/env python
"""
Data validation and statistics script.
"""

import pandas as pd
import os
from collections import Counter

def check_data():
    """Kiểm tra data files."""
    
    print("="*60)
    print("DATA VALIDATION & STATISTICS")
    print("="*60 + "\n")
    
    files_to_check = [
        ("data/train.csv", "Train"),
        ("data/test.csv", "Test"),
    ]
    
    for filepath, name in files_to_check:
        if not os.path.exists(filepath):
            print(f"✗ {name}: File not found at {filepath}")
            continue
        
        print(f"\n{'─'*60}")
        print(f"📊 {name} Dataset: {filepath}")
        print(f"{'─'*60}")
        
        try:
            df = pd.read_csv(filepath)
            
            # Basic stats
            print(f"  Total samples: {len(df):,}")
            print(f"  Columns: {list(df.columns)}")
            
            # Check required columns
            if "text" not in df.columns:
                print("  ✗ Missing 'text' column")
                continue
            if "label" not in df.columns:
                print("  ✗ Missing 'label' column")
                continue
            
            # Text statistics
            text_lengths = df["text"].str.len()
            print(f"\n  Text Length Statistics:")
            print(f"    Min: {text_lengths.min()}")
            print(f"    Max: {text_lengths.max()}")
            print(f"    Mean: {text_lengths.mean():.1f}")
            print(f"    Median: {text_lengths.median():.1f}")
            
            # Label distribution
            label_counts = Counter(df["label"])
            total = len(df)
            
            print(f"\n  Label Distribution:")
            for label in sorted(label_counts.keys()):
                count = label_counts[label]
                pct = (count / total) * 100
                print(f"    Label {label}: {count:,} samples ({pct:.1f}%)")
            
            # Missing values
            missing = df.isnull().sum()
            if missing.any():
                print(f"\n  Missing Values:")
                for col, count in missing.items():
                    if count > 0:
                        print(f"    {col}: {count}")
            
            # Data quality
            print(f"\n  Data Quality:")
            print(f"    ✓ Valid rows: {len(df)}")
            print(f"    ✓ No missing values in text: {df['text'].notna().all()}")
            print(f"    ✓ No missing values in label: {df['label'].notna().all()}")
            print(f"    ✓ All labels valid (0-2): {label_counts.keys() <= {0, 1, 2}}")
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print("\n" + "="*60)
    print("Validation Complete")
    print("="*60 + "\n")

if __name__ == "__main__":
    check_data()
