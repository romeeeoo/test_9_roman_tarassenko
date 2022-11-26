from django.contrib.auth import get_user_model
from django.db import models

from gallery.managers import PictureManager


# Create your models here.
class Picture(models.Model):
    image = models.ImageField(
        verbose_name="Image",
        null=False,
        blank=False
    )
    author = models.ForeignKey(
        verbose_name="author",
        to=get_user_model(),
        related_name="pictures",
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    description = models.CharField(
        verbose_name="description",
        null=False,
        blank=False,
        max_length=200
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    favored_by = models.ManyToManyField(
        to=get_user_model(),
        related_name="favorite_pictures",
        blank=True
    )
    object = PictureManager()
