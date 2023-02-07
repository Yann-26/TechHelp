from django import forms
from django.contrib.auth import get_user_model



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    city = forms.CharField(max_length=100)
    country = forms.ChoiceField(choices=[])
    phone_number = forms.CharField(max_length=20)
    profile_photo = forms.ImageField()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'city', 'country', 'phone_number', 'profile_photo']