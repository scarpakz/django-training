from django import forms
from django.contrib.auth.models import User

from .models import Book


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
