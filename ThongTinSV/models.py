from django.db import models
from django.contrib import admin

# Create your models here.
class SinhVien(models.Model):
    MA_GIOI_TINH = (
        ('Nam', 'Nam'),             #('giá_trị_lưu_trong_db', 'giá_trị_hiển_thị')
        ('Nữ', 'Nữ'),
        ('Khác', 'Khác'),
    )

    ma_sinh_vien = models.CharField(max_length=20, unique=True)  # Mã sinh viên
    ho_ten = models.CharField(max_length=50)                         # Họ Tên
    gioi_tinh = models.CharField(max_length=10, choices=MA_GIOI_TINH)
    ngay_sinh = models.DateField()
    email = models.EmailField()
    so_dien_thoai = models.CharField(max_length=10)
    dia_chi = models.TextField()
    lop = models.CharField(max_length=20)                        # Lớp học (ví dụ: D15CQCN01)
    nganh = models.CharField(max_length=100)                     # Ngành học
    khoa = models.CharField(max_length=100)                      # Khoa
    # ngay_nhap_hoc = models.DateField()
    # anh_dai_dien = models.ImageField(upload_to='sinhvien_avatars/', null=True, blank=True)
    def __str__(self):
        return f"{self.ma_sinh_vien} |  {self.ho_ten} | {self.lop} |  {self.nganh}"

class SinhVienAdmin(admin.ModelAdmin):
    list_display = ('ma_sinh_vien', 'ho_ten', 'lop', 'nganh')  # Cột hiển thị
  

    
    