from django import forms
from django.forms import inlineformset_factory
from django.forms import TextInput, Select, FileInput, CheckboxInput

from main.models.product import (
    Product, Image, Variant
)
from main.models.subcategory import SubCategory


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'product title',}),
            'subcategory': Select(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'short_description',}),
            'price': forms.TextInput(attrs={'class': 'form-control','placeholder': 'product price',}),

        }


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = '__all__'


class VariantForm(forms.ModelForm):

    class Meta:
        model = Variant
        fields = '__all__'
        widgets = {
            'size': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'size'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control',  'placeholder':'Qty'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'price'}),
        }


VariantFormSet = inlineformset_factory(
    Product, Variant, form=VariantForm,
    extra=1, can_delete=True, can_delete_extra=True
)
ImageFormSet = inlineformset_factory(
    Product, Image, form=ImageForm,
    extra=1, can_delete=True, can_delete_extra=True
)