# Generated by Django 4.1.7 on 2023-05-25 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
        ('feed', '0002_rename_user_post_user2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_related', to='post.publicacao'),
        ),
    ]
