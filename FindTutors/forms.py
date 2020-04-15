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
from crispy_forms.helper import FormHelper

SUBJECT_CHOICES = (
    ('Computer Science', 'Computer Science'),
    ('Biology', 'Biology'),
    ('Chemistry', 'Chemistry'),
    ('Physics', 'Physics'),
    ('Math', 'Math'),
    ('English', 'English'),
    ('Algebra', 'Algebra'),
    ('Calculus', 'Calculus'),
    ('Geometry', 'Geometry'),
    ('Language', 'Language'),
    ('Reading', 'Reading'),
    ('Music', 'Music'),
)


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ('subject', 'description', 'location',)


class RegisterForm(UserCreationForm):
    class Meta:
        model = TUser
        fields = ('firstname', 'lastname', 'email', 'phone_number',)


class TutorUserSignUpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TutorUserSignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        profile = Profile.objects.get(pk=self.user.pk)
        # self.initial['firstname'] = profile.user_type

    class Meta:
        model = TUser  # change model to TutorProfile and add bio
        fields = ['username', 'firstname', 'lastname',
                  'email', 'phone_number', 'subjects', 'image']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'firstname': forms.TextInput(
                attrs={
                    'class': 'form-control',
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
            'subjects': forms.Select(
                choices=SUBJECT_CHOICES,
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
