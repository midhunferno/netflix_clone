from django.shortcuts import render

# Create your views here.
def index(request):    
    return render(request,'index.html')
def movie_list(request):
    return render(request,'movie_list.html')