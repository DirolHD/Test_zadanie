from rest_framework import serializers

from .models import Город, Улица, Магазин

# Сериализатор "Город"
class ГородSerializer(serializers.ModelSerializer):
    class Meta:
        model = Город
        fields = ['id', 'название']

# Сериализатор "Улица"
class УлицаSerializer(serializers.ModelSerializer):
    class Meta:
        model = Улица
        fields = ['id', 'название', 'город']

# Сериализатор "Магазин"
class МагазинSerializer(serializers.ModelSerializer):
    class Meta:
        model = Магазин
        fields = ['id', 'название', 'улица', 'время_открытия', 'время_закрытия']