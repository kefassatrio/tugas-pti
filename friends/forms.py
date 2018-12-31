from django import forms
from . import models


class CreateFriends(forms.ModelForm):
    class Meta:
        model = models.Friends
        fields = ['name', 'slug', 'tempat_tanggal_lahir', 'description', 'line']

class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = [
            "text",
        ]
