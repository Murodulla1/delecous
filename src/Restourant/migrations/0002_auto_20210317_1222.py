# Generated by Django 3.1.7 on 2021-03-17 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restourant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reyting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default=[], max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='recipes',
            name='reyting_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Restourant.reyting'),
        ),
    ]
