# Generated by Django 2.1.7 on 2019-07-07 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herald_bot', '0002_auto_20190707_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.IntegerField(blank=True, choices=[(0, 'Русский'), (1, 'English'), (2, '竜神の剣を喰らえ')], null=True, verbose_name='Язык'),
        ),
    ]
