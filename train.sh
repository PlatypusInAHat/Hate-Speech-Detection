#!/bin/bash

# Cấu hình chung
MODEL_NAME="vinai/phobert-base"
DATASET_PATH="data/UIT-ViHSD_train.csv"
OUTPUT_DIR="./results"
LOG_DIR="./logs"
EPOCHS=5
BATCH_SIZE=16
LEARNING_RATE=2e-5
WARMUP_STEPS=500
WEIGHT_DECAY=0.01
SAVE_TOTAL_LIMIT=2
GRADIENT_ACCUMULATION_STEPS=2

# Kích hoạt môi trường ảo (nếu có)
# source venv/bin/activate

# Huấn luyện mô hình
python train.py \
    --model_name $MODEL_NAME \
    --dataset_path $DATASET_PATH \
    --output_dir $OUTPUT_DIR \
    --log_dir $LOG_DIR \
    --epochs $EPOCHS \
    --batch_size $BATCH_SIZE \
    --learning_rate $LEARNING_RATE \
    --warmup_steps $WARMUP_STEPS \
    --weight_decay $WEIGHT_DECAY \
    --save_total_limit $SAVE_TOTAL_LIMIT \
    --gradient_accumulation_steps $GRADIENT_ACCUMULATION_STEPS
