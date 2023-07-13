from django import forms
from django.forms import TextInput, Select, FileInput, CheckboxInput
from main.models.subcategory import SubCategory
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control',  'placeholder': 'category name','id': 'name'}),
            'category': Select(attrs={'class': 'form-control'}),
            'subcategory_image': FileInput(attrs={'class': 'form-control', 'id': 'imageUpload'}),
            'is_active': CheckboxInput(attrs={'class': 'checkbox', 'id': 'activity'})
            # 'multiselect': SelectMultiple(attrs={'class': 'form-control select2', 'id': 'tags', 'multiple': 'multiple'}),

        }
