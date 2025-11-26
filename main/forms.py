from django import forms 


clue_options = (
    ("t","تجربی"),
    ("e","انسانی"),
    ("r","ریاضی"),
)

source_options = (
    ("local","اکسل‌‌ها"),
    ("kanon","کانون"),
    ("hiva","هیوا"),
)

class MainForm(forms.Form):
    clue =  forms.ChoiceField(choices=clue_options , label='رشته')
    source =  forms.ChoiceField(choices=source_options , label='منبع')