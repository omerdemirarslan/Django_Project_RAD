from django import forms

from developers.models import DeveloperUsers


class RegistrationForm(forms.Form):
    """
    This Class Create Register Form For The Registration Process
    """
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    mail_address = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Mail Address'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )
    github_address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Github Address'})
    )
    linkedin_address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Linkedin Address'})
    )
    twitter_address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Twitter Address'})
    )

    class Meta:
        model = DeveloperUsers
        fields = [
            "first_name", "last_name", "mail_address", "password", "confirm_password", "github_address",
            "linkedin_address", "twitter_address"
        ]


class LoginForm(forms.Form):
    """
    This Class Create Login Form For User Authentication
    """
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
