from django.db import models


class Telefon(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Mashina(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    brend = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "mashina"
        verbose_name_plural = "mashinalar"

    def __str__(self):
        return self.name
