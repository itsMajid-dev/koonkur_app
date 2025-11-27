from django.contrib import messages 
from clear import clear_excel 
from .models import Ensani 
import pandas as pd 
import re 
import os 



def is_file(*file):
    """برسی وجود فایل اکسل انسانی در پوشه data"""
    main_path = os.path.dirname(__file__)
    path_file = os.path.join(main_path ,*file )
    return {'status' : os.path.isfile(path_file) ,'path' :  path_file}


def ensani(request):
    """نوع استخراج دیتای انسانی بر اساس منبع"""

    source  =  request.session['source']
    if source =='local':
        return  ensani_extract_from_excel(request) 




def ensani_extract_from_excel(request):
    """استخراجی دیتا از فایل اکسل"""


    F = is_file("..", "data", "excel", "e.xlsx")
    if not F['status']:
        messages.error(request , 'فایل اکسل انسانی وجود ندارد')
        return
    else:
        
        if Ensani.objects.filter(source='local').exists():
            messages.warning(request , 'قبلا دیتا استخراج شده است')
        else:
            path = F['path']
            df= pd.read_excel(path, header=None)
            current_clue = "-"  
            for i in range(3, len(df)):
                row = df.iloc[i]
                col0 = str(row[0]) if not pd.isna(row[0]) else ""
                if re.search(r"[\u0600-\u06FF]", col0) and (
                    pd.isna(row[1]) or pd.isna(row[2])
                ):
                    current_clue = clear_excel(col0)
                    rank_3 = rank_2 = rank_1 = 0
                    period = ""
                    univercity = ""
                else:
                    clue = current_clue
                    def clean_num(x):
                        if pd.isna(x):
                            return 0
                        x = str(x).replace("*", "").strip()
                        return int(x) if x.isdigit() else 0
                    rank_3 = clean_num(row[0])
                    rank_2 = clean_num(row[1])
                    rank_1 = clean_num(row[2])
                    period = "" if pd.isna(row[3]) else str(row[3])
                    univercity = "" if pd.isna(row[4]) else str(row[4])
            
                if rank_1 == rank_2 == rank_3 == 0 and period == "" and univercity == "":
                    continue
                Ensani.objects.create(
                    reshte='انسانی',
                    clue=clue,
                    univercity=univercity,
                    period=period,
                    rank_1=rank_1,
                    rank_2=rank_2,
                    rank_3=rank_3,
                    source = 'local'
                )
                
            messages.success(request , 'استخراج رتبه های انسانی با موفقیت به اتمام رسید')
        
        

    







