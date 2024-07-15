from typing import Iterable
from django.urls import reverse
from django.utils.text import slugify
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, db_index=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(max_length=100, null=True)
    is_bestselling = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.title} ({self.rating})'
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
