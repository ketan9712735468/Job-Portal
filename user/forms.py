from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import Job, Profile
from django import forms
from django.forms import ModelForm

class UserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = "__all__"