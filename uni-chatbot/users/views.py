from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from django.contrib.auth import login

# Tutorial in https://www.youtube.com/watch?v=DIFaOkxy6TE&list=PL0Zuz27SZ-6NamGNr7dEqzNFEcZ_FAUVX&index=9

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("/")
    else: #Not a POST    
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #LOGIN HERE
            login(request, form.get_user())
            return redirect("/")
    else: 
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})
