from django.db import models
from datetime import datetime
# Create your models here.
class Blogger(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    about = models.CharField(max_length=300)
    email = models.EmailField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    reg_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
