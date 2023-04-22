from django.shortcuts import render
from .models import DashData
from django.db.models import Count


# Create your views here.
def dashboard(request):
    top_5=DashData.objects.values("restaurant").annotate(name_count=Count('restaurant')).filter(name_count__gt=1)
    # print(top_5)
    order = top_5.order_by('-name_count')[:5] # order_by : 정렬 [:숫자] : 상위 숫자 만큼
    # print(order)


    context = {
        "chart":order
    }

    return render(request, "dashboard/dashboard1.html", context)
    # return render(request, "dashboard/dashboard1.html")
    