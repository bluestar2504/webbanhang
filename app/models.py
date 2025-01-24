from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)  # Tên nhân viên
    last_name = models.CharField(max_length=100)   # Họ nhân viên
    email = models.EmailField(default='default@example.com', unique=True)          # Địa chỉ email, cần phải duy nhất
    hire_date = models.DateField(default='2024-01-01', unique=True)                 # Ngày tuyển dụng
    job_title = models.CharField(default='abc',max_length=100)    # Chức danh công việc
    salary = models.DecimalField(default='1000',max_digits=10, decimal_places=2)  # Lương, với độ chính xác

    class Meta:
        db_table = 'employee'  # Tên bảng trong cơ sở dữ liệu

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # ID sản phẩm
    name = models.CharField(max_length=255)  # Tên sản phẩm
    description = models.TextField(blank=True)  # Mô tả sản phẩm
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Giá sản phẩm
    quantity = models.IntegerField()  # Số lượng sản phẩm
    image_url = models.URLField(blank=True)  # Đường dẫn hình ảnh
    category = models.CharField(max_length=100, blank=True)  # Loại hàng
    origin = models.CharField(max_length=100, blank=True)  # Xuất xứ
    created_at = models.DateTimeField(auto_now_add=True)  # Ngày tạo

    class Meta:
        db_table = 'product'  # Tên bảng trong cơ sở dữ liệu

    def __str__(self):
        return self.name  # Trả về tên sản phẩm