from django import forms
from .models import Facilities


class FacilityCreateForm(forms.ModelForm):
    class Meta:
        model = Facilities
        fields = (
            'laboratory_name',
            'facility',
            'address',
            'city',
            'state',
            'country',
            'zip_code',
            'type',
            'link',
            'poc_email',
            'poc_phone'
        )


class FacilityUpdateForm(forms.ModelForm):
    class Meta:
        model = Facilities
        fields = (
            'laboratory_name',
            'facility',
            'address',
            'city',
            'state',
            'country',
            'zip_code',
            'type',
            'link',
            'poc_email',
            'poc_phone'
        )
