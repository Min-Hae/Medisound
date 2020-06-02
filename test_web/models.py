from django.db import models
from django.urls import reverse


class Drug(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=20)
    effect = models.TextField()
    use = models.TextField()
    ingredient = models.TextField(null=True)

    class Meta:
        ordering = ['id', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('drug-detail', args=[str(self.id)])


class Image(models.Model):
    img = models.ImageField(upload_to="image")
    name = models.CharField(max_length=30)
