from django.contrib import admin
from .models import Riazi

class RAdmin(admin.ModelAdmin):
    list_display = ['clue', 'rank_1' , 'rank_2' , 'rank_3' , 'rank_5_percentage' , 'rank_25_percentage']

admin.site.register(Riazi , RAdmin)
