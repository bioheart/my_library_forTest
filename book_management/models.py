import os
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=255)
    pulish_date = models.DateField('date publish')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bookImage = models.ImageField(blank=True,upload_to = 'book_image')



    # def url(self):
    #     # returns a URL for either internal stored or external image url
    #     if self.externalURL:
    #         return self.externalURL
    #     else:
    #         # is this the best way to do this??
    #         return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.image)))

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="120" height="120" />' % (self.bookImage))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __unicode__(self):
        # add __str__() if using Python 3.x
        return self.title

    def __str__(self):
        return self.title