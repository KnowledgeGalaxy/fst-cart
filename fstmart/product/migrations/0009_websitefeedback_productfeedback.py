# Generated by Django 4.2.6 on 2023-12-16 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_billdetails_delete_bill'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.TextField(blank=True)),
                ('rating', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='ProductFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(default=3)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
