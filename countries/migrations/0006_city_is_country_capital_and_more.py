# Generated by Django 4.0.3 on 2022-03-21 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_alter_city_country_alter_transcontinental_continent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='is_country_capital',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transcontinental',
            name='main_continent',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='CapitalCity',
        ),
    ]
