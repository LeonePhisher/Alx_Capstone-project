from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user_data_has_error = False

        if not (first_name and last_name and username and email and password and confirm_password):
            messages.error(request, 'All fields are required!')
            user_data_has_error = True

        if User.objects.filter(username=username).exists():
            messages.error(request, 'A user with that username already exists!')
            user_data_has_error = True
            
        if User.objects.filter(email=email).exists():
            messages.error(request, 'A user with that email already exists!')
            user_data_has_error = True

        if len(password) < 5:
            messages.error(request, 'Password must be at least 5 characters!')
            user_data_has_error = True
            
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            user_data_has_error = True

        if user_data_has_error:          
            return redirect('register')
         user=User.objects.create_user(
            username=username,
            password = password,
            first_name = first_name,
            last_name = last_name
        )
        user.save()
    return render(request,'Authentication/register.html')
    
         
         
def login_user(request):
     return render(request,'Authentication/login.html')

