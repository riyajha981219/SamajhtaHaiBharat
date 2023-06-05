from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django import forms

from .models import *


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)

class MemberForm(ModelForm):
    
    class Meta :
        model = Member
        fields = ("nickname", "profilepic", "bio",)
        labels={
            'nickname':'',
            'profilepic':'',
            'bio':''
        }
        widgets = {
            'nickname': forms.TextInput()
        }