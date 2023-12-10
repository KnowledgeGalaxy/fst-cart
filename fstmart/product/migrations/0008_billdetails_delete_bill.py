# Generated by Django 4.2.6 on 2023-12-01 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_bill'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.customer')),
                ('ordered_items', models.ManyToManyField(blank=True, related_name='bills', to='product.ordereditems')),
            ],
        ),
        migrations.DeleteModel(
            name='Bill',
        ),
    ]