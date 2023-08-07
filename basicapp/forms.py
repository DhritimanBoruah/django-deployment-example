from django import forms
from django.contrib.auth.models import User
from basicapp.models import UserProfileinfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileinfoForm(forms.ModelForm):      
    class Meta():
        model = UserProfileinfo
        fields = ('portfolio_site','profile_pic')