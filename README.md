# 🔥 Phát hiện Hate Speech Tiếng Việt bằng PhoBERT

Dự án này sử dụng **PhoBERT** để phát hiện **ngôn từ thù ghét (Hate Speech)** trong văn bản tiếng Việt. Hệ thống được huấn luyện trên tập dữ liệu **UIT-ViHSD** với các nhãn phân loại:  
- **0 - Bình thường**: Không chứa nội dung tiêu cực  
- **1 - Công kích (Offensive Language)**: Ngôn từ xúc phạm, không nghiêm trọng  
- **2 - Thù ghét (Hate Speech)**: Ngôn từ mang tính kích động, xúc phạm mạnh  

## 🚀 Mục tiêu  
- Xây dựng mô hình **Phân loại văn bản** để nhận diện hate speech trong tiếng Việt.  
- Tối ưu hóa PhoBERT với **fine-tuning**, cân bằng dữ liệu & sử dụng **Early Stopping**.  
- Ứng dụng vào **kiểm duyệt nội dung mạng xã hội**, hỗ trợ chatbot AI, và phân tích dữ liệu.  

---

## 📌 Công nghệ sử dụng  
✅ **Ngôn ngữ**: Python  
✅ **Thư viện chính**:  
- `transformers` → Dùng **PhoBERT**  
- `datasets`, `pandas` → Xử lý dữ liệu  
- `torch`, `accelerate` → Huấn luyện mô hình  
- `wandb` → Theo dõi training  
✅ **Tập dữ liệu**: UIT-ViHSD (Vietnamese Hate Speech Detection)  

---

## 🛠 Cài đặt  
Trước khi chạy dự án, hãy đảm bảo bạn có **Python 3.8+** và cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
