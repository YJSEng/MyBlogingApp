# Generated by Django 4.1.1 on 2024-09-19 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_comment_comment_blog_commen_created_0e6ed4_idx"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(default=2, upload_to="static/products/"),
            preserve_default=False,
        ),
    ]
