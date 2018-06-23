from typing import Optional, Any

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,get_user_model
from .forms import ContactForm,LoginForm,RegisterForm
def home_page(request):
    context={

    }
    # return HttpResponse(request,"Hiii")
    return render(request,"home_page.html",{})

def about_us(request):
    context={

    }
    return render(request,"home_page.html",{})

def contact_page(request):
    form=ContactForm(request.POST or None)
    context={
     "form":form,
    }
    if form.is_valid():
        print(form.cleaned_data)
    # if request.method=="POST":
    #     print(request.POST.get('username'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request,"home_page.html",context)

def login_page(request):
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(request,username='username',password='password')
        print(user)
        if user is not None:
            login(request,user)
            redirect("/")
        else:
            print("error")


    return render(request,"auth/login_page.html",context)

User=get_user_model()

def register_page(request):

    form=RegisterForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        User.objects.create_user(username,email,password)
    return render(request,"auth/register_page.html",context)


