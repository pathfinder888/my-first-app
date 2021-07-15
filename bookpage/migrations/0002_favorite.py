# Generated by Django 2.2.24 on 2021-07-02 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manga_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookpage.Manga')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookpage.User')),
            ],
        ),
    ]
