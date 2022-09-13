# Generated by Django 4.1 on 2022-09-06 16:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('size', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=200000)])),
                ('dev_date', models.DateField()),
                ('description', models.TextField()),
                ('min_system_requirements', models.TextField()),
                ('recommended_system_requirements', models.TextField()),
                ('downloads', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=0), django.core.validators.MaxValueValidator(limit_value=20000000)])),
                ('price', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=0), django.core.validators.MaxValueValidator(limit_value=10000)])),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Application', related_query_name='Applications', to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_time', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=0), django.core.validators.MaxValueValidator(limit_value=100000)])),
                ('last_launch', models.DateTimeField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Library', related_query_name='Libraries', to='games.application')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Library', related_query_name='Libraries', to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('CONSUMER_GRADE', 'Consumer grade'), ('INDUSTRIAL_GRADE', 'Industrial grade'), ('MIL_SPEC', 'Mil-spec'), ('RESTRICTED', 'Restricted'), ('CLASSIFIED', 'Classified'), ('COVERT', 'Covert')], max_length=30)),
                ('quality', models.CharField(choices=[('BATTLE_SCARRED', 'Battle-Scarred'), ('WELL_WORN', 'Well-Worn'), ('FIELD_TESTED', 'Field-Tested'), ('MINIMAL_WEAR', 'Minimal Wear'), ('FACTORY_NEW', 'Factory new')], max_length=40)),
                ('description', models.TextField()),
                ('is_sellable', models.BooleanField(default=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Item', related_query_name='Items', to='games.application')),
            ],
        ),
        migrations.CreateModel(
            name='GameComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('grade', models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MinValueValidator(limit_value=0), django.core.validators.MaxValueValidator(limit_value=5)])),
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='GameComment', related_query_name='GameComments', to='games.application')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='GameComment', related_query_name='GameComments', to='user.user')),
            ],
        ),
    ]