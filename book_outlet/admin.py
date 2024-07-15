from django.contrib import admin
from .models import Book, Author, Address
# Register your models here.


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['city', 'street', 'postal_code']
    
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'rating', 'is_bestselling']
    list_filter = ['author', 'rating', 'is_bestselling']
    prepopulated_fields = {'slug': ('title',)}
