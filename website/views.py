 
 
from django.shortcuts import render ,redirect # type: ignore
from django.contrib.auth import login,logout,authenticate # type: ignore
from django.contrib import messages   # type: ignore
# Create your views here.
def home (request):
    #check to see if logging in
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,'you have been Logged IN')
            return redirect('home') # type: ignore
        else:
            messages.success(request,'error failed to logging')
            return redirect('home') # type: ignore
    return render(request,'home.html',{})

def register_user (request):
    return render(request,'register.html',{})

def logout_user (request):
    logout(request)
    return render(request,'home.html',{})
