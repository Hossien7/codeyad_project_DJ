from django import forms
from django.core.validators import ValidationError
from blog.models import Message

class ContactUsForm(forms.Form):    # Define a form class
    name = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    text = forms.CharField(max_length=10, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Text'}))
    

    def clean(self):    # Custom validation logic
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('Name and Text cannot be the same.', code='invalid')
        
    def clean_name(self):    # Field-specific validation
        name = self.cleaned_data.get('name')
        if 'a' in name:
            raise ValidationError('A is in text', code='invalid')
        return name
    

class MessageForm(forms.ModelForm): 
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'enter your title'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter your text'
            })
        }