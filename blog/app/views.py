from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import post
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

# def index(request):
    #persons = person.objects.all()
    #return render(request,"index.html",{"persons":persons})



def index(request):
    posts = post.objects.all().values("title","content","person__name","person__email","person__gender","image")
    return render(request,"index.html",{"posts":posts})



def search_action(request):
    search_item = request.GET.get("search_item")
    posts = post.objects.filter(person__name__icontains=search_item).values("title","content","person__name","person__email","person__gender")
    return render(request,"index.html",{"posts":posts})
def search(request):
    return render(request,"search.html")
def signup(request):
        return render(request,"signup.html")
def signin(request):
        return render(request,"signin.html")

def signup_action(request):
    username = request.POST.get("email")
    password = request.POST.get("password")
    name = request.POST.get("name")
    user = User.objects.create_user(username=username,password=password,first_name=name)
    auth.login(request,user=user)
    return redirect('index')

def signin_action(request):
    username = request.POST.get("email")
    password = request.POST.get("password")
    user = auth.authenticate(request,username=username,password=password)
    auth.login(request,user=user)
    return redirect('index')



