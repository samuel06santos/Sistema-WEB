# Generated by Django 4.1.3 on 2022-12-08 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_usuario_email_alter_usuario_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
