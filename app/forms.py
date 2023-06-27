from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    importance = forms.ChoiceField(widget=forms.Select(attrs={'style': 'width: 50%;', 'class': 'form-control'}), choices = (("0", "No"),("1", "Little important"),("2", "Important"),("3", "Very important"),))

    class Meta:
        model = Notes
        fields = ['title', 'content', 'importance']