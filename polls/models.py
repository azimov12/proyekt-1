from django.db import models

# Create your models here.
class NewsModel(models.Model):
    tittle = models.CharField(default="")
    body = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.tittle