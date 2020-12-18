"""Users Forms"""

#Django
from django import forms

#Models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """signup form"""
    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(min_length=6, max_length=70, widget= forms.PasswordInput())
    password_confirmation = forms.CharField(min_length=6, max_length=70, widget= forms.PasswordInput())

    first_name = forms.CharField(min_length=2, max_length=20)
    last_name = forms.CharField(min_length=2, max_length=20)

    email = forms.CharField(min_length=6, max_length=70, widget= forms.EmailInput())

    def clean_username(self):
        """username must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username = username).exists()

        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """verify password confirmation match"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password do not match')
        return data

    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user = user)
        profile.save()

class ProfileForm(forms.ModelForm):
    
    website = forms.URLField(max_length = 200, required = False)
    biography = forms.CharField(max_length = 500, required = False)
    phone_number = forms.CharField(max_length = 20, required = True)
    picture = forms.ImageField(required = True)

    class Meta:
        model = Profile
        fields = ['website', 'biography', 'phone_number', 'picture']
