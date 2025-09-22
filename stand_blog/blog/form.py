from django import forms


class ContactUsForm(forms.Form):    # Define a form class
    name = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    text = forms.CharField(max_length=10)
    