# Generated by Django 4.2.1 on 2023-06-22 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_medicalhistory_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicalhistory',
            options={'ordering': ('date',), 'verbose_name_plural': 'MedicalHistories'},
        ),
        migrations.AlterModelOptions(
            name='prescription',
            options={'ordering': ('date',)},
        ),
        migrations.AlterModelOptions(
            name='rate',
            options={'ordering': ('date',)},
        ),
    ]
