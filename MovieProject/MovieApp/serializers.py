
from rest_framework import serializers
from MovieApp.models import Movie,Actor,Relation

class RelationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Relation
        fields = (
            'Actor_id',
            'Movie_id',
            )

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            
            'Title',
            'Description',
            'ReleaseDate',
            'Votes',
            )


class ActorSerializer(serializers.ModelSerializer):
    #Movies = Relation.objects.raw('SELECT Movie_id FROM MovieApp_relation')
    #movie_set=RelationSerializer(Movies,many=True)
    class Meta:
        model = Actor
        fields = (
            
            'Name',
            'DOB',

            )


            


