from django.contrib.auth.models import User,auth
from urllib import request
from django.shortcuts import redirect, render
from django.contrib import messages



def index(request):
    return render(request,"shop/index.html")

def register(request):
    return render(request,"shop/register.html")

def onlineorder(request):
    return render(request,"shop/onlineorder.html")

def menu(request):
    return render(request,"shop/menu.html")

def breakfastveg(request):
    return render(request,"shop/breakfastveg.html")

def breakfastnon(request):
    return render(request,"shop/breakfastnon.html")

def lunchveg(request):
    return render(request,"shop/lunchveg.html")

def lunchnon(request):
    return render(request,"shop/lunchnon.html")

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Name taken")
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                  messages.info(request,"email id exists")
                  return redirect('/signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.info(request,"Name taken")
                return redirect('/register')
        else:
             messages.info(request,"User created")
             return redirect('/register')
    
    return render(request,"shop/signup.html")

def foodrecom(request):
    return render(request,"shop/foodrecom.html")

def contact(request):
    return render(request,"shop/contact.html")

def cart(request):
    return render(request,"shop/cart.html")

def juice(request):
    return render(request,"shop/juice.html")

def chatsveg(request):
    return render(request,"shop/chatsveg.html")

def dinnerveg(request):
    return render(request,"shop/dinnerveg.html")

def dinnernon(request):
    return render(request,"shop/dinnernon.html")

def soups(request):
    return render(request,"shop/soups.html")

def starters(request):
    return render(request,"shop/starters.html")

def combo(request):
    return render(request,"shop/combo.html")

def editlist(request):
    return render(request,"shop/editlist.html")

def about(request):
    return render(request,"shop/about.html")