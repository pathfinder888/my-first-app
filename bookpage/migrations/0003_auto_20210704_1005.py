# Generated by Django 2.2.24 on 2021-07-04 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookpage', '0002_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='series',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='manga_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='manga_id', to='bookpage.Manga'),
        ),
    ]
