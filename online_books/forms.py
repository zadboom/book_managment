from django import forms
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# 📚 فرم کتاب
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'publish_date', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded-md focus:ring-2 focus:ring-blue-400'
            }),
            'author': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded-md focus:ring-2 focus:ring-blue-400'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full p-2 border rounded-md focus:ring-2 focus:ring-blue-400'
            }),
            'publish_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full p-2 border rounded-md focus:ring-2 focus:ring-blue-400'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-2 border rounded-md focus:ring-2 focus:ring-blue-400'
            }),
        }


# 👤 فرم ثبت‌نام با Tailwind
class CustomSignupForm(UserCreationForm):
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(attrs={
            'class': 'w-full p-2 border rounded-md focus:ring-2 focus:ring-green-400'
        })
    )
    email = forms.EmailField(
        label="ایمیل",
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'w-full p-2 border rounded-md focus:ring-2 focus:ring-green-400'
        })
    )
    password1 = forms.CharField(
        label="کلمه عبور",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-2 border rounded-md focus:ring-2 focus:ring-green-400'
        })
    )
    password2 = forms.CharField(
        label="تأیید کلمه عبور",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-2 border rounded-md focus:ring-2 focus:ring-green-400'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# 🔑 فرم ورود با Tailwind
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(attrs={
            'class': 'w-full p-2 border rounded-md focus:ring-2 focus:ring-indigo-400'
        })
    )
    password = forms.CharField(
        label="کلمه عبور",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-2 border rounded-md focus:ring-2 focus:ring-indigo-400'
        })
    )
