from django.db import models


class FAQ(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ['order']


MEMBERS_ROLE_CHOICES = (
    ('leader', 'Leader'),
    ('member', 'Member'),
)

class Member(models.Model):
    role = models.CharField(max_length=10, choices=MEMBERS_ROLE_CHOICES )
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to= 'members/%Y/%m',blank=True, null=True)
    designation = models.CharField(max_length=250, blank=True)
    linkedin = models.URLField(blank=True, help_text='please use https:// before link')
    github = models.URLField(blank=True, help_text='please use https:// before link')
    facebook = models.URLField(blank=True, help_text='please use https:// before link')
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order',]
        indexes = [models.Index(fields=['order'])]
   
    def __str__(self):
        return self.name


class ProjectSummary(models.Model):
    figure = models.CharField(max_length=10)
    detail = models.CharField(max_length=250)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order',]
        indexes = [models.Index(fields=['order'])]
   
    def __str__(self):
        return self.detail

class Portfolio(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/%Y/%m', blank=True)
    duration = models.CharField(max_length=50)
    detail = models.TextField()
    link = models.URLField(blank=True, help_text='please use https:// before link')
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order',]
        indexes = [models.Index(fields=['order'])]
   
    def __str__(self):
        return self.title