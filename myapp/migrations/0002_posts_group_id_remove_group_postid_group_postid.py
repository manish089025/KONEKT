# Generated by Django 4.1.2 on 2023-01-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='group_id',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='group',
            name='postId',
        ),
        migrations.AddField(
            model_name='group',
            name='postId',
            field=models.ManyToManyField(blank=True, null=True, to='myapp.posts'),
        ),
    ]
