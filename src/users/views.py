from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy



def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                passw = form.cleaned_data['password1']
                user.save()
                auth = authenticate(username=user,password=passw)
                login(request, auth)


                messages.success(request, f'Your account has been created. You can log in now!')    
                return redirect('/')
               

        else:
            form = UserRegistrationForm()

        context = {'form': form}
        return render(request, 'users/register.html', context)

def logins(request):
    return render(request, "users/login.html")

def password_reset(request):
    return render(request,"password/password_reset.html")

def change_password(request):
    return render(request,"password/change_password.html" )


def wishlist(request):
    return render(request, "users/wishlist.html")

def logout_user(request):
    logout(request)
    return redirect("/")


class LoginUserWithClass(auth_views.LoginView):
    success_url = reverse_lazy("index:index")
    

