# Generated by Django 4.1.4 on 2022-12-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_preorder_email_alter_preorder_text_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='preorder',
            name='order_id',
            field=models.TextField(null=True),
        ),
    ]
