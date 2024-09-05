from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import path, re_path, reverse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from Admin_panel.models import App
from Admin_panel.serializers import AppSerializer
from .models import Task, User_profile
from django.contrib.auth.decorators import login_required

def redirect_tasks_completed(request, user_id):
    return redirect('tasks_completed', user_id)

def redirect_upload_screenshot(request,user_id):
    return redirect('uploaded_screenshot')

def redirect_points(request, user_id):
    return redirect('points', user_id)

def redirect_profile(request, user_id):
    return redirect('profile', user_id=user_id)

def redirect_view_in_detail(request):
    return redirect('view_in_detail')

def redirect_signup(request):

    return redirect('login')

def redirect_login(request):
    if request.method == 'POST':        
        email = request.POST.get('email', None)
        name = request.POST.get('name', None)        
        password = request.POST.get('password',None)        

        user = User_profile.objects.create(email_id=email, name=name)    
        user.save()  

        if email==None or name==None or password==None:
            messages.error(request, 'Bad Credentials!')
            return redirect('home')
        else:    
            return redirect('main_page', user.id)
        
def redirect_logout(request, user_id):
    return redirect('login')

def home(request):
    """Renders the home page"""
    return render(request, "authentication/home.html")

def signup(request):
    """Signin to the app"""

    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm password']  

        user = User_profile.objects.create(email_id=email, name=name)    
        user.save() 

        messages.success(request, 'Your account has been successfully created')

        return redirect('login')

    return render(request, "authentication/signup.html")

def login(request):   
    """Login to the app"""

    return render(request, "authentication/login.html") #signup-login

def logout(request):
    """Logout of the app"""

    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('main_page')

def main_page(request, user_id):
    """Main page view"""

    apps=App.objects.all()
    return render(request, "authentication/main_page.html", {'apps':apps, 'user_id':user_id}) #, "user_detail":user_det}) 

def view_in_detail(request, app_id, user_id):
    """Gives the details of the app the user wants to download"""

    app = get_object_or_404(App, id=app_id)
    app_details = {
        'name': app.app_name,
        'download_link': app.download_link,
        'points':app.points,
        'user_id':user_id
    }
    return JsonResponse(app_details)

def upload_screenshot(request,user_id): 
    """Uploading screenshot"""
    
    if request.method == 'POST':
        app_id=request.POST['app_id']
        user_id=request.POST['user_id']

        app = App.objects.get(id=app_id)
        user=User_profile.objects.get(id=user_id)
        screenshot=request.FILES.get('screenshot')
        
        if not app or not screenshot or not user:
            return JsonResponse({'status': 'error', 'message': 'app or user or screenshot not received'}, status=403)   
        else:           
            task=Task.objects.create(user=user, app=app, screenshot=screenshot, points_earned=app.points)
            task.save()
        
        return JsonResponse({'status': 'success', 'message': 'Request received'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=403)
 

def profile(request, user_id):
    """View that shows user profile"""

    print(f"User ID: {user_id}")
    user_det = get_object_or_404(User_profile, id=user_id)
    user_details= {
        'id':user_det.id,
        'name': user_det.name,
        'email': user_det.email_id,
        'points':user_det.points_earned,
    }
    return render(request, "authentication/profile.html", {'user_details':user_details})

def points(request, user_id):
    """View that shows total points the user has earned"""

    user = User_profile.objects.get(id=user_id)
    total_points = Task.objects.filter(user=user).aggregate(total_points=Sum('points_earned'))['total_points']
    print(total_points)
    if total_points is None:
        total_points = 0 
   
    return render(request, "authentication/points.html", {'points':total_points})

def tasks_completed(request, user_id):
    """View that gives the list of apps the user has downloaded"""

    apps = []
    tasks = Task.objects.filter(user_id=user_id)    
    for task in tasks:
        app = get_object_or_404(App, id=task.app_id)  
        apps.append(app.app_name)
    return render(request, "authentication/tasks_completed.html", {'apps':apps})
