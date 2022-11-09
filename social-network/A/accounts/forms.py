from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# widget=forms.Textarea
class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=3, required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control w-25'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control w-25'}))
    password = forms.CharField(label='pass',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control w-25', 'placeholder': 'Your pass'}))
    password2 = forms.CharField(label='con pass',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control w-25', 'placeholder': 'Your pass'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('Exists username')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('Exists email')
        return email

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password')
        p2 = cd.get('password2')

        if p1 and p2 and p1 != p2:
            raise ValidationError('pass must match')


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control w-25'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control w-25', 'placeholder': 'Your pass'}))
