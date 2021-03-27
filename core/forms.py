from django import forms
from .models import ContactMe
class ContactMeForm(forms.ModelForm):

    class Meta:
        model = ContactMe
        #specify reqired feilds         
        fields = ('name', 'mail','phone_num','message')
