from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Osoba
from .models import Stanowisko
from .serializers import OsobaSerializer
from .serializers import StanowiskoSerializer


class OsobaList(APIView):
    def get(self, request):
        osoby = Osoba.objects.all().order_by('id')
        nazwisko = request.query_params.get('nazwisko')
        if nazwisko:
            osoby = Osoba.objects.filter(nazwisko__icontains=nazwisko).order_by('id')
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OsobaSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OsobaDetail(APIView):
    def get_object(self, pk):
        try:
            return Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = OsobaSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = OsobaSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StanowiskoList(APIView):
    def get(self, request):
        stanowiska = Stanowisko.objects.all().order_by('id')
        serializer = StanowiskoSerializer(stanowiska, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StanowiskoSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StanowiskoDetail(APIView):
    def get_object(self, pk):
        try:
            return Stanowisko.objects.get(pk=pk)
        except Stanowisko.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = StanowiskoSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = StanowiskoSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
