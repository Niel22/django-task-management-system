from django.shortcuts import render, redirect
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def loginPage(request):

    
    errors = {}
    if request.method == "POST":
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        email_regex = r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not email:
            errors['email'] = "Email is required."
        elif not re.match(email_regex, email):
            errors['email'] = "Enter a valid email."

        if not password:
            errors['password'] = "Password field is required"
        
        if errors:
            return render(request, 'user_auth/login.html', {'errors' : errors})
        
        validated_user = authenticate(email=email, password=password)

        if validated_user is not None:
            login(request, validated_user)
            return redirect('home')
        

        errors['email'] = "Invalid email or password."
        return render(request, 'user_auth/login.html', {'errors' : errors})
        
        
    # Default login page
    return render(request, 'user_auth/login.html', {})

def registerPage(request):
      
    if request.method == "POST":
        errors = {}
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not name:
            errors['name'] = "Name is required"
        elif len(name) < 3:
            errors['name'] = "Name must be more than 3 characters long"

        email_regex = r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not email:
            errors['email'] = "Email is required."
        elif not re.match(email_regex, email):
            errors['email'] = "Enter a valid email."
        elif User.objects.filter(email=email):
            errors['email'] = "Email has already being taken"
        
        if not username:
            errors['username'] = "Username is required"
        elif User.objects.filter(username=username):
            errors['username'] = "Username already taken"
        
        if not password:
            errors['password'] = "Password field is required"
        elif len(password) < 8:
            errors['password'] = "Password should not be less than 8 characters"
        
        if errors:
            return render(request, 'user_auth/register.html', {'errors' : errors})
        
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.name = name
        new_user.save()

        messages.success(request, "You have been registered, now proceed to login")
        return redirect('loginPage')

    return render(request, 'user_auth/register.html', {})

def logout(request):
    logout
    return redirect('loginPage')