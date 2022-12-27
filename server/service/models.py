from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse

class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Thumbnail(models.Model): 
    image = models.ImageField(upload_to='service/thumbnails/')
    def __str__(self):
        return f'{self.image.url}'


class Service(models.Model): 
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True, null=True)
    thumbnails = models.ManyToManyField(to=Thumbnail, blank=True)

    def get_absolute_url(self):
        return reverse("service:service-detail", kwargs={"pk": self.pk})
    


class FeedbackRequest(models.Model): 
    content = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)


class Settings(SingletonModel): 
    contact_number = models.TextField(blank=True)
    contact_number_wa = models.TextField(blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    
    class Meta:
        verbose_name_plural = 'settings'