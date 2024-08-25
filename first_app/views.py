from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeUserDataForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def singup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account Created Successfully')
                form.save()
                print(form.cleaned_data)
                return redirect('login')  # Redirect to login page after successful signup
        else:
            form = RegisterForm()
        return render(request, 'singup.html', {'form': form})
    else:
        return redirect('profile')  # Redirect authenticated users to profile page

def home(request):
    return render(request, 'home.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserDataForm(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
                return redirect('profile')  # Redirect to profile page after successful update
        else:
            form = ChangeUserDataForm(instance=request.user)
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('login')  # Redirect unauthenticated users to login page

def userlogout(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'passchange.html', {'form': form})
    else:
        return redirect('login')

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'passchange.html', {'form': form})
    else:
        return redirect('login')


def change_user_data(request):
    if  request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserDataForm(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated Successfully')
                form.save()
                print(form.cleaned_data)
                return redirect('login')  # Redirect to login page after successful signup
        else:
            form =ChangeUserDataForm()
        return render(request, 'singup.html', {'form': form})
    else:
        return redirect('singup')  # Redirect authenticated users to profile page