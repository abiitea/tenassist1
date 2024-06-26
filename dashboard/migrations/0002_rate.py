# Generated by Django 4.2.1 on 2023-06-15 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0)),
                ('comments', models.CharField(blank=True, max_length=200, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.doctor')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.patient')),
            ],
        ),
    ]
