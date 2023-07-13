from django.db import models
from main.models.category import Category
from ckeditor_uploader.fields import RichTextUploadingField


class SubCategory(models.Model):
    name = models.CharField(max_length=90, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, related_name='subcategory')
    subcategory_image = models.ImageField(upload_to='subcategory/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
#  body = RichTextUploadingField(config_name='LeftFields', blank=True, null=True)


    def __str__(self):
        return self.name

    def get_children(self):
        return SubCategory.objects.filter(category=Category)
