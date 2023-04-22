from django.forms import ModelForm
from .models import RestData

class RestDataForm(ModelForm):
    class Meta:
        model = RestData
        # restData 클래스의 모든 속성을 form field로 사용
        fields = '__all__'