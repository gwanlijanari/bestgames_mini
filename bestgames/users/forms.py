from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username"]

    def save(self, commit=True):

        user = super().save(commit=False)
        if commit:
            user.save()
            if hasattr(user, "student"):
                user.student.save()

        return user
