# Generated by Django 4.0.4 on 2022-05-31 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='MrcData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
    ]
