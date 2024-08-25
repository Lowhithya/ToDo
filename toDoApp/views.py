from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        task=request.POST.get('task')
        newToDo=todo(user=request.user, todo_name=task)
        newToDo.save()

    all_todos=todo.objects.filter(user=request.user)
    context={
        'todos':all_todos
    }    
    return render(request, 'toDoApp/todo.html',context)

def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('uname')
        password= request.POST.get('pass')

        validateUser=authenticate(username=username,password=password)
        if validateUser is not None:
            login(request,validateUser)
            return redirect('home-page')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'toDoApp/login.html',{})

def logoutView(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password)<3:
            messages.error(request, "Password should be at least 3 characters long")
            return redirect('register')
        
        get_all_usernames=User.objects.filter(username=username)
        if get_all_usernames:
            messages.error(request, "Username already exists, Use another UserName!")
            return redirect('register')

        new_user=User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        messages.success(request, "User Successfully Registered! Login Now.")
        return redirect('login')
    return render(request, 'toDoApp/register.html',{})

@login_required
def deleteTask(request,name):
    get_todo=todo.objects.get(user=request.user, todo_name=name)
    get_todo.delete()
    return redirect('home-page')
    

def Update(request,name):
    get_todo=todo.objects.get(user=request.user, todo_name=name)
    get_todo.status=True
    get_todo.save()
    return redirect('home-page')