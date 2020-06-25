from django.db import models
from datetime import datetime
from blogger.models import Blogger
# Create your models here.
class Posts(models.Model):
    blogger = models.ForeignKey(Blogger, on_delete=models.DO_NOTHING)
    heading = models.CharField(max_length=200)
    post_date = models.DateTimeField(default=datetime.now)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo_caption = models.CharField(max_length=200)
    body = models.CharField(max_length=600)

    heading_2 = models.CharField(max_length=200, blank=True)
    body_2 = models.CharField(max_length=600, blank=True)

    heading_3 = models.CharField(max_length=200, blank=True)
    body_3 = models.CharField(max_length=600, blank=True)

    quote_head = models.CharField(max_length=200, blank=True)
    quote = models.CharField(max_length=400, blank=True)
    quote_credit = models.CharField(max_length=40, blank=True)
    is_published = models.BooleanField(default=True)

    promo =  models.CharField(max_length=200, blank=True)
    promo_body = models.CharField(max_length=400, blank=True)
    promo_url = models.CharField(max_length=300, blank=True)
    promo_img =  models.ImageField(upload_to = 'photos/%Y/%m/%d/')


    def __str__(self):
        return self.heading
