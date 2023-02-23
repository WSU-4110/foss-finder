from django import forms
from .models import SubmittedSoftware


class SubmitSoftwareForm(forms.ModelForm):
    class Meta:
        model = SubmittedSoftware
        fields = ["name", "developer", "description", "tag_WordProcesser", "tag_SpreadSheet", "tag_GraphicsEditor", "tag_AudioEditor", "tag_Communication", 
            "tag_Multimedia", "tag_AntiVirus", "tag_CodeEditor", "tag_DiskBurner", "tag_FileShare", "tag_Other", "os_WIN", "os_MAC", "os_NIX", "image",]

        labels = {'name': "name", 'developer': "developer", 'description': "description", 'Word Processer': "tag_WordProcesser", 
            'Spreadsheet Editor': "tag_SpreadSheet", 'Graphics Editor': "tag_GraphicsEditor", 'Audio Editor': "tag_AudioEditor", 
            'Communication': "tag_Communication", 'Multimedia': "tag_Multimedia", 'AntiVirus': "tag_AntiVirus", 'Code Editor': "tag_CodeEditor", 
            'Disk Burner': "tag_DiskBurner", 'File Sharing': "tag_FileShare", 'Other': "tag_Other", 'Windows': "os_WIN", 
            'Mac OS X': "os_MAC", 'Linux': "os_NIX", 'image': "image",}
