import mysql.connector
from mysql.connector import Error

def connect():
    try:
        # Kết nối đến database
        connection = mysql.connector.connect(
            host='localhost',  # Địa chỉ máy chủ (có thể là 'localhost' hoặc IP máy chủ)
            database='company',  # Tên database bạn muốn kết nối
            user='root',  # Tên người dùng
            password='root'  # Mật khẩu
        )

        if connection.is_connected():
            print("Đã kết nối đến MySQL database")

            # Tạo cursor để thực hiện truy vấn
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM employee")  # Thay 'table_name' bằng tên bảng của bạn
            
            # Lấy kết quả
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    except Error as e:
        print("Lỗi khi kết nối đến MySQL", e)

    finally:
        # Đóng kết nối
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Kết nối đã được đóng")

# Gọi hàm kết nối
if __name__ == "__main__":
    connect()