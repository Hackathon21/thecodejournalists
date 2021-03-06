# Generated by Django 3.2.4 on 2021-06-22 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_text', models.TextField()),
                ('bias_score', models.FloatField()),
                ('bias_class', models.IntegerField()),
                ('quality_score', models.FloatField()),
                ('quality_class', models.IntegerField()),
                ('origin_url', models.TextField()),
                ('origin_source', models.TextField()),
            ],
        ),
    ]
