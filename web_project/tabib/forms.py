from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Login_Form(forms.ModelForm):
    #required = False
    username= forms.CharField(max_length=30 , label="Username")
    password= forms.CharField(max_length=50 , label="Password" , widget=forms.PasswordInput())
    class Meta:
       model = User
       fields = ('username' , 'password')

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label="Username")
    first_name = forms.CharField(label="First name")
    second_name = forms.CharField(label="Second_name")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password1" , widget=forms.PasswordInput() , min_length=8)
    password2 = forms.CharField(label="Password2" , widget=forms.PasswordInput() , min_length=8)
    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'second_name' , 'email', 'password1', 'password2')

    def clean_password2(self):
      cd = self.cleaned_data
      if cd ['password1'] != cd ['password2']:
        raise forms.ValidationError('password match , try agin!')
      return cd ['password2']
    
    def clean_username(self):
      cd = self.cleaned_data
      if User.objects.filter(username=cd['username']).exists():
        raise forms.ValidationError('this username has already exists try again with another one')
      return cd ['username']


class Update_Profile(forms.ModelForm):
    first_name = forms.CharField(label="First name")
    second_name = forms.CharField(label="Second name ")
    email = forms.EmailField(label="Email")
    class Meta:
        model = User
        fields = ('first_name' , 'second_name' , 'email')
