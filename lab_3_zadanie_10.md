**Zadanie 10**  
Korzystając z dokumentacji API klasy QuerySet z pkt. 3 wykonaj następujące zapytania za pomocą shella Django (**kod Pythona z zapytaniami umieść w pliku lab_3_zadanie_10.md w swoim repozytorium**):
* wyświetl wszystkie obiekty modelu `Osoba`,
  * Osoba.objects.all()
* wyświetl obiekt modelu `Osoba` z id = 3,
  * Osoba.objects.get(id=3)
* wyświetl obiekty modelu `Osoba`, których nazwa rozpoczyna się na wybraną przez Ciebie literę alfabetu (tak, żeby był co najmniej jeden wynik),
  * Osoba.objects.filter(imie__startswith='B')
* wyświetl unikalną listę stanowisk przypisanych dla modeli `Osoba`,
  * Osoba.objects.order_by().values_list('stanowisko__nazwa', flat=True).distinct()
* wyświetl nazwy stanowisk posortowane alfabetycznie malejąco,
  * Stanowisko.objects.values_list('nazwa', flat=True).order_by('-nazwa')
* dodaj nową instancję obiektu klasy `Osoba` i zapisz w bazie.
  * Osoba.objects.create(imie='Robert', nazwisko='Makłowicz', plec='1', stanowisko=Stanowisko.objects.get(nazwa='Król')) 