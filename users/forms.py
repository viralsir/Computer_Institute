from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Div
#from .models import profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=(forms.TextInput(attrs={'placeholder':'Email'})))
    username= forms.CharField(widget=(forms.TextInput(attrs={'placeholder':'Username'})))
    password1 = forms.CharField(widget=forms.PasswordInput({'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput({'placeholder': ' Retype Password'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.layout=Layout(
            Div('username',css_class='input-group mb-3')
        )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = profile
#         fields = ['image']
