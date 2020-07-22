from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import Login_Form , UserCreationForm , Update_Profile
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
  items = Profile.objects.all()
  context = {
   'title' : 'home',
   'items' : items ,
  }
  return render(request, 'home.html' , context)


def profile(request , slug):
  items_details = Profile.objects.get(slug = slug)
  context = { 'title' : 'profile' ,
              'items_details' : items_details
            }
  return render(request, 'doctor_profile.html' , context)

def register(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      new_user = form.save(commit=False)
      new_user.set_password(form.cleaned_data['password1'])
      new_user.save()
      messages.success(request, ('Registration is done Successfully! {}').format(new_user))
      return redirect('home')
  else:
    form = UserCreationForm()
  return render (request, 'register.html' , {'form': form})


def login_user(request):
  if request.method == "POST":
    form = Login_Form()
    username=request.POST['username']
    password=request.POST['password']
    user = authenticate(request, username=username , password=password)
    if user is not None :
      login = (request, user)
      messages.success(request, ('successfully registered {}').format(username))
      return redirect ('home')
    else:
      messages.warning(request,('username or password is not correct'))
  else:
    form = Login_Form()
  context={
    'form': form
    }
  return render(request, 'login.html' , context)


def logout_user(request):
  logout_user = logout(request)
  context = { 'title' : 'logout',
              'user_logout' : logout_user
            }
  return render(request, 'logout.html' , context)


@login_required(login_url='login')
def myprofile(request):
  return render(request, 'myprofile.html', {'title':'myprofile'})


def profile_update(request):
  form = Update_Profile(instance=request.user)
  context = { 'title' : 'profile_update',
               'form' : form
            }
  return render(request, 'profile_update.html' , context)
