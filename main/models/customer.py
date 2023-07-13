
from django.db import models

from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.OneToOneField(User, related_name='customers')
    phone_number = models.CharField(max_length=14, unique=True)
    shop_name = models.CharField(max_length=90, unique=True)
    nid_number = models.IntegerField(max_length=20, unique=True)
    trea_liance = models.CharField(max_length=50, unique=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='customer/', null=True, blank=True)
    is_active = models.BooleanField(default=True)