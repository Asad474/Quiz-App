# Generated by Django 4.1.5 on 2023-06-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_remove_quizquestion_topic_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(default='captain-america.jpg', null=True, upload_to='images/', verbose_name='Profile pic'),
        ),
    ]