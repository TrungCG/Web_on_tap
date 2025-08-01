
# QuerySet trong Django

`QuerySet` trong Django đại diện cho một tập hợp các đối tượng được lấy từ cơ sở dữ liệu. Đây là cách làm việc với dữ liệu kiểu tương đương với câu lệnh SQL `SELECT`.

---

## 1. Mô hình mẫu

```python
# models.py
from django.db import models

class SinhVien(models.Model):
    ten = models.CharField(max_length=100)
    tuoi = models.IntegerField()
    lop = models.CharField(max_length=20)
    gioi_tinh = models.CharField(max_length=10, choices=[("Nam", "Nam"), ("Nữ", "Nữ")])

    def __str__(self):
        return self.ten
```

---

## 2. Truy vấn cơ bản với QuerySet

### 2.1. Lấy tất cả bản ghi
```python
SinhVien.objects.all()
```

### 2.2. Lấy một bản ghi duy nhất
```python
SinhVien.objects.get(id=1)
```

### 2.3. Lọc dữ liệu
```python
SinhVien.objects.filter(lop='12A1')
SinhVien.objects.filter(tuoi__gte=18)
SinhVien.objects.filter(ten__icontains='an')
```

---

## 3. Các toán tử truy vấn

| Toán tử        | Mô tả                             |
|----------------|-----------------------------------|
| `exact`        | chính xác                         |
| `iexact`       | chính xác, không phân biệt hoa/thường |
| `contains`     | chứa                             |
| `icontains`    | chứa, không phân biệt hoa/thường |
| `gt`, `gte`    | lớn hơn, lớn hơn hoặc bằng        |
| `lt`, `lte`    | nhỏ hơn, nhỏ hơn hoặc bằng         |
| `in`           | nằm trong danh sách               |
| `startswith`   | bắt đầu bằng                     |
| `endswith`     | kết thúc bằng                    |

---

## 4. Truy vấn nâng cao

### 4.1. Sắp xếp
```python
SinhVien.objects.order_by('tuoi')
SinhVien.objects.order_by('-tuoi')
```

### 4.2. Giới hạn số lượng
```python
SinhVien.objects.all()[:5]
```

### 4.3. Loại bỏ trùng
```python
SinhVien.objects.values('lop').distinct()
```

---

## 5. Các phương thức đặc biệt

| Phương thức             | Ý nghĩa                      |
|-------------------------|------------------------------|
| `.count()`              | Đếm số lượng bản ghi         |
| `.first()`, `.last()`   | Lấy bản ghi đầu/cuối         |
| `.exists()`             | Kiểm tra có tồn tại hay không |
| `.values()`             | Trả về dict                  |
| `.values_list()`        | Trả về danh sách giá trị     |
| `.update()`             | Cập nhật nhiều bản ghi       |
| `.delete()`             | Xoá bản ghi                  |

Ví dụ:
```python
SinhVien.objects.filter(lop='12A1').count()
SinhVien.objects.filter(lop='12A1').values_list('ten', flat=True)
SinhVien.objects.filter(lop='12A1').update(tuoi=18)
```

---

## 6. Sử dụng Q và F để truy vấn nâng cao

```python
from django.db.models import Q, F

# Điều kiện OR
SinhVien.objects.filter(Q(tuoi__gt=18) | Q(gioi_tinh="Nữ"))

# So sánh giữa 2 trường
SinhVien.objects.filter(tuoi__gt=F('id'))
```

---

## ✅ Ghi nhớ

- QuerySet là **lazily evaluated** – chỉ thực sự truy vấn khi cần dùng dữ liệu.
- Bạn có thể **xếp chồng các truy vấn** như `.filter().order_by()` để xử lý linh hoạt.
- Có thể dùng trong `views.py`, `shell`, hoặc tích hợp vào `template`.
