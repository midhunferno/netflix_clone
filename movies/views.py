from django.shortcuts import render,redirect
from .models import Movies
from customer.models import Profile

# Create your views here.
def index(request):    
    return render(request,'index.html')
def movie_list(request,profile_id):
    try:
        profile=Profile.objects.get(uuid=profile_id)
        movie = Movies.objects.filter(agel_limit=profile.age_limit)
        if not profile:
            return redirect('profile')
        context={
            'movie':movie
         }
        return render(request,'movie_list.html',context)
    except Profile.DoesNotExist:
        return redirect('profile')

def movie_details(request,movies_id):
    try:
        movies=Movies.objects.get(uuid=movies_id)
        context={
            'movie':movies
        }
        return render(request,'movie_details.html',context)
    except Movies.DoesNotExist:
        return redirect('profile')