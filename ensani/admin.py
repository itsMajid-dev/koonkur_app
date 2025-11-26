from django.contrib import admin
from .models import Ensani

class EAdmin(admin.ModelAdmin):
    list_display = ['clue', 'rank_1' , 'rank_2' , 'rank_3' , 'rank_5_percentage' , 'rank_25_percentage']

admin.site.register(Ensani , EAdmin)
