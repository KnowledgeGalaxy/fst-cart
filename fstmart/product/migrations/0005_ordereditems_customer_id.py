# Generated by Django 4.2.6 on 2023-11-30 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_confirmorder_ordereditems_delete_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordereditems',
            name='customer_id',
            field=models.ForeignKey(default='9999999999', on_delete=django.db.models.deletion.CASCADE, to='product.customer'),
        ),
    ]
