from django.shortcuts import render

# Create your views here.
def loginPage(request):
    return render(request, 'user_auth/login.html', {})

def registerPage(request):
    return render(request, 'user_auth/register.html', {})