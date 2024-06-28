from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)
from django.forms import (
    EmailField,
    EmailInput,
)
from accounts.models import User


# this is so you can log in with an email
class LoginForm(AuthenticationForm):
    username = EmailField(
        widget=EmailInput(attrs={"autofocus": True, "autocomplete": "email"})
    )


class UserRegisterForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
