from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    email = forms.EmailField(label='Your email',max_length=100,widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Subscriber
        fields = ['email']
