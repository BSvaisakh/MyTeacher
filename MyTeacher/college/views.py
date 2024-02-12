from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,"home.html")

def collegeLogin(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        
        college = College.objects.filter(name=name).first()
        if college is not None :
            stored_pswd = college.password
            if password == stored_pswd :
                return render(request,"college_dashboard.html")
            response = f"""
                <script>
                window.alert('WRONG PASSWORD')
                window.location.href ='/';
                </script>
                """
            return HttpResponse(response)
        response = f"""
                <script>
                window.alert('No such User')
                window.location.href ='/';
                </script>
                """
        return HttpResponse(response)
    return render(request,"home.html")
            
        