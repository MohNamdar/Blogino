from django.db import models
from django.contrib.auth.models import AbstractUser
from django_jalali.db import models as jmodels
from django.template.defaultfilters import slugify
from django.urls import reverse


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