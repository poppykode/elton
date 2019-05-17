# Generated by Django 2.2.1 on 2019-05-14 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dependencies', '0004_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dependent',
            options={'ordering': ['-timestamp'], 'verbose_name_plural': 'Dependencies(students)'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-timestamp'], 'verbose_name_plural': 'Dependencies Videos'},
        ),
        migrations.RenameField(
            model_name='video',
            old_name='dep',
            new_name='dependent',
        ),
    ]