from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class DashData(models.Model):
    # rest = models.CharField(max_length=100)
    # revu = models.IntegerField()
    # pers = models.IntegerField()
    # created_at = models.DateTimeField()
    regDate = models.DateField()
    restaurant = models.CharField(max_length=300)
    personnel = models.IntegerField(null=True)
    revenue = models.IntegerField()
    district = models.CharField(max_length=500, default = '')
    
    # def __str__(self):
    #     return f'{self.rest}--{self.revu}'
    
    # class Meta:
    #     verbose_name_plural = "각 자치구별 맛집 순위"

# class Post(models.Model):
#     category = models.ForeignKey(Dong, null=True, blank=True, on_delete=models.SET_NULL)    

# class Dong(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#     slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    
    # class Meta:
    #     verbose_name_plural = '자치구별 식당'
    
    # def __str__(self):
    #     return self.name