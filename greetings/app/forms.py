from django import forms
from .models import PreOrder

class MyForm(forms.ModelForm):
  class Meta:
    model = PreOrder
    fields = ["email", "name",]
    labels = {'email': "E-Mail-Adresse", "name": "Vor- und Nachname",}