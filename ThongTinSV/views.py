from django.shortcuts import render
from django.http import Http404

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import SinhVien

def index(Request):
    return HttpResponse("Hello")


def index1(request):
    return HttpResponse("chao")

def index(request):
    latest_SinhVien_list = SinhVien.objects.order_by('-id')
    # order_by() là một phương thức của QuerySet, dùng để sắp xếp kết 
    # quả truy vấn từ cơ sở dữ liệu.
    '''
    template = loader.get_template("ThongTinSV/index.html")
    context = {"latest_SinhVien_list": latest_SinhVien_list}
    return HttpResponse(template.render(context, request))
    '''
    context = {"latest_SinhVien_list": latest_SinhVien_list}
    return render(request, "ThongTinSV/index.html", context)

def detail(request, SinhVien_id):
    try:
        sinhvien = SinhVien.objects.get(pk=SinhVien_id)
    except SinhVien.DoesNotExist:
        raise Http404("sinhvien does not exist")
    return render(request, "ThongTinSV/detail.html", {"sinhvien": sinhvien})