from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'phone_num', 'job')


