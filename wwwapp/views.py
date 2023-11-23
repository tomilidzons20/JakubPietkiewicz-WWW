from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http.response import HttpResponse, Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Osoba
from .models import Stanowisko
from .serializers import OsobaSerializer
from .serializers import StanowiskoSerializer
from .permissions import CustomDjangoModelPermissions


class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_list(request):
    if request.method == 'GET':
        osoby = Osoba.objects.all().order_by('id')
        nazwisko = request.query_params.get('nazwisko')
        if nazwisko:
            osoby = Osoba.objects.filter(nazwisko__icontains=nazwisko).order_by('id')
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OsobaSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save(wlasciciel=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def osoba_stanowisko(request, pk):
    if request.method == 'GET':
        osoby = Osoba.objects.filter(stanowisko=pk).order_by('id')
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_get(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.user != osoba.wlasciciel:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)


@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_put(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.user != osoba.wlasciciel:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'PUT':
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save(wlasciciel=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def osoba_delete(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.user != osoba.wlasciciel:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def stanowisko_list(request):
    if request.method == 'GET':
        stanowiska = Stanowisko.objects.all().order_by('id')
        serializer = StanowiskoSerializer(stanowiska, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StanowiskoSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def stanowisko_detail(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StanowiskoSerializer(stanowisko)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StanowiskoSerializer(stanowisko, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def osoba_view(request):
    if not request.user.has_perm('wwwapp.view_osoba') or not request.user.has_perm('wwwapp.can_view_other_persons'):
        return HttpResponse(f"Nie masz uprawnien view_osoba i can_view_other_persons.")
    osoby = Osoba.objects.all()
    message = ''
    for osoba in osoby:
        message += f'<br>{osoba}'
    return HttpResponse(f"Masz uprawnienia view_osoba i can_view_other_persons. <br>{message}")


class OsobaListView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]

    def get_queryset(self):
        return Osoba.objects.all()

    def get(self, request):
        osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)
