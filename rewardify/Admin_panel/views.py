from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import App
from rest_framework import generics, request
from django.http import HttpResponse
from django.contrib.auth import logout


def redirect_add_app(request):
    """Redirecting to the relevant function"""
    return redirect('add_app')

def add_app(request):
    """Adding app details by the admin"""
    
    if request.method=='POST':
        appname=request.POST.get('app_name')
        downloadlink=request.POST.get('download_link')
        points=request.POST.get('points')

        print('appname:',appname)
        print('dl:',downloadlink)
        print('pointsl:',points)

        if appname and downloadlink and points:
            app = App(app_name=appname, download_link=downloadlink, points=points)
            app.save()    
        else:
            return HttpResponse({'status':'error', 'message':'All fields are required'})    

        return render(request,'admin_page/add_app.html')
    
    return render(request, 'admin_page/add_app.html')

def logout(request):
    """Logout"""
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('main_page')