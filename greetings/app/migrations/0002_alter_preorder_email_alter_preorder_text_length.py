# Generated by Django 4.1.4 on 2022-12-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preorder',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='preorder',
            name='text_length',
            field=models.TextField(null=True),
        ),
    ]