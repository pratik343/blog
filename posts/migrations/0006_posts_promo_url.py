# Generated by Django 3.0.7 on 2020-06-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200623_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='promo_url',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
