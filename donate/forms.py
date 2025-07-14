from django import forms
from . models import *

class reg_form(forms.ModelForm):
    class Meta:
        model=user
        fields=['name','contact','address','location']

class log_form(forms.ModelForm):
    class Meta:
        model=login
        fields=['email','password']

class login_verify(forms.Form):
    email=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)

class user_edit_form(forms.ModelForm):
    class Meta:
        model=user
        fields=['name','contact','address','location']
        widget={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'})
        }

class log_edit_form(forms.ModelForm):
    class Meta:
        model=login
        fields=['email']
        widget={
            'email':forms.TextInput(attrs={'class':'form-control'})
        }

class donation_form(forms.ModelForm):
    class Meta:
        model=donations
        fields=['food_name','quantity']
        widget={
            'food_name':forms.TextInput(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'})
        }