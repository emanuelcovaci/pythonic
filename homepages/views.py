from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'homepages/home.html')

def graphics(request):
    return render(request,'grafic.html')