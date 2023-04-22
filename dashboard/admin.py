# from django.contrib import admin
from django.contrib import admin
from .models import DashData

# admin site dashboard list ui 바꾸기
# UI 변경 클래스 정의
## admin.ModelAdmin 상속 받기
# admin.site.register(모델클래스, UI 재정의 클래스)

class DashboardAdmin(admin.ModelAdmin):
    list_display = ("regDate", "restaurant", "personnel", "revenue", "district")
    
    # Register your models here.
    admin.site.register(DashData)


# Register your models here.
# class DongAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name', )}

#     admin.site.register(Dong, DongAdmin)