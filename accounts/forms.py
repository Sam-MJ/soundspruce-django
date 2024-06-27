from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    UserCreationForm,
)
from django.forms import (
    EmailField,
    EmailInput,
)
from accounts.models import User


class LoginForm(AuthenticationForm):
    username = EmailField(
        widget=EmailInput(attrs={"autofocus": True, "autocomplete": "email"})
    )


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
