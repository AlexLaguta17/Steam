# Generated by Django 4.1 on 2022-09-06 16:45

from django.db import migrations, models
import user.services.validators.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('login', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('ver_email', models.BooleanField(default=False)),
                ('phone_number', models.CharField(max_length=14, validators=[user.services.validators.validators.validate_phone_number])),
                ('ver_phone', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
