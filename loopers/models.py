from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


#service and subservice models----------------------------------------------
class Service(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='service/%Y/%m', blank=True)
    home_icon = models.ImageField(upload_to='service_icon/%Y/%m', blank=True)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']
        indexes = [models.Index(fields=['order'])]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('sub_service', args=[self.slug])


class ServiceOffer(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='offers')
    offer = models.CharField(max_length=250)
    order = models.PositiveIntegerField(default=1)
    class Meta:
        ordering = ['order']
        indexes = [models.Index(fields=['order'])]

    def __str__(self):
        return self.offer

class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='subservices')
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, help_text='if does not fill automatically, leave blank')
    description = models.TextField()
    image = models.ImageField(upload_to='service/%Y/%m', blank=True)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']
        indexes = [models.Index(fields=['order'])]

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Review(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=250, blank=True)
    image = models.ImageField(blank=True,upload_to='review/%Y/%m' )
    review = models.TextField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']
        indexes = [models.Index(fields=['order'])]
   
    def __str__(self):
        return self.name



class Page(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True)
    link_on_footer = models.BooleanField(default=False)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('extra_page', args=[self.slug])



class Pricing(models.Model):
    name = models.CharField(max_length=50)
    price_range = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']
        indexes = [models.Index(fields=['order'])]
   
    def __str__(self):
        return self.name


class PriceFeature(models.Model):
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, related_name='features')
    feature = models.CharField(max_length=250)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']
        indexes = [models.Index(fields=['order'])]

    def __str__(self):
        return self.feature