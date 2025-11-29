from bs4 import BeautifulSoup

# خواندن فایل HTML
with open('data.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# ایجاد شیء BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# پیدا کردن جدول
table = soup.find('table', class_='table table-bordered Superior')

# استخراج داده‌ها از ردیف‌ها
data = []
for row in table.find_all('tr')[1:]:  # رد کردن هدر
    cells = row.find_all(['td', 'th'])
    
    if len(cells) >= 5: 
        rank_country = cells[1].get_text(strip=True)  
        rank_sahmie = cells[2].get_text(strip=True)  
        city = cells[5].get_text(strip=True)  
        reshte = cells[6].get_text(strip=True) 

        
        data.append([rank_country, rank_sahmie, city , reshte])

# نمایش نتایج
for row in data:
    print(row)