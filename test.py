

# import httpx 

# url = 'https://www.kanoon.ir/Public/SuperiorsRankBasedShowSuperiors'

# headers = {
#     "Accept": "*/*",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Referer": "https://www.kanoon.ir/Public/SuperiorsRankBased?type=3",
#     "Content-Type": "application/json; charset=utf-8",
#     "X-Requested-With": "XMLHttpRequest",
#     "Origin": "https://www.kanoon.ir",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-origin",
#     "Priority": "u=0",
#     "TE": "trailers"
# }

# cookies = {
#     "_ga": "GA1.1.1642763471.1763470685",
#     "_ga_97JH6MD3F9": "GS2.1.s1764238857$o2$g1$t1764238875$j42$l0$h0",
#     "kanoonirSession": "111e93ae-fe2a-4d7a-bfa1-d8bb88df3d7e",
#     "kfacommnet": "cd802ba4-8468-4833-919b-c1e2f9c2b0e3",
# }

# data = {
#     "dept": "1",
#     "sahmieh": "3", 
#     "rank": "0",
#     "reshte": None,  
#     "year": "103",
#     "univercity": None, 
#     "type": "3"
# }

# bot = httpx.Client(http2=True)
# r = bot.post(url, json=data, cookies=cookies, headers=headers)
# print(r.status_code)
# if r.status_code ==200:
#     f = open('data.html' , 'w' , encoding='utf-8')
#     f.write(r.text)
#     f.close()