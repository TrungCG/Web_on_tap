from django.contrib import admin

# Register your models here.
from .models import SinhVien
from .models import SinhVienAdmin

admin.site.register(SinhVien, SinhVienAdmin)


