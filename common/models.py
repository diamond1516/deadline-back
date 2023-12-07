from django.db import models


# Create your models here.


class BaseModel(models.Model):
    cerated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField(verbose_name='Name', max_length=255)
    description = models.TextField(verbose_name='Izoh')
    image = models.ImageField(upload_to='post/')


class AboutLogin(BaseModel):
    text = models.TextField(verbose_name='Izoh')

