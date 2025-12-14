from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

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

        if not all([first_name, last_name, username, email, password, confirm_password]):
            messages.error(request, 'All fields are required!')
            user_data_has_error = True

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            user_data_has_error = True

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            user_data_has_error = True

        if len(password) < 4:
            messages.error(request, 'Password must be at least 4 characters!')
            user_data_has_error = True

        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            user_data_has_error = True

        if user_data_has_error:
            return redirect('register')

        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'Authentication/register.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'Authentication/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
