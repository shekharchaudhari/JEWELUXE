from django import forms
from .models import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')