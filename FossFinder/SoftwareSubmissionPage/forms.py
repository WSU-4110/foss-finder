from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class SubmitSoftwareForm(forms.Form):

    Name = forms.CharField(
        max_length=25,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Software Name"
            }
        )
    )
    
    Description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Software Discription"
            }
        )
    )

    TAGS = [
        ('Operating System', 'Operating System'),
        ('Office Suite', 'Office Suite'),
        ('Web Browser', 'Web Browser'),
        ('Graphics Editor', 'Graphics Editor'),
        ('Programming Language', 'Programming Language'),
    ]
    Type = forms.ChoiceField(
        choices = TAGS
    )

    Similar = forms.CharField(
        max_length=25,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Software like this"
            }
        )
    )

    OS = forms.CharField(
        max_length=25,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Operating System"
            }
        )
    )

    Thumbnail = forms.CharField(
        max_length=25,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Image URL"
            }
        )
    )
