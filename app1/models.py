from django.db import models

# Create your models here.
class Muaji(models.Model):
    mauji = models.CharField(max_length=20)
    sfida = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f'{self.mauji}'

