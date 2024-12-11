from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
# Create your views here.

def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'], email=data['email'],
                                            first_name=data['first_name'],
                                            last_name=data['last_name'], password=data['password_2'])
            user.save()
            messages.success(request, 'you were registered', 'success')
            return redirect('home:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})