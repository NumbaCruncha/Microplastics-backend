from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from .models import Observation, FieldUser

class ObservationForm(ModelForm):
    model = Observation
    fields = ['datetime', 'field_user', 'sample_type']


class FieldUserModelForm(ModelForm):
    class Meta:
        model = FieldUser
        fields = ['fname', 'lname']

        def clean_fname(self):
            data = self.cleaned_data['fname']
            if data ==  'Parker':
                raise ValidationError(_('First Name too lame'))
            data = 'Bowie'
            return data

        
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)