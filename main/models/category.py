from django.db import models

from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class Category(models.Model):
    name =  RichTextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_children(self):
        return Category.objects.filter(parent=self)
