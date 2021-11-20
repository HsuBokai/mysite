from django import forms

class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)

class ContactForm2(forms.Form):
    subject = forms.CharField(max_length=200)
