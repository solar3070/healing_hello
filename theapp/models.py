from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField('date published')
    body = models.CharField(max_length=500)

    def __str__(self):
        return self.title

