# Generated by Django 5.0 on 2024-03-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0005_train_list_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='train_list',
            name='seat_layout',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]