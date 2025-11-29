from bs4 import BeautifulSoup


with open('data.html', 'r', encoding='utf-8') as file:
    html_content = file.read()


soup = BeautifulSoup(html_content, 'html.parser')

# پیدا کردن تمام سطرهای جدول با کلاس Sahmieh-3
rows = soup.find_all('tr', class_='Sahmieh-3')

# لیست برای ذخیره داده‌ها
data = []

# استخراج داده از هر سطر
for row in rows:
    # پیدا کردن تمام سلول‌های <td> در این سطر
    cells = row.find_all('td')
    
    # استخراج متن از هر سلول و حذف فضاهای اضافی
    # row_data = [cell.get_text(strip=True) for cell in cells]
    row_data =[]
    for i in cells:
        row_data.append(i.text.strip())
        
    data.append(row_data)

# نمایش داده‌ها
for i, row in enumerate(data, 1):
    print(f"Row {i}: {row}")