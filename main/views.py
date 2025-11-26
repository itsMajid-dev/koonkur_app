from django.shortcuts import render
from .forms import MainForm
from tajrobi.views import tajrobi 
from ensani.views import ensani
from riazi.views import riazi


def main_veiws(request):
    form = MainForm()
    if request.method =='POST':
        clue = request.POST.get("clue")
        source = request.POST.get("source")
        request.session['source'] = source
        if clue=='t':
           tajrobi(request)
        elif clue=='e':
            ensani(request)
        elif clue =='r':
            riazi(request)


            

    return render(request , 'main.html' , {'form':form})
