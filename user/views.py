from django.shortcuts import render, redirect
from user.models import Job, Profile
from .forms import JobForm, UserForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def registe_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user,user_type=request.POST["user_type"])
            print("🚀 ~ file: views.py ~ line 19 ~ profile", profile)
            login(request, user)
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserForm()
    return render(request, "register.html", {"register_form":form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})


@login_required
def home(request):
    profile = Profile.objects.get(user=request.user)
    if profile.user_type == "admin":
        job = Job.objects.filter(created_by__user=request.user)
        return render(request, 'home.html', {"jobs":job, "user_type":"admin"})
    else:
        job = Job.objects.all()
        return render(request, 'home.html', {"jobs":job})


@login_required
def job_view(request):
    if request.method == "POST":
        data = {}
        data["name"] = request.POST["name"]
        data["description"] = request.POST["description"]
        data["category"] = request.POST["category"]
        data["price"] = request.POST["price"]
        data["length"] = request.POST["length"]
        profile = Profile.objects.get(user=request.user)
        data["created_by"] = profile.id
        form = JobForm(data)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = JobForm
    return render(request,'job.html',{"form":form})
        