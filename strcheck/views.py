from django.shortcuts import render

# Create your views here.
def index(request):
    s1 = "the quick brown fox jumped right over the little lazy dog and run and run and run and run"
    s2 = "fvnjnvnnvfjn"
    cat_dict = {'stories':{'story1':s1,'story2':s2}}
    return render(request,"index.html",context=cat_dict)
