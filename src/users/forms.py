from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    # first_name = forms.CharField(max_length=101)
    # last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username',  'email', 'password1', 'password2']