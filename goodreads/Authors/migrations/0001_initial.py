# Generated by Django 2.0.2 on 2018-02-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author_Name', models.CharField(max_length=100)),
                ('Author_DoB', models.DateField(blank=True, null=True)),
                ('Author_Books', models.TextField(max_length=200)),
                ('Author_Bio', models.CharField(max_length=200)),
            ],
        ),
    ]
