# Generated by Django 4.2.3 on 2023-08-02 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0005_newspaper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaper',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]