from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm, PasswordResetForm
)

from django_recaptcha.fields import ReCaptchaField, ReCaptchaV3

from django.forms import (
    EmailField,
    EmailInput,
)
from accounts.models import User


class LoginForm(AuthenticationForm):

    captcha = ReCaptchaField(
    widget=ReCaptchaV3(
        attrs={
            'required_score':0.5
        },action="login"
    )
)


class CustomPasswordResetForm(PasswordResetForm):

    captcha = ReCaptchaField(
    widget=ReCaptchaV3(
        attrs={
            'required_score':0.7
        },action="login"
    )
    )


class UserRegisterForm(UserCreationForm):

    captcha = ReCaptchaField(
    widget=ReCaptchaV3(
        attrs={
            'required_score':0.7
        },action="register"
    )
)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
