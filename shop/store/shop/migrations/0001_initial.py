# Generated by Django 4.2.13 on 2024-08-16 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.FloatField()),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='products/')),
                ('color', models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('yellow', 'Yellow'), ('black', 'Black'), ('white', 'White')], max_length=10)),
                ('rating', models.FloatField()),
                ('cell_count', models.PositiveSmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('discount', models.PositiveSmallIntegerField(default=0)),
                ('stock', models.PositiveSmallIntegerField(default=0)),
                ('aviable', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_products', to='shop.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_products', to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('value', models.PositiveSmallIntegerField(default=0)),
                ('name', models.CharField(max_length=250)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_ratings', to='shop.product')),
            ],
        ),
    ]
