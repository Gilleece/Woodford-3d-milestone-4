from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """
    Contact Us form
    """
    class Meta:
        model = Contact
        fields = ['email', 'subject', 'message']
