# Generated by Django 3.2.8 on 2021-10-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0008_auto_20211022_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='languaje',
            field=models.CharField(blank=True, choices=[('ESP', 'ESP'), ('ENG', 'ENG'), ('OTHER', 'OTHER')], default='OTHER', max_length=6),
        ),
    ]
