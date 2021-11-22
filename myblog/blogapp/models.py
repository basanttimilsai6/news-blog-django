from django.db import models

# Create your models here.
class post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=20)
    slug = models.CharField(max_length=130)
    image = models.CharField(max_length=500)
    timestamp = models.DateTimeField(blank=True)
    

    def __str__(self):
        return self.title + '-->' + 'created by-->' + self.author