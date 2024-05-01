# Generated by Django 5.0.4 on 2024-05-01 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productId', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=50)),
                ('productPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('productQuantity', models.IntegerField()),
            ],
        ),
    ]