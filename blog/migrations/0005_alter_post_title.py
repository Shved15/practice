# Generated by Django 4.1.7 on 2023-02-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_slug_alter_post_content_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(db_index=True, help_text='no more than 200 characters', max_length=200),
        ),
    ]
