from rest_framework import serializers
from .models import Osoba
from .models import Stanowisko


class OsobaSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        read_only=True,
    )
    imie = serializers.CharField(
        required=True,
    )
    nazwisko = serializers.CharField(
        required=True,
    )
    plec = serializers.ChoiceField(
        choices=Osoba.PLCI.choices,
        default=Osoba.PLCI.MEZCZYZNA,
    )
    stanowisko = serializers.PrimaryKeyRelatedField(
        queryset=Stanowisko.objects.all(),
    )
    data_dodania = serializers.DateField(
        read_only=True,
    )

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.save()
        return instance


class StanowiskoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = [
            'id',
            'nazwa',
            'opis',
        ]
        read_only_fields = [
            'id',
        ]
