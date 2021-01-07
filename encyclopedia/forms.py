from django import forms
from .models import New_Entry
from . import util

class New_Entry_Form(forms.ModelForm):
    class Meta:
        model = New_Entry
        fields = ['title', 'content']


    def clean_title(self):
        title_clean = self.cleaned_data.get("title")
        entry_list = util.list_entries()
        if title_clean in entry_list:
            raise forms.ValidationError("Error title is already in use")
        return title_clean

class Edit_form(forms.Form):
    content = forms.CharField(widget=forms.Textarea)