# Generated by Django 4.2 on 2023-05-09 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_order_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Order Confirmed', 'Order Confirmed'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], default='Pending', max_length=50, null=True),
        ),
    ]
