from django.contrib import admin
from django import forms
from .models import  Insurance, User,  UserManager
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Register your models here.

class UserCreationForms(forms.ModelForm):
    """
    creating new user 
    """
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email"]

    def save(self, commit= True):
        if self.is_valid():
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password"])
            if commit:
                user.save()
            return user

class UserChangeForm(forms.ModelForm):
    """
    changes in user profile
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "is_admin"]

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.Meta.fields.remove("password")            

class MyUserAdmin(UserAdmin):
    """
    allow to set user admin or take admin from user
    """
    form = UserChangeForm
    add_form = UserCreationForms

    list_display = ["email", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = (
        (None, {"fields": ["email", "password"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    )
    
    add_fieldsets = (
        (None, {
            "fields": ["email", "password"]
        }),
    )
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(Insurance)
admin.site.register(User, MyUserAdmin)
