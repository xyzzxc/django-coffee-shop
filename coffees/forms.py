from django import forms

from coffees.models import Coffee


class CoffeeForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Coffee