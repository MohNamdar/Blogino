from django.db import models
from django.contrib.auth.models import AbstractUser
from django_jalali.db import models as jmodels
from django.template.defaultfilters import slugify
from django.urls import reverse


# Managers
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


# Create your models here.
class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile = models.ImageField(upload_to="profiles", blank=True, null=True)
    phone = models.CharField(max_length=11, null=True, blank=True)


class Article(models.Model):
    class Category(models.TextChoices):
        AI = 'AI', 'هوش مصنوعی'
        TECHNOLOGY = 'TCH', 'تکنولوژی'
        PROGRAMMING = 'PRG', 'برنامه نویسی'
        SECURITY = 'SEC', 'امنیت'
        PODCAST = 'PDC', 'پادکست'
        VIDEOCAST = 'VDC', 'ویدئوکست'

    title = models.CharField(max_length=250)
    cover = models.ImageField(upload_to="cover", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    content = models.TextField()
    create_date = jmodels.jDateTimeField(auto_now_add=True)
    update_date = jmodels.jDateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250, unique=True)
    category = models.CharField(choices=Category.choices, max_length=3, default=Category.TECHNOLOGY)
    tags = models.ManyToManyField('Tag', related_name='articles', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']
        indexes = [models.Index(fields=['-create_date'])]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:article_single", kwargs={'slug': self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    objects = models.Manager()
    actived = ActiveManager()

    def __str__(self):
        return f"{self.name} #{self.article}"
