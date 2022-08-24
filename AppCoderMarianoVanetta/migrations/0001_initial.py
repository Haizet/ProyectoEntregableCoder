# Generated by Django 4.1 on 2022-08-23 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('fecha_nac', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Hijo',
            fields=[
                ('familiar_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AppCoderMarianoVanetta.familiar')),
                ('es_hijo', models.BooleanField()),
            ],
            bases=('AppCoderMarianoVanetta.familiar',),
        ),
        migrations.CreateModel(
            name='Padres',
            fields=[
                ('familiar_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AppCoderMarianoVanetta.familiar')),
                ('es_padre', models.BooleanField()),
            ],
            bases=('AppCoderMarianoVanetta.familiar',),
        ),
    ]
