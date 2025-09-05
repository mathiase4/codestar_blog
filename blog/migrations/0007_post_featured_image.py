# blog/migrations/0007_post_featured_image.py
import cloudinary.models
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0006_drop_challenge_from_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(
                default='placeholder',
                max_length=255,
                verbose_name='image'
            ),
        ),
    ]
