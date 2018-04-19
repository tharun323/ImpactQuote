from django import forms

from .models import Quote

class PostQuote(forms.ModelForm):
    class Meta:
        model=Quote
        fields=["quote","movie"]
