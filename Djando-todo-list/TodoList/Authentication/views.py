from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    return render(request,'Authentication/register.html')



def login_user(request):
     return render(request,'Authentication/login.html')
