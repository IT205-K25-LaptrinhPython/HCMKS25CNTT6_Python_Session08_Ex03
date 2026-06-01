# Phân tích Input/Output
# Dữ liệu đầu vào
# Tất cả các dữ liệu đầu vào đều là Kiểu chuỗi (String).
# Menu hệ thống: Lựa chọn chức năng (choice): Các ký tự từ "1" đến "5".
# Chức năng 1 (Nhập thông tin):
# Tên người gửi, Số điện thoại người gửi, Địa chỉ lấy hàng
# Tên người nhận, Số điện thoại người nhận, Địa chỉ giao hàng
# Mã đơn hàng, Ghi chú giao hàng
# Chức năng 4 (Tìm và thay thế): 
# * Từ khóa cần tìm (find_word)
# * Từ khóa thay thế (replace_word)
#
# Dữ liệu đầu ra (Output)
# Chức năng 1:
# Tên người gửi, người nhận được chuẩn hóa (loại bỏ khoảng trắng, viết hoa chữ cái đầu).
# Địa chỉ được chuẩn hóa khoảng trắng.
# Ghi chú được loại bỏ khoảng trắng thừa, hiển thị độ dài, số lượng từ, chữ thường, chữ hoa.
# Chức năng 2: Mã đơn hàng ban đầu và mã đã được chuẩn hóa (chuyển chữ hoa, thêm GRAB-, đổi khoảng trắng thành gạch ngang).
# Chức năng 3: Số điện thoại người gửi và nhận được ẩn 5 số ở giữa bằng dấu *.
# Chức năng 4: Số lượng từ khóa tìm thấy và ghi chú mới sau khi thay thế. Thông báo nếu không tìm thấy.
# Chức năng 5: Dòng thông báo thoát và ngắt chương trình.
#
# Đề xuất giải pháp
# Sử dụng cấu trúc lặp kết hợp rẽ nhánh (match-case) và các phương thức xử lý chuỗi (String methods) của Python.
# Cấu trúc điều khiển chính
# Vòng lặp while True: Tạo vòng lặp vô hạn hiển thị menu liên tục.
# Câu lệnh match-case: Điều hướng luồng thực thi từ lựa chọn "1" đến "5".
# Bẫy lỗi menu (Bẫy 5 & Bẫy 6): Sử dụng case _ để bắt mọi trường hợp người dùng nhập chữ hoặc số nằm ngoài khoảng 1-5.
# Các phương thức xử lý chuỗi và kiểm tra dữ liệu
# Làm sạch và định dạng: .strip(), .title(), .upper(), .lower().
# Xử lý khoảng trắng giữa các từ: " ".join(chuoi.split()).
# Tính toán và kiểm tra: len(), .isdigit(), .startswith(), .replace(), .count().
# Xử lý bẫy dữ liệu (Bẫy 1, 2, 3): Dùng vòng lặp while phụ bên trong chức năng 1 để ép người dùng nhập đúng định dạng.
#
# Thiết kế thuật toán (Pseudocode)
# BẮT ĐẦU CHƯƠNG TRÌNH
# KHỞI TẠO các biến lưu thông tin quan trọng bằng chuỗi rỗng
# LẶP VÔ HẠN (while True):
#     IN ra màn hình Khung giao diện Menu (1 đến 5)
#     NHẬP lựa chọn chức năng vào biến 'choice'
#     CHỌN 'choice' (match-case):
#         TRƯỜNG HỢP "1":
#             LẶP ĐỂ NHẬP các trường thông tin, kiểm tra rỗng (Bẫy 1).
#             LẶP ĐỂ KIỂM TRA số điện thoại phải là số và đủ 10 ký tự (Bẫy 2, Bẫy 3).
#             CHUẨN HÓA tên, địa chỉ, ghi chú.
#             IN ra báo cáo thống kê.
#         TRƯỜNG HỢP "2":
#             CHUẨN HÓA order_id: viết hoa, thay khoảng trắng bằng '-', thêm 'GRAB-'.
#             IN order_id cũ và mới.
#         TRƯỜNG HỢP "3":
#             ẨN 5 số giữa của số điện thoại bằng '*****'.
#             IN kết quả.
#         TRƯỜNG HỢP "4":
#             NẾU ghi chú rỗng -> Báo lỗi (Bẫy 4).
#             NGƯỢC LẠI: Nhập find_word và replace_word, đếm và thay thế.
#         TRƯỜNG HỢP "5":
#             IN "Thoát chương trình"
#             THOÁT LẶP (break)
#         TRƯỜNG HỢP MẶC ĐỊNH (case _):
#             IN "Lựa chọn không hợp lệ"
# KẾT THÚC CHƯƠNG TRÌNH

while True:
    print(f"+{"="*60}+")
    print("|" + "HỆ THỐNG QUẢN LÝ NỘI DUNG ĐƠN HÀNG GRAB EXPRESS".center(60) + "|")
    print(f"+{"="*60}+")
    print("|   1. Nhập dữ liệu đơn hàng và xem báo cáo thống kê         |")
    print("|   2. Chuẩn hóa mã đơn hàng                                 |")
    print("|   3. Ẩn số điện thoại khách hàng                           |")
    print("|   4. Tìm kiếm và thay thế từ khóa trong ghi chú đơn hàng   |")
    print("|   5. Thoát chương trình                                    |")
    print(f"+{"="*60}+")    
    choice = input("> Mời bạn chọn chức năng (1-5): ").strip()    
    match choice:
        case "1":
            print("\n--- NHẬP DỮ LIỆU ĐƠN HÀNG ---")
            # Nhập Tên người gửi (Bẫy 1)
            while True:
                sender_name = input("- Tên người gửi: ").strip()
                if len(sender_name) == 0:
                    print("[Tên người gửi] không được bỏ trống")
                else:
                    break
            while True:
                sender_phone = input("- Số điện thoại người gửi: ").strip()
                if len(sender_phone) == 0:
                    print("[Số điện thoại người gửi] không được bỏ trống")
                elif not sender_phone.isdigit():
                    print("Số điện thoại không hợp lệ")
                elif len(sender_phone) != 10:
                    print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
                else:
                    break
            while True:
                pickup_address = input("- Địa chỉ lấy hàng: ").strip()
                if len(pickup_address) == 0:
                    print("[Địa chỉ lấy hàng] không được bỏ trống")
                else:
                    break
            while True:
                receiver_name = input("- Tên người nhận: ").strip()
                if len(receiver_name) == 0:
                    print("[Tên người nhận] không được bỏ trống")
                else:
                    break
            while True:
                receiver_phone = input("- Số điện thoại người nhận: ").strip()
                if len(receiver_phone) == 0:
                    print("[Số điện thoại người nhận] không được bỏ trống")
                elif not receiver_phone.isdigit():
                    print("Số điện thoại không hợp lệ")
                elif len(receiver_phone) != 10:
                    print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
                else:
                    break
            while True:
                delivery_address = input("- Địa chỉ giao hàng: ").strip()
                if len(delivery_address) == 0:
                    print("[Địa chỉ giao hàng] không được bỏ trống")
                else:
                    break
            while True:
                order_id = input("- Mã đơn hàng: ").strip()
                if len(order_id) == 0:
                    print("[Mã đơn hàng] không được bỏ trống")
                else:
                    break
            while True:
                notes = input("- Ghi chú giao hàng: ").strip()
                if len(notes) == 0:
                    print("[Ghi chú giao hàng] không được bỏ trống")
                else:
                    break
            print()
            print(f"- Tên người gửi (chuẩn hóa): {sender_name.title()}")
            print(f"- Tên người nhận (chuẩn hóa): {receiver_name.title()}")
            print(f"- Địa chỉ lấy hàng (chuẩn hóa): {" ".join(pickup_address.split())}")
            print(f"- Địa chỉ giao hàng (chuẩn hóa): {" ".join(delivery_address.split())}")
            print(f"- Ghi chú (đã loại bỏ khoảng trắng thừa): {notes}")
            print(f"- Độ dài ghi chú: {len(notes)} ký tự")
            print(f"- Số lượng từ trong ghi chú: {notes.count(' ') + 1} từ")
            print(f"- Ghi chú chữ thường: {notes.lower()}")
            print(f"- Ghi chú chữ hoa: {notes.upper()}\n")
        case "2":
            print("\n--- CHUẨN HÓA MÁ ĐƠN HÀNG ---")
            if len(order_id) == 0:
                print("Chưa có mã đơn hàng. Vui lòng nhập thông tin ở chức năng 1.\n")
                continue              
            print(f"- Mã đơn hàng ban đầu: \"{order_id}\"")
            normalized_id = order_id.upper()
            if " " in normalized_id:
                normalized_id = normalized_id.replace(" ", "-")
            if not normalized_id.startswith("GRAB-"):
                normalized_id = "GRAB-" + normalized_id               
            print(f"- Mã đơn hàng sau khi được chuẩn hóa: \"{normalized_id}\"\n")
            order_id = normalized_id
        case "3":
            print("\n--- ẨN SỐ ĐIỆN THOẠI KHÁCH HÀNG ---")
            if len(sender_phone) == 0 or len(receiver_phone) == 0:
                print("Chưa có thông tin số điện thoại. Vui lòng nhập ở chức năng 1.\n")
                continue         
            masked_s_phone = sender_phone[:3] + "*****" + sender_phone[-2:]
            masked_r_phone = receiver_phone[:3] + "*****" + receiver_phone[-2:]         
            print(f"SĐT người gửi: {masked_s_phone}")
            print(f"SĐT người nhận: {masked_r_phone}\n")
        case "4":
            print("\n--- TÌM KIẾM VÀ THAY THẾ TỪ KHÓA TRONG GHI CHÚ ---")
            # Bẫy 4: Chưa nhập ghi chú
            if len(notes) == 0:
                print("Chưa có ghi chú giao hàng để tìm kiếm\n")
                continue                
            print(f"Ghi chú đơn hàng hiện tại:\n{notes}")
            find_word = input("- Từ khóa cần tìm: ")
            replace_word = input("- Từ khóa thay thế: ")            
            count_word = notes.count(find_word)
            if count_word > 0:
                notes = notes.replace(find_word, replace_word)
                print("\nOutput:")
                print(f"Số lần xuất hiện của từ khóa: {count_word}")
                print(f"Ghi chú đơn hàng sau khi thay thế:\n{notes}\n")
            else:
                print("Không tìm thấy\n")
        case "5":
            print("Thoát chương trình\n")
            break            
        case _:
            print("Lựa chọn không hợp lệ\n")