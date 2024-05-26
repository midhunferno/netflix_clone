from django.shortcuts import render,redirect
from .models import CustomUser,Profile
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username=request.POST['Username']
        email=request.POST['email']
        password=request.POST['password']
        conform_password=request.POST['password2']
        if password != conform_password:
            err="Passwords do not match"    
            return render(request,'signup.html',{'err':err})
        elif CustomUser.objects.filter(username=username).exists():
            err1="This username already exists"
            return render(request,'signup.html',{'err':err1})
        else:
         user=CustomUser.objects.create(
            username=username,
            email=email,
            password=make_password(password),
            conform_password=make_password(conform_password)          
        )
        user.save()
        return redirect('login')
    return render(request,'signup.html')

def log_in(request):
    if request.method == 'POST':
        username=request.POST['Username']
        password=request.POST['password']
        user=authenticate( request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('profile')
        elif not user:
            err="Wrong credentials"
            return render(request,'login.html',{'err':err})
    return render(request,'login.html')

def log_out(request):
    logout(request)
    return redirect('index')

def profil(request): 
    profil_show=Profile.objects.all()
    context={
        'profil_show':profil_show
    }
    return render(request,'profile.html',context)

def profile_creat(request):
    if request.method == 'POST':
        profile_name=request.POST['profile_name']
        age_limit=request.POST['age_limit']

        profil_user=Profile.objects.create(
            name=profile_name,
            age_limit=age_limit                                       
        )
        profil_user.save()
        if profil_user:
            request.user.profile.add(profil_user)
            return redirect('profile')
    return render(request,'profile_creation.html')