# Generated by Django 3.2.8 on 2021-10-23 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0010_alter_item_relevance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='relevance',
            field=models.TextField(blank=True, default=None),
        ),
    ]