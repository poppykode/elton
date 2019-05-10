from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,ReadOnlyPasswordHashField
from .models import (
    User,
)

class ClientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','first_name','last_name','email',"password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_approve = False
        user.is_client = True
        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):
    password = None   
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )