# Hate-Speech-Detection

Một project để tập ML

📌 Dự án: Phát hiện Hate Speech Tiếng Việt bằng PhoBERT
🔹 Mô tả dự án
Dự án này nhằm xây dựng một mô hình phát hiện ngôn từ thù ghét (Hate Speech) trong văn bản tiếng Việt bằng cách sử dụng PhoBERT – một mô hình ngôn ngữ mạnh mẽ được huấn luyện dành riêng cho tiếng Việt.

Hệ thống sẽ được huấn luyện trên tập dữ liệu UIT-ViHSD, một tập dữ liệu chuẩn về phát hiện hate speech trong tiếng Việt, với các nhãn như:

0 - Bình thường: Không có ngôn từ thù ghét
1 - Công kích (Offensive Language): Có lời lẽ xúc phạm nhưng không quá nghiêm trọng
2 - Thù ghét (Hate Speech): Ngôn từ thù ghét, có thể gây kích động
🔹 Mục tiêu
Huấn luyện mô hình PhoBERT để phân loại bình luận tiếng Việt thành các nhóm bình thường / công kích / thù ghét.
Áp dụng các kỹ thuật tiền xử lý văn bản, cân bằng dữ liệu, và tối ưu hóa để đạt kết quả tốt nhất.
Triển khai mô hình để sử dụng trong các hệ thống kiểm duyệt nội dung trên mạng xã hội, diễn đàn, hoặc chatbot.
🔹 Công nghệ sử dụng
✅ Ngôn ngữ lập trình: Python
✅ Thư viện chính:

transformers (Hugging Face) → Sử dụng PhoBERT
pandas, datasets → Xử lý dữ liệu
PyTorch → Huấn luyện mô hình
WandB → Theo dõi training
✅ Tập dữ liệu: UIT-ViHSD
✅ Phần cứng: GPU CUDA (NVIDIA) hoặc TPU (Google Colab)
🔹 Pipeline của dự án
1️⃣ Tiền xử lý dữ liệu:

Chuẩn hóa văn bản, loại bỏ stopwords, ký tự đặc biệt.
Chuyển đổi nhãn (0, 1, 2) về dạng số.
2️⃣ Huấn luyện mô hình PhoBERT:

Sử dụng AutoModelForSequenceClassification để fine-tune PhoBERT.
Áp dụng Early Stopping để tránh overfitting.
Cân bằng dữ liệu bằng class weights để tránh bias.
3️⃣ Đánh giá mô hình:

Tính các chỉ số accuracy, precision, recall, F1-score.
Kiểm tra kết quả trên tập test.
4️⃣ Triển khai & sử dụng:


