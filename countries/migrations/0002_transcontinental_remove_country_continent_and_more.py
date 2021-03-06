# Generated by Django 4.0.3 on 2022-03-21 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransContinental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='country',
            name='continent',
        ),
        migrations.AddField(
            model_name='continent',
            name='continent',
            field=models.ManyToManyField(through='countries.TransContinental', to='countries.country'),
        ),
        migrations.AddField(
            model_name='transcontinental',
            name='continent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='countries.continent'),
        ),
        migrations.AddField(
            model_name='transcontinental',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='countries.country'),
        ),
    ]
