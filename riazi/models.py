from django.db import models

class Riazi(models.Model):
    reshte = models.CharField(max_length=10 , verbose_name='رشته تحصیلی' ,null=True , blank=True)
    clue = models.CharField(max_length=10 , verbose_name='رشته دانشگاهی',null=True , blank=True)
    univercity = models.CharField(max_length=100 , verbose_name='دانشگاه' , help_text='نام دانشگاه پذیرفته شده' ,null=True , blank=True)
    period = models.CharField(max_length=22 , verbose_name='دوره' ,null=True , blank=True)
    rank_1 = models.PositiveIntegerField(  verbose_name='رتبه منطقه 1' ,null=True , blank=True)
    rank_2 = models.PositiveIntegerField(  verbose_name='رتبه منطقه 2' ,null=True , blank=True)
    rank_3 = models.PositiveIntegerField( verbose_name='رتبه منطقه 3',null=True , blank=True)
    rank_5_percentage = models.PositiveIntegerField( verbose_name='رتبه سهمیه 5 درصد',null=True , blank=True)
    rank_25_percentage = models.PositiveIntegerField( verbose_name='رتبه سهیمه 25 درصد',null=True , blank=True)
    