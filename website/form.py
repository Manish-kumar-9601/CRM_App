﻿ 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class SignUpForm(UserCreationForm):
    email=forms.EmailField( widget=forms.TextInput(attrs={'class':'form-control col-6' }))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' }))
    password1=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control' }))
    password2=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control' }))
    class Meta:
        model=User
        fields=('username','email','password1','password2')
        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'User Name'
            self.fields['username'].label = ''
            self.fields['username'].help_text =' <span class="form-text text-muted small">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span> '
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text ='<ul class="form-text text-muted small"><li>Your password cant be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password cant be a commonly used password.</li><li>Your password cant be entirely numeric.</li></ul>'
            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted small">Enter the same password as before, for verification.</span>'

# class AddRecordForm(forms.ModelForm):
