from django.urls import path
from . import views

app_name = "input"

urlpatterns = [
    # BASIC URL --> localhost:8000/info/
    path("", views.index, name="index"),
    # 입력 요청 처리
    path("createInfo/", views.createInfo),
    # 수정페이지 요청 -> http://localhost:8000/info/edit/1
    path("edit/<str:idx>", views.editForm),
    path("edit/update/", views.updateInfo),
    path("delete/<str:idx>", views.deleteInfo),
    path("qrcode/<str:idx>", views.qrCode),
]
