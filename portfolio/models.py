from django.db import models

# Create your models here.
class Proyect(models.Model):
    title= models.CharField(max_length=200)
    link=models.URLField(null=True, blank=True)
    description=models.TextField()
    image=models.ImageField(upload_to="proyects")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-created"]

    def __str__(self):
        return self.title