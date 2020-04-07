# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# # from .models import  BigUser, Request, TUser
# from .models import TUser, Request, Profile, Reviews
# from django.forms import ModelForm
# from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import TUser, Profile, Request, Reviews
from django.forms import ModelForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms import bootstrap
from django.utils.translation import gettext_lazy as _
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ('subject', 'description', 'location',)


class RegisterForm(UserCreationForm):
    class Meta:
        model = TUser
        fields = ('firstname', 'lastname', 'email', 'phone_number',)


class TutorUserSignUpForm(forms.ModelForm):
    class Meta:
        model = TUser  # change model to TutorProfile and add bio
        fields = ['username', 'firstname', 'lastname',
                  'email', 'phone_number', 'subjects', 'image']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'firstname': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'lastname': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'phone_number': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'subjects': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class TuteeUserSignUpForm(UserCreationForm):
    class Meta:
        model = TUser
        fields = ('firstname', 'lastname', 'email',
                  'phone_number', 'year', 'subjects')


# TutorRegistrationForm
class TutorRegistration(UserCreationForm):
    class Meta:
        model = TUser
        fields = ('firstname', 'lastname', 'phone_number', 'subjects')


# update user profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'year', 'user_type', 'subjects', 'bio']


class ReviewRatingForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['profile', 'rating', 'reviews']
