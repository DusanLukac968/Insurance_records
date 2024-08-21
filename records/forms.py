from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
    
class UserRegistrationForm(UserCreationForm):
    """
    form for creating new user(not admin)
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["name","surname", "age", "tel_number", "email",]

class LoginForm(forms.Form):
    """
    form for login user in to system 
    """
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ["email", 'password']


class UserUpdateForm(forms.ModelForm):
    """
    from for edititing user data by user himself
    """
    email = forms.EmailField()
    name = forms.CharField()
    surname = forms.CharField()
    age = forms.CharField(max_length=10)
    tel_number = forms.CharField(max_length=30)

    class Meta:
        model= User
        fields = ["email", "name", "surname", "age", "tel_number"]


class AddUserProductForm(forms.ModelForm):
    """
    form for adding and editing user insurance and its value 
    """
    class Meta:
        model = User
        fields = ['insurance', 'insurance_value']