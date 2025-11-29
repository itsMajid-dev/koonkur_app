from bs4 import BeautifulSoup
import httpx 
import os 
from django.contrib import messages 

# riazi = 1
# tajrobi = 2
# ensani = 3


class Crawel:
    def __init__(self , clue:int , sahmie:int , ):
        self.is_table = False
        self.clue = clue 
        self.sahmie = sahmie
        self.url = 'https://www.kanoon.ir/Public/SuperiorsRankBasedShowSuperiors'
        self.cookies ={
            "_ga": "GA1.1.1642763471.1763470685",
            "_ga_97JH6MD3F9": "GS2.1.s1764238857$o2$g1$t1764238875$j42$l0$h0",
            "kanoonirSession": "111e93ae-fe2a-4d7a-bfa1-d8bb88df3d7e",
            "kfacommnet": "cd802ba4-8468-4833-919b-c1e2f9c2b0e3",
        }
        self.header =  {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.kanoon.ir/Public/SuperiorsRankBased?type=3",
            "Content-Type": "application/json; charset=utf-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://www.kanoon.ir",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Priority": "u=0",
            "TE": "trailers"
        }
        self.data = {
            "dept": f"{self.clue}",
            "sahmieh": f"{self.sahmie}", 
            "rank": "0",
            "reshte": None,  
            "year": "103",
            "univercity": None, 
            "type": "3"
        }

    def is_file(self , *path):
       main_path = os.path.dirname(__file__)
       path_file = os.path.join(main_path ,*path )
       return {'status' : os.path.isfile(path_file) ,'path' :  path_file}


    def get_table(self):
        table_name = f'{self.clue}-{self.sahmie}.html'
        status =self.is_file('data' , 'table' , table_name )
        if status['status']:
            self.path = status['path']
            self.is_table = True
            return self.is_table
        else:
            self.path = status['path']
            self.bot = httpx.Client(http2=False)
            res = self.bot.post(self.url,
                                json=self.data,
                                headers=self.header,
                                cookies=self.cookies,
                                )
            if res.status_code!=200:
                return f'ERR : {res.status_code}'
            f = open(self.path , 'w' , encoding='utf-8')
            f.write(res.text)
            f.close()
            self.is_table = True
            return self.is_table
        
    def get_data(self , model):
        if self.is_table==False:
            return False
        else:
            html = open(self.path , 'r' , encoding='utf-8').read()
            soup = BeautifulSoup(html , 'html.parser')
            table = soup.find('table', class_='table table-bordered Superior')

            for row in table.find_all('tr')[1:]:
                cells = row.find_all(['td', 'th'])
                if len(cells) >= 5: 
                    rank_country = cells[1].get_text(strip=True)  
                    rank_sahmie = cells[2].get_text(strip=True)  
                    city = cells[5].get_text(strip=True)  
                    reshte = cells[6].get_text(strip=True) 
                    if self.sahmie==1:
                        model.objects.create(
                            rank_country = rank_country,
                            city = city,
                            rank_1 = rank_sahmie,
                            reshte='ریاضی',
                            clue = reshte,
                            source = 'kanon',
                        ).save()
                    elif self.sahmie==2:
                        model.objects.create(
                            rank_country = rank_country,
                            city = city,
                            rank_2 = rank_sahmie,
                            reshte='ریاضی',
                            clue = reshte,
                            source = 'kanon',
                        ).save()
                    elif self.sahmie==3:
                        model.objects.create(
                            rank_country = rank_country,
                            city = city,
                            rank_3 = rank_sahmie,
                            reshte='ریاضی',
                            clue = reshte,
                            source = 'kanon',
                        ).save()

        
            return True
        

       
    



        


            


        
