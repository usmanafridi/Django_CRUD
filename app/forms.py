from django import forms
from django.forms import fields

from .models import Mobile, Booking


class MobileForm(forms.ModelForm):

    class Meta:
        model = Mobile
        fields = [
            'name',
            'company',
            'price',
            'color',
            'is_new',
            'features',
        ]


class HotelForm(forms.ModelForm):
    class Meta:
        model= Booking
        fields= '__all__'

        


