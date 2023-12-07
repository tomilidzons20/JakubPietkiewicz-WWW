import graphene
from graphene_django import DjangoObjectType

from wwwapp.models import Osoba, Stanowisko


class OsobaType(DjangoObjectType):
    class Meta:
        model = Osoba
        fields = '__all__'


class StanowiskoType(DjangoObjectType):
    class Meta:
        model = Stanowisko
        fields = '__all__'


class Query(graphene.ObjectType):
    all_osobas = graphene.List(OsobaType)
    osoba_by_id = graphene.Field(OsobaType, id=graphene.Int(required=True))
    all_osobas = graphene.List(OsobaType)
    osoba_by_name = graphene.Field(OsobaType, imie=graphene.String(required=True))
    find_osobas_name_by_phrase = graphene.List(OsobaType, substr=graphene.String(required=True))
    find_stanowiskos_nazwa_by_phrase = graphene.List(StanowiskoType, substr=graphene.String(required=True))
    find_stanowisko_by_osoba = graphene.Field(StanowiskoType, id=graphene.Int(required=True))
    find_osobas_before_date = graphene.List(OsobaType, date=graphene.Date(required=True))

    def resolve_all_stanowiskos(self, info):
        return Stanowisko.objects.all()

    def resolve_osoba_by_id(self, info, id):
        try:
            return Osoba.objects.get(pk=id)
        except Osoba.DoesNotExist:
            raise Exception('Invalid osoba Id')

    def resolve_osoba_by_name(self, info, name):
        try:
            return Osoba.objects.get(imie=name)
        except Osoba.DoesNotExist:
            raise Exception(f'No Osoba with name \'{name}\' found.')

    def resolve_all_osobas(self, info):
        """ zwraca również wszystkie powiązane obiekty team dla tego obiektu Osoba"""
        return Osoba.objects.select_related("stanowisko").all()

    def resolve_find_osobas_name_by_phrase(self, info, substr):
        return Osoba.objects.filter(imie__icontains=substr)

    def resolve_find_stanowiskos_nazwa_by_phrase(self, info, substr):
        return Stanowisko.objects.filter(nazwa__icontains=substr)

    def resolve_find_stanowisko_by_osoba(self, info, id):
        try:
            stanowisko_id = Osoba.objects.get(id=id).stanowisko.id
        except Osoba.DoesNotExist:
            raise Exception('Invalid osoba id')
        return Stanowisko.objects.get(id=stanowisko_id)

    def resolve_find_osobas_before_date(self, info, date):
        return Osoba.objects.filter(data_dodania__lte=date)


schema = graphene.Schema(query=Query)
