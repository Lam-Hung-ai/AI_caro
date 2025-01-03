# Ứng dụng hàm đánh giá heuristic trong giải thuật Minimax và cắt tỉa Alpha-beta trong game cờ caro
**Sản phẩm thuộc nhóm 1**  
Lớp 65ANM  

## Giới thiệu  
Đây là một dự án AI chơi cờ caro của chúng em, được phát triển để thử nghiệm và tối ưu hóa thuật toán Minimax với độ sâu và cắt tỉa Alpha-Beta cùng với hàm đánh giá heuristic

## Công nghệ sử dụng
- **Ngôn ngữ lập trình**: Python
- **Thư viện**: Pygame
## Cách hoạt động cơ bản
- Với các ô trống bị ảnh hưởng bởi các nước cờ X/O được dùng **hàm đánh giá heuristic** điểm để có thể chọn ra 5 điểm có số điểm cao nhất phục vụ cho duyệt Minimax giúp giảm không gian tìm kiếm
- **Thuật toán Minimax với độ sâu hạn chế là 2**: AI đánh giá tất cả các nước đi khả thi để tìm ra nước đi tốt nhất dựa trên cây trạng thái.
- **Cắt tỉa Alpha-Beta**: tăng tốc thuật toán Minimax bằng cách loại bỏ các nhánh không cần thiết.  

## Đánh giá
- Mô hình đạt chiến thắng cao khoảng 70% trong 30 trận đấu
- AI có thể tự chặn được nhiều `3 nước`: _\_OOO\__ liên tiếp của người chơi hay các tình huống `4 nước liên tiếp bị chặn đầu khá tốt`: _\_XOOO\__
- AI cũng chủ động tấn công người chơi với `3 nước`:  _\_XXX\__ liên tiếp để tấn công, biết tạo liên tục 
- Nhưng mà AI cũng gặp một số hạn chế, trong một số trường hợp AI không phát hiện ra các nước đi khó có thể tạo thành 2 chuỗi `3 nước` của người chơi
- Tỉ lệ thắng AI vẫn còn thấp
- Nếu người chơi dùng đúng một form đánh mà không nguy hiểm thì AI cũng sẽ lặp lại trạng thái đã dùng từ những ván trước (không có sự thay đổi, cứng nhắc)  
## Hướng dẫn cài đặt 
1. Tải kho chứa code về:
   ```bash
   git clone https://github.com/Lam-Hung-ai/AI_caro.git
   cd ai-caro-minimax
   ```
2. Cài đặt thư viện cần thiết
   ```bash
   pip install -U pygame
   ```
3. Chạy chương trình
   ```bash
   python main.py
   ```
### Trên Windows bạn có thể trải nghiệm ngay với file .exe trong `AI_caro/exe/AI_caro.exe`
