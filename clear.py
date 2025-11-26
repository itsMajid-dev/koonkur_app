import re 

def clear_excel(text):
    pattern = r"[\u0600-\u06FF\uFB8A\u067E\u0686\u06AF\u200C\u200F ]+"
    persian_text = re.findall(pattern, text)
    result = " ".join(persian_text).strip()
    return result