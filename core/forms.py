from django import forms

from .models import ContactMe
class ContactMeForm(forms.ModelForm):

    class Meta:
        model = ContactMe
        fields = ('name', 'mail','phone_num','message')