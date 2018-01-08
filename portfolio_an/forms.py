from django import forms

from portfolio_an.models import Contact
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'John',
                                                               'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Doe',
                                                               'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'john@doe.com',
                                                           'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('Schrijf hier jouw vraag'),
                                                           'class': 'form-control',
                                                           'rows': '5'}))
    class Meta:
        model = Contact
        fields = ("email", "first_name", "last_name", "message", "attachment",)
