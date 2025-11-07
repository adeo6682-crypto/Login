from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import User

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        hashed_pw = make_password(password)
        User.objects.create(full_name=name, email=email, password_hash=hashed_pw)
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email).first()
        if user and check_password(password, user.password_hash):
            request.session['user_id'] = user.user_id
            return redirect('dashboard')
        messages.error(request, 'Invalid credentials!')
    return render(request, 'login.html')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('login')
    user = User.objects.get(user_id=request.session['user_id'])
    return render(request, 'dashboard.html', {'user': user})

def logout_view(request):
    request.session.flush()
    return redirect('login')
