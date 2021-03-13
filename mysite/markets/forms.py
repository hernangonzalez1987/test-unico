from django import forms
from .models import Market


class MarketCreate(forms.ModelForm):
    class Meta:
        model = Market
        fields = '__all__'