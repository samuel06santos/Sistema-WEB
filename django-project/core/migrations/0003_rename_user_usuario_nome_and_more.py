# Generated by Django 4.1.3 on 2022-12-08 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usuario_email_usuario_first_name_usuario_last_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='user',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='first_name',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
    ]
