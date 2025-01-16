from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']




from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
