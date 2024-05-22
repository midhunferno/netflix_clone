from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib.auth.hashers import make_password

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
    return render(request,'login.html')