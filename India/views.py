from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from .models import *
from .forms import *
# Create your views here.

db_user=get_user_model()

def index(request):
    if not request.user.is_authenticated:
        authenticated= False
        return redirect(reverse('map:login'))
    username= CustomUser.objects.get(pk=request.user.id)
    map = Map.objects.all()
    authenticated = True
    try:
        user= Member.objects.filter(user=username)
        userid=user.id
        print(userid)
        # community=user.community.all()
    except:
        user=None
    return render(request, "India/Map.html",{
        "userid": user,
        "state": map,
        "authenticated":authenticated
        
    })

def signup(request):
    if request.method== "POST":
        form= CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("map:index")
    form=CustomUserCreationForm()
    return render(request,"India/signup.html",{
        "form":form
        
    })


def login_view(request):
    if request.method == "POST":
        mail= request.POST["email"]
        password=request.POST["password"]
        user = authenticate(request, email=mail, password=password)
        if user:
            login(request,user)
            return redirect('map:index')
        else:
            return redirect('map:signup')
        
    return render(request, "India/login.html" )



def logout_view(request):
    logout(request)
    return render(request,"India/login.html",{
        "message":"Logged Out!"
    })

def state(request,state_id):
    state= Map.objects.get(pk=state_id)
    user= CustomUser.objects.get(pk=request.user.id)
    try:
        member= state.communities.get(user=user)
        print(member)
    except:
        member=None
    return render(request,"India/state.html",{
        "state":state,
        "member":member
    })


def add_member(request,state_id):
    state=Map.objects.get(pk=state_id)
    username=CustomUser.objects.get(pk=request.user.id)
    if request.method == "POST":
        member = Member()
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)
            member.user = username
        try:  
            member.community.add(state)
            member.save()
        except:
            return render(request, "India/add.html",{
                "status": "Internal Server Error"
            })
        return redirect("map:state",state_id)
    return render(request, "India/add.html",{
        "stateid":state_id,
        "state":state.name,
        "form":MemberForm()
        
    })