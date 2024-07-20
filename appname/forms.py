from django import forms
from .models import ContactForm


class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'phone', 'mc_number', 'query', 'contact_method']

from .models import Reach

class ReachModelForm(forms.ModelForm):
    class Meta:
        model = Reach
        fields = ['name', 'email', 'comment']