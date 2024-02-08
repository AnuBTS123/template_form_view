from django import forms
from app.models import *

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'
