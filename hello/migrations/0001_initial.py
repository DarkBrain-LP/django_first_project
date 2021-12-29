# Generated by Django 4.0 on 2021-12-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name='Nom')),
                ('prenoms', models.CharField(max_length=255, verbose_name='Prénoms')),
                ('contact', models.CharField(blank=True, max_length=16, verbose_name='Contact')),
            ],
            options={
                'verbose_name': 'Étudiant',
                'verbose_name_plural': 'Étudiants',
                'db_table': 'hello_etudiant',
            },
        ),
    ]
