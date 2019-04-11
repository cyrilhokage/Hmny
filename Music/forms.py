from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Playlist, Track

#Login Form
class Login_form(forms.Form):
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input-1', 'placeholder':'username'}))
	password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class':'input-2', 'placeholder':'password'}))


#Sign Up Form
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Playlist_Form(forms.ModelForm):
	class Meta:
		model = Playlist
		exclude = ('id', 'user')

class Track_Form(forms.ModelForm):
	class Meta:
		model = Track
		fields = ('track_title', 'playlist', 'stream_source')