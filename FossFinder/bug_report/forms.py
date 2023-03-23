from django import forms
from .models import SubmittedBugs


class SubmitBugsForm(forms.ModelForm):
    class Meta:
        model = SubmittedBugs
        fields = ["title", "description", "image",]
        labels = {'name': "name", 'description': "description", 'image': "image",}
