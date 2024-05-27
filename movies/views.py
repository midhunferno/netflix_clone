from django.shortcuts import render,redirect
from .models import Movies
from customer.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request): 
     
    return render(request,'index.html')

@login_required
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
@login_required
def movie_details(request,movies_id):
    try:
        movies=Movies.objects.get(uuid=movies_id)
        context={
            'movie':movies
        }
        return render(request,'movie_details.html',context)
    except Movies.DoesNotExist:
        return redirect('profile')
   
@login_required   
def play(request,movies_id):
    try:
        movie=Movies.objects.get(uuid=movies_id)
        video=movie.video.all()
        context={
            'movie':movie,
            'video':video
        }
        return render(request,'play_movie.html',context)
    except Movies.DoesNotExist:
        return redirect('profile')
    