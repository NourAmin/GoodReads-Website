# Generated by Django 2.0.2 on 2018-02-19 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authors', '0002_remove_authors_author_books'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Users', '0003_auto_20180215_0421'),
    ]

    operations = [
        migrations.CreateModel(
            name='followList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authors.Authors')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]