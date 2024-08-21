from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import  Insurance
from .forms import  UserRegistrationForm, LoginForm, UserUpdateForm, AddUserProductForm

# Create your views here.

class MainPage(generic.ListView):
    """
    view of main page with list of available insurances
    """
    template_name = "records/main_page.html"
    context_object_name = "main_page"

    def get_queryset(self):
        return Insurance.objects.all().order_by("-id")

class InsuranceDetail(generic.DetailView):
    """
    view for each one insurance with detailed description
    """

    model= Insurance
    template_name = "records/insurance_details.html"
    
    def get(self, request, pk):
        try:
            insurance = self.get_object()
        except:
            return redirect("main_page")
        return render(request, self.template_name, {"insurance": insurance})

class UserViewLogin(generic.edit.CreateView):
    """
    view for user login 
    """
    form_class = LoginForm
    template_name = 'records/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password= password)
            if user:
                login(request, user)
                return redirect("main_page")
        return render(request, self.template_name, {"form": form})
    

def register(request):
    """
    view for user registraion formular
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}')
            return redirect('main_page')
    else:
        form = UserRegistrationForm()
    return render(request, 'records/register.html', {'form': form}) 

def logout_user(request):
    """
    allows user to logout and log in new one account or registration new user 
    """
    logout(request)
    return redirect("login")

@login_required
def profile(request):  
    """
    view that shows account details, only logged user
    """ 
    user =  get_user_model()  
    if user:
        return render(request, 'records/profile.html')
    return redirect("main_page")

@login_required
def user_update(request):
    """
    allows logged user to update/change his profile 
    """
    if request.method == 'POST':
        user = get_user_model()
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'{user_form}, Your profile has been updated!')
            return redirect('profile')
        
        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model()
    if user:
        form = UserUpdateForm(instance=request.user)
        return render(request, 'records/user_update.html', {'form':form})

    return redirect("")   

@login_required
def products_user(request):
    """
    view that allows  logged user to  change his insurance and its value
    """
    if request.method == 'POST':
        user = get_user_model()
        form = AddUserProductForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your products has been updated!')
            return redirect('profile')
        
        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model()
    if user:
        form = AddUserProductForm(instance=request.user)
        return render(request, 'records/user_update.html', {'form':form})

    return redirect("")   
