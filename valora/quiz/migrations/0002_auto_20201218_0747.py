# Generated by Django 3.1.4 on 2020-12-18 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='answer1',
            new_name='answer_A',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='answer2',
            new_name='answer_B',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='answer3',
            new_name='answer_C',
        ),
    ]