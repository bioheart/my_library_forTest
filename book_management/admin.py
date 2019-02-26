from django.contrib import admin
from book_management.models import Category,Book
from django.db import models
# Register your models here.

# class BookAdmin(models.MOdel):
class BookAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    list_display = ('title','image_tag')
    #fields = ['image_tag']
    readonly_fields = ['image_tag']

admin.site.register(Category)
admin.site.register(Book,BookAdmin)
