import random

from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class DateTimeField(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Notes(DateTimeField):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    content = models.TextField()
    pictures = models.ManyToManyField("Picture", blank=True)
    url = models.SlugField(max_length=300, unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title) + str(random.randint(0, 1000))
        return super(Notes, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('note_detail', kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        ordering = ['-updated_at']

    def __str__(self):
        return self.title

class Picture(DateTimeField):
    image = models.ImageField(upload_to="pictures/")

    class Meta:
        verbose_name = "Picture"
        verbose_name_plural = "Pictures"
        ordering = ['-created_at']