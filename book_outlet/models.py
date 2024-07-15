from typing import Iterable
from django.urls import reverse
from django.utils.text import slugify
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.city} {self.street}'
    
    class Meta :
        verbose_name_plural = 'Address Entries'



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, db_index=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name='books')
    is_bestselling = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.title} ({self.rating})'

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
