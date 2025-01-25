from django.db import models
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # ID sản phẩm
    name = models.CharField(max_length=255)  # Tên sản phẩm
    description = models.TextField(blank=True)  # Mô tả sản phẩm
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Giá sản phẩm
    quantity = models.IntegerField(default=0)  # Số lượng sản phẩm
    image_url = models.URLField(blank=True)  # Đường dẫn hình ảnh
    category = models.CharField(max_length=100, blank=True)  # Loại hàng
    origin = models.CharField(max_length=100, blank=True)  # Xuất xứ
    created_at = models.DateTimeField(auto_now_add=True)  # Ngày tạo

    class Meta:
        db_table = 'product'  # Tên bảng trong cơ sở dữ liệu

    def __str__(self):
        return self.name  # Trả về tên sản phẩm