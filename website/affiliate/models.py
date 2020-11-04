from django.db import models
from django.utils import timezone

# Create your models here.
class amazonAffiliate(models.Model):

    site_url        = models.CharField(max_length=200)
    tag             = models.CharField(max_length=20)
    price           = models.CharField(max_length=10)
    product_link    = models.CharField(max_length=200)
    pub_date = models.DateTimeField(timezone.now)
    image_link      = models.CharField(max_length=200)
    title      = models.CharField(max_length=200)
    
    def __str__(self):
        return self.product_link

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

        