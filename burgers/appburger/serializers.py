from rest_framework import serializers
from appburger.models import Hamburguesa, Ingrediente

class IngredienteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length=200)
    descripcion = serializers.CharField(max_length=200)


    def create(self, validated_data):
        return Ingrediente.objects.create(**validated_data)


class HamburguesaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length=200)
    precio = serializers.IntegerField()
    descripcion = serializers.CharField(max_length=200)
    imagen = serializers.CharField(max_length=200)
    ingredientes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='ingrediente-detail'
    )

    def create(self, validated_data):
        return Hamburguesa.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.save()
        return instance

