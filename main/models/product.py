from datetime import datetime
from django.db import models
from django.utils import timezone


from main.models.subcategory import SubCategory
class Product(models.Model):
    title = models.CharField(max_length=150)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE, blank=True, null=True, related_name='subcategory')
    short_description = models.TextField(max_length=100)
    price = models.FloatField(default=0)
    is_active = models.BooleanField(default=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def get_all_images(self) :
         image_val = Image.objects.filter(product=self)
         return image_val
    
    def get_all_variants(self) :
         attr_val = Variant.objects.filter(product=self)
         return attr_val

class Image(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True
        )
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.product.title


class Variant(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
        )
    size = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.product.title
    




class Order(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    code = models.CharField(max_length=100, blank=True, null=True)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    status=models.CharField(max_length=50,null=True,choices=STATUS, default='Pending')
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.code
    

    def get_order_items(self) :
         items_val = OrderItems.objects.filter(order_id=self)
         return items_val

class OrderItems(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)