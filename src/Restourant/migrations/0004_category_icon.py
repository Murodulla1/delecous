# Generated by Django 3.1.7 on 2021-03-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restourant', '0003_suggestions_recipe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]