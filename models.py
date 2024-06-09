from django.db import models

# Модель "Город"
class Город(models.Model):
    название = models.CharField(max_length=255)

# Модель "Улица"
class Улица(models.Model):
    название = models.CharField(max_length=255)
    город = models.ForeignKey(Город, on_delete=models.CASCADE)

# Модель "Магазин"
class Магазин(models.Model):
    название = models.CharField(max_length=255)
    улица = models.ForeignKey(Улица, on_delete=models.CASCADE)
    время_открытия = models.TimeField()
    время_закрытия = models.TimeField()