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
    image = models.ImageField('Görüntü', upload_to='service/thumbnails/')
    def __str__(self):
        return f'{self.image.url}'
    class Meta:
        verbose_name = 'Hizmet Görüntüsü'
        verbose_name_plural = 'Hizmet Görüntüleri'


class Service(models.Model): 
    title = models.CharField('Başlık', max_length=255)
    slug = AutoSlugField('Slug', populate_from='title', unique=True)
    content = models.TextField('İçerik')
    excerpt = models.TextField('Kısa İçerik', blank=True, null=True)
    thumbnails = models.ManyToManyField(verbose_name='Görüntüler', to=Thumbnail, blank=True)

    def get_absolute_url(self):
        return reverse("service:service-detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Hizmet'
        verbose_name_plural = 'Hizmetler'
    


class FeedbackRequest(models.Model): 
    content = models.TextField("Mesajınız", null=True, blank=True)
    name = models.CharField("İsim Soyisim *", max_length=255)
    email = models.EmailField("E-posta *")
    website = models.URLField("Websiteniz", null=True, blank=True)

    class Meta:
        verbose_name = 'Geri Dönüş Talebi'
        verbose_name_plural = 'Geri Dönüş Talepleri'


class Settings(SingletonModel): 
    contact_number = models.TextField('Telefon Numarası (0\'dan başlayan)', blank=True)
    contact_number_str = models.TextField('Telefon Numarası (Görsel İçerik)', blank=True)
    contact_number_wa = models.TextField('Telefon Numarası (Whatsapp 0\'dan başlayan)', blank=True)
    address = models.TextField('Adres', blank=True)
    email = models.EmailField('Kurumsal Eposta', blank=True)
    
    class Meta:
        verbose_name = 'Ayar'
        verbose_name_plural = 'Ayarlar'