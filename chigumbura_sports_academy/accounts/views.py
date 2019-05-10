from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import auth
from django.contrib import messages
from .forms import (
    ClientSignUpForm,EditProfileForm,
)
from .models import (
    User,
)
#  and user.is_active

# Create your views here.
def login_view(request):
    template_name='accounts/login.html'
    return render(request,template_name)

def login(request):
    template_name='accounts/login.html'
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if not user.is_active:         
            messages.success(request, 'Your application is still beign processed, for further info please contact admin.') 
            return  redirect(reverse('corporate:home'))
        if not user.is_approve:
            messages.success(request, 'Your application is still beign processed for further info please contact admin.') 
            return  redirect(reverse('corporate:home'))
        auth.login(request, user)
        messages.success(request, 'user successfully logged in.') 
        return  redirect(reverse('accounts:view_profile'))  
    else:
        messages.error(request, 'Invalid username or password.') 
        return render(request,template_name) 


def register(request):
    if request.method =='POST':
        form = ClientSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application send to admin, an email will be sent to you upton account activation.') 
            return redirect(reverse('accounts:login_view'))
    else:
        form = ClientSignUpForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated.')
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Paasword changed.') 
            return redirect(reverse('accounts:view_profile'))
        else:
            messages.error(request, 'something went wrong.') 
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('accounts:view_profile')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'accounts/change_password.html', {
#         'form': form
#     })

