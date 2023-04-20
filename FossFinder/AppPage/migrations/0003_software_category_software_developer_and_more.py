# Generated by Django 4.1.7 on 2023-04-20 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPage', '0002_alter_software_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='category',
            field=models.CharField(default='Other', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='software',
            name='developer',
            field=models.CharField(default='nothing', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='software',
            name='download_link',
            field=models.URLField(default='Other'),
            preserve_default=False,
        ),
    ]
