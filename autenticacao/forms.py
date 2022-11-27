from django.contrib.auth.forms import AuthenticationForm
from django.forms import BooleanField


class CustomUserLoginForm(AuthenticationForm):
    remember = BooleanField(required=False)
