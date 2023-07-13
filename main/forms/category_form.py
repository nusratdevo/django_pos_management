from django import forms
from django.forms import TextInput, Select, FileInput, CheckboxInput
from main.models.category import Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.fields import RichTextField


class CategoryForm(forms.ModelForm):
    # name = forms.CharField(widget=CKEditorUploadingWidget())
    # name = RichTextField()

    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            # 'name': CKEditorUploadingWidget(),
            'name': TextInput(attrs={'class': 'form-control',  'placeholder': 'category name','id': 'name'}),

            'is_active': CheckboxInput(attrs={'class': 'checkbox', 'id': 'activity'})
        }
