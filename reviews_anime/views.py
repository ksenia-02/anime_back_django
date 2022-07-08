from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def genre_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def genre_detail(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def anime_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        anime = Anime.objects.all()
        serializer = AnimeSerializer(anime, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def anime_detail(request, pk):
    try:
        anime = Anime.objects.get(pk=pk)
    except Anime.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GenreSerializer(anime)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GenreSerializer(anime, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        anime.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def raitingStar_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        star = RaitingStar.objects.all()
        serializer = RaitingStarSerializer(star, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RaitingStarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def raitingStar_detail(request, pk):
    try:
        star = RaitingStar.objects.get(pk=pk)
    except RaitingStar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RaitingStarSerializer(star)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RaitingStarSerializer(star, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        star.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reviews_list(request):
    if request.method == 'GET':
        reviews = Reviews.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail(request, pk):
    try:
        reviews = Reviews.objects.get(pk=pk)
    except Reviews.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewsSerializer(reviews)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewsSerializer(reviews, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def raiting_list(request):
    if request.method == 'GET':
        raiting = Raiting.objects.all()
        serializer = RaitingSerializer(raiting, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RaitingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def raiting_detail(request, pk):
    try:
        raiting = Raiting.objects.get(pk=pk)
    except Raiting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RaitingSerializer(raiting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RaitingSerializer(raiting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        raiting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
