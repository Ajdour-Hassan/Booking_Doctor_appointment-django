from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def home(request):
  items = Profile.objects.all()
  context = {
   'title' : 'home',
   'items' : items ,
  }
  return render(request, 'home.html' , context)


def profile(request , slug):
  item_details = Profile.objects.get(slug = slug)
  context = { 'title' : 'profile' , 'item_details': item_details}
  return render(request, 'doctor_profile.html' , context)


