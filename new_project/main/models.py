from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Film(models.Model):
    class Meta:
        ordering = ['-rating', 'title', 'updated']
    director = models.ForeignKey(Director, on_delete=models.PROTECT, related_name="directors", null=True)
    title = models.CharField(max_length=100, default="no name")
    regiser = models.CharField(max_length=150)
    rating = models.FloatField()
    dlitelnost = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
