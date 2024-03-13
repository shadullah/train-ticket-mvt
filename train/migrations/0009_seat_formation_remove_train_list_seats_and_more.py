# Generated by Django 5.0 on 2024-03-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0008_alter_train_list_seats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat_formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='train_list',
            name='seats',
        ),
        migrations.AddField(
            model_name='train_list',
            name='seat_formation',
            field=models.ManyToManyField(to='train.seat_formation'),
        ),
    ]