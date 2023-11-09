from wwwapp.models import Osoba, Stanowisko
from wwwapp.serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# 1.Stworzenie nowej instancji klasy Osoba
- osoba = Osoba(imie='Nikita', nazwisko='Oszejko', plec='1', stanowisko=Stanowisko.objects.get(nazwa='Król'))
- osoba.save()

# 2.Inicjalizacja serializera
- serializer = OsobaSerializer(osoba)
- serializer.data
#### Output
{'id': 6, 'imie': 'Nikita', 'nazwisko': 'Oszejko', 'plec': 1, 'stanowisko': 2, 'data_dodania': '2023-10-26'}

# 3.Serializacja danych do JSON
- content = JSONRenderer().render(serializer.data)
- content
#### Output
b'{"id":6,"imie":"Nikita","nazwisko":"Oszejko","plec":1,"stanowisko":2,"data_dodania":"2023-10-26"}'

# Walidacja
- import io
- stream = io.BytesIO(content)
- data = JSONParser().parse(stream)
- deserializer = OsobaSerializer(data=data)
- deserializer.is_valid()
#### Output
True
- deserializer.fields
#### Output
{'id': IntegerField(read_only=True), 'imie': CharField(required=True), 'nazwisko': CharField(required=True), 'plec': ChoiceField(choices=[(1, 'Mezczyzna'), (2, 'Kobieta'), (3, 'Inne')], default=Osoba.PLCI.MEZCZYZNA), 'stanowisko': PrimaryKeyRelatedField(queryset=<QuerySet [<Stanowisko: Pet>, <Stanowisko: Król>, <Stanowisko: Błazen>]>), 'data_dodania': DateField(read_only=True)}
- deserializer.validated_data
#### Output
OrderedDict([('imie', 'Nikita'), ('nazwisko', 'Oszejko'), ('plec', 1), ('stanowisko', <Stanowisko: Król>)])
- deserializer.save()
<Osoba: Nikita Oszejko>
- deserializer.data
{'id': 7, 'imie': 'Nikita', 'nazwisko': 'Oszejko', 'plec': 1, 'stanowisko': 2, 'data_dodania': '2023-10-26'}

# 1.Stworzenie nowej instancji klasy Stanowisko
- stanowisko = Stanowisko(nazwa='Prezes', opis='Prezes zarządu')
- stanowisko.save()

# 2.Inicjalizacja serializera
- serializer = StanowiskoSerializer(stanowisko) 
- serializer.data
#### Output
{'id': 4, 'nazwa': 'Prezes', 'opis': 'Prezes zarządu'}

# 3.Serializacja danych do JSON
- content = JSONRenderer().render(serializer.data)
- content
#### Output
b'{"id":4,"nazwa":"Prezes","opis":"Prezes zarz\xc4\x85du"}'

# Walidacja
- import io
- stream = io.BytesIO(content)
- data = JSONParser().parse(stream)
- deserializer = StanowiskoSerializer(data=data)
- deserializer.is_valid()
#### Output
True
- deserializer.fields
#### Output
{'id': IntegerField(label='ID', read_only=True), 'nazwa': CharField(), 'opis': CharField(allow_blank=True, required=False)}
- deserializer.validated_data
#### Output
OrderedDict([('nazwa', 'Prezes'), ('opis', 'Prezes zarządu')])
- deserializer.save()
<Stanowisko: Prezes>
- deserializer.data
{'id': 5, 'nazwa': 'Prezes', 'opis': 'Prezes zarządu'}
