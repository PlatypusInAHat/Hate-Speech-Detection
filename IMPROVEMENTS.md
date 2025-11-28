# Hate Speech Detection - Improved Model with Tuning

## 📋 Overview

Đây là dự án phát hiện hate speech sử dụng PhoBERT (Vietnamese BERT) với các cải tiến về:
- Model tuning tối ưu
- Xử lý dữ liệu cải thiện
- Các chỉ số đánh giá toàn diện
- Early stopping thông minh

## 🔧 Cải tiến chính

### 1. **Model Tuning**
- **Batch size**: 32 (tăng từ 16 → gradient estimates tốt hơn)
- **Learning rate**: 3e-5 (fine-tuned từ 2e-5)
- **Epochs**: 15 (tăng từ 10 → convergence tốt hơn)
- **Dropout**: 0.1 cho cả hidden và attention layers
- **Optimizer**: AdamW (torch version tối ưu)
- **Mixed precision**: FP16 training trên GPU (nhanh hơn + tiết kiệm memory)
- **Weight decay**: 0.01 (regularization)

### 2. **Early Stopping**
- Patience: 4 epochs (hợp lý hơn so với 3)
- Threshold: 0.0001 (ngưỡng cải thiện tối thiểu)
- Metric: F1-score (tốt hơn accuracy cho dữ liệu không cân bằng)

### 3. **Data Handling**
- Xử lý labels chuẩn (0, 1, 2)
- Class weights cân bằng (xử lý data imbalance)
- Tokenization tối ưu với max_length=256

### 4. **Metrics**
- Accuracy, Precision, Recall, F1-score
- Classification Report chi tiết
- Confusion Matrix

### 5. **Lỗi được sửa**
- ✓ Fixed: Path hardcode → đường dẫn tương đối
- ✓ Fixed: Tokenization không lưu labels → lưu đúng
- ✓ Fixed: Thiếu class weights handling
- ✓ Fixed: Evaluate.py không hoàn chỉnh
- ✓ Fixed: Predict.py thiếu confidence scores

## 📦 Cấu trúc Project

```
hate speech/
├── src/
│   ├── train.py              # Training script (cải tiến)
│   ├── dataset.py            # Dataset loading (sửa lỗi)
│   ├── evaluate.py           # Evaluation (hoàn chỉnh)
│   ├── predict.py            # Prediction (cải tiến)
│   └── __pycache__/
├── configs/
│   └── config.yaml           # Config tối ưu (cập nhật)
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── vihsd/
├── notebooks/
│   └── exploratory_data_analysis.ipynb
├── results/                  # Output từ training
├── saved_model/              # Model weights
├── logs/                     # TensorBoard logs
├── run_training.py           # Main script
├── requirements.txt          # Dependencies (cập nhật)
└── README.md
```

## 🚀 Cách sử dụng

### 1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 2. **Chuẩn bị Data**
Đảm bảo có file `data/train.csv` và `data/test.csv` với cột:
- `text`: văn bản cần phân loại
- `label`: nhãn (0, 1 hoặc 2)

Ví dụ:
```csv
text,label
"Văn bản ở đây",0
"Văn bản khác",1
```

### 3. **Chạy Training**
```bash
python run_training.py
```

Hoặc chạy trực tiếp từ src:
```bash
cd src
python train.py
```

### 4. **Evaluate Model**
```bash
cd src
python evaluate.py
```

### 5. **Prediction**
```bash
cd src
python predict.py
```

## 📊 Output

### Training
- `results/` - TensorBoard logs
- `saved_model/` - Trained model weights
- `training_config.json` - Configuration used
- `logs/` - Event files for TensorBoard

### Evaluation
- `evaluation_results.json` - Metrics và confusion matrix

### Prediction
- `predictions.csv` - Results với confidence scores

## 📈 Expected Results

Với các tuning tối ưu, mô hình sẽ:
- **Converge nhanh hơn** → fewer epochs needed
- **F1-score cao hơn** → Better precision-recall balance
- **Generalization tốt hơn** → Avoid overfitting với early stopping

## 🔍 Hyperparameter Tuning

Bạn có thể điều chỉnh trong `configs/config.yaml`:

```yaml
training:
  batch_size: 32          # Tăng cho gradient estimate tốt hơn
  learning_rate: 3e-5     # Giảm = học chậm hơn (ổn định), tăng = học nhanh hơn
  epochs: 15              # Tăng = học lâu hơn (nhưng nguy hiểm overfitting)
  weight_decay: 0.01      # Regularization strength
```

## 🐛 Lỗi Common & Fix

| Lỗi | Nguyên nhân | Fix |
|-----|-----------|-----|
| `ModuleNotFoundError: No module named 'wandb'` | Thiếu package | `pip install wandb` |
| `RuntimeError: CUDA out of memory` | Batch size quá lớn | Giảm `batch_size` |
| `ValueError: Column 'label' not found` | Format data sai | Check `data/train.csv` |
| `FileNotFoundError: saved_model` | Model chưa train | Chạy `run_training.py` trước |

## 📝 Notes

- Model mặc định dùng **vinai/phobert-base** (Vietnamese language)
- Early stopping dựa trên **F1-score** (tốt cho imbalanced data)
- Sử dụng **class weights** để xử lý data imbalance
- **Seed=42** → reproducible results

## 📚 References

- [PhoBERT](https://github.com/VinAI/PhoBERT)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- [Weights & Biases](https://wandb.ai/)

---

**Last Updated**: 2025-02-10
**Status**: ✓ Ready for training with improved tuning
