from rest_framework import serializers
from datetime import date


def letters_only(data):
    if isinstance(data, str):
        if all(char.isalpha() or char.isspace() for char in data):
            return data
        raise serializers.ValidationError('Napis nie zawiera tylko liter')
    raise serializers.ValidationError('Nie jest to napis')


def date_check(date):
    if date < date.today():
        return date
    raise serializers.ValidationError('Podana data jest w przyszlosci')

