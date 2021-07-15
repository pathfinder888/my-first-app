# Generated by Django 2.2.24 on 2021-06-25 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('tag', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField(blank=True)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('isbn', models.TextField(max_length=200)),
                ('manga_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookpage.Manga')),
            ],
        ),
    ]
