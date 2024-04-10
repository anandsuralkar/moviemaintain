from http.client import HTTPResponse
from re import S
from tkinter.tix import Select
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http.response import JsonResponse
from MovieApp.models import Actor,Movie, Relation
from MovieApp.serializers import ActorSerializer,MovieSerializer,RelationSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def index(request):
    return HttpResponse("This is home")
@csrf_exempt
def movieApi(request,Title=''):
    if request.method=='GET':
        Movies = Movie.objects.all()
        movie_serializer = MovieSerializer(Movies,many = True)
        return JsonResponse(movie_serializer.data,safe=False)
    elif request.method == 'PUT':
        movieData = JSONParser().parse(request)
        try:
            movie = Movie.objects.get(Title=movieData['Title'])
            movie_serializer = MovieSerializer(movie, data=movieData)
            if movie_serializer.is_valid():
                movie_serializer.save()
                return JsonResponse("Success", safe=False)
            return JsonResponse("Failed to update", safe=False)
        except ObjectDoesNotExist:
            return JsonResponse("Movie not found", status=404, safe=False)


def actorApi(request):
    if request.method=='GET':
        Actors = Actor.objects.all()
        
        actor_serializer = ActorSerializer(Actors,many=True)
        
        return JsonResponse(actor_serializer.data,safe=False)

def relationAPI(request):
    if request.method=='GET':
        Movies = Relation.objects.all()
        movies_relation_serializer=RelationSerializer(Movies,many=True)
        return JsonResponse(movies_relation_serializer.data,safe=False)
    
'''
def upvote(request,movieTitle):
    if request.method == 'GET':
        movie = Movie.objects.get(Title=movieTitle)
        print(request.GET)
        movie.upvotes = movie.upvotes+1
        #Movie.object.filter(movieTitle=title)
        movie.save()
        return JsonResponse("Success")
def downvote(request,movieTitle):
    if request.method == 'GET':
        movie = Movie.objects.get(Title=movieTitle)
        print(request.GET)
        if movie.upvotes>0:
            movie.upvotes = movie.upvotes-1
        movie.save()
        return JsonResponse("Success")

'''
