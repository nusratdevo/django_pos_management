from django import forms
from django.forms import TextInput, Select, FileInput, CheckboxInput, NumberInput
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from main.models.customer import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control',  'placeholder': 'category name','id': 'name'}),
            'phone_number': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone No.'}),
            'profile_picture': FileInput(attrs={'class': 'form-control', 'id': 'imageUpload'}),
            'shop_name': TextInput(attrs={'class': 'form-control',  'placeholder': 'shop name'}),
            'nid_number': NumberInput(attrs={'class': 'form-control', 'placeholder': 'nid number.'}),
            'trea_liance': TextInput(attrs={'class': 'form-control',  'placeholder': 'trea_liance name'}),
            'address': TextInput(attrs=CKEditorUploadingWidget()),

            'is_active': CheckboxInput(attrs={'class': 'checkbox', 'id': 'activity'})
        }