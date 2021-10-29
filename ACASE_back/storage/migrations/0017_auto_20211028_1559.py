# Generated by Django 3.2.8 on 2021-10-28 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0016_auto_20211027_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='created_at',
            new_name='Created_at',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='finding',
            new_name='Finding',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='languaje',
            new_name='Languaje',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='learning',
            new_name='Learning',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='pages',
            new_name='Pages',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='relevance',
            new_name='Relevance',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='source_url',
            new_name='Source_url',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='text',
            new_name='Text',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='title',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='updated_at',
            new_name='Updated_at',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='url',
            new_name='Url',
        ),
        migrations.RenameField(
            model_name='keyword',
            old_name='items',
            new_name='Items',
        ),
        migrations.RenameField(
            model_name='keyword',
            old_name='word',
            new_name='Word',
        ),
        migrations.RenameField(
            model_name='target',
            old_name='base_url',
            new_name='Base_url',
        ),
        migrations.RenameField(
            model_name='target',
            old_name='name',
            new_name='Name',
        ),
    ]