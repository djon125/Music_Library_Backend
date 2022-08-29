from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Song



@api_view(['GET', 'POST'])
def songs_list(request):  
    
    if request.method == 'GET':
        songs = Song.objects.all()
        genre_name = request.query_params.get('genre') 
        artist_name = request.query_params.get('artist')
        album_name = request.query_params.get('album')
        release_date = request.query_params.get('date')
        title_name = request.query_params.get('title')
        if genre_name:
            songs= songs.filter(genre__exact=genre_name)
        serializer = SongSerializer(songs, many=True)
        if artist_name:
            songs =songs.filter(artist__exact=artist_name)
        serializer = SongSerializer(songs, many=True)
        if album_name:
            songs =songs.filter(album__exact=album_name)
        serializer = SongSerializer(songs, many=True)
        if release_date:
            songs =songs.filter(release_date__exact=release_date)
        serializer = SongSerializer(songs, many=True)
        if title_name:
            songs =songs.filter(title__exact=title_name)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)   
    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializer =SongSerializer(song)
        return Response(serializer.data)  
    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

