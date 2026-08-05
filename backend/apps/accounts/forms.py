from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter your email",
            }
        ),
    )

    first_name = forms.CharField(
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your first name",
            }
        ),
    )

    last_name = forms.CharField(
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your last name",
            }
        ),
    )

    class Meta:
        model = User

        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = User

        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_photo",
        )

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Username",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "First name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Last name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email",
                }
            ),
            "profile_photo": forms.ClearableFileInput(
                attrs={
                    "accept": "image/*",
                }
            ),
        }

