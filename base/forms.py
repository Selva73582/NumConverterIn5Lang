from django import forms

class NumberForm(forms.Form):
    inputInteger=forms.CharField(label="Enter a number")