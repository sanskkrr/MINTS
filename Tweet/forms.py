from django import forms
from .models import Tweet
from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ['text', 'photo']

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'w-full bg-white/10 border border-white/20 rounded-xl p-4 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'rows': 4,
                'placeholder': 'Share something...'
            }),

            'photo': forms.ClearableFileInput(attrs={
                'class': 'w-full text-gray-300'
            }),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full p-3 rounded-xl bg-white/10 border border-white/20 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500'
            })