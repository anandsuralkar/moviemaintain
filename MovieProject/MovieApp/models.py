from django.db import models

# Create your models here.
# Create your models here.
class Movie(models.Model):
#    MovieID = models.AutoField()
    Title = models.CharField(max_length=100,primary_key=True)
    Description = models.CharField(max_length=1024)
    ReleaseDate = models.DateField()
    Votes = models.IntegerField(default=0)


class Actor(models.Model):
#    ActorID = models.AutoField()
    Name = models.CharField(max_length=100,primary_key=True)
    DOB = models.DateField()

class Relation(models.Model):
    Actor_id = models.ForeignKey(Actor,on_delete=models.CASCADE)
    Movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['Actor_id','Movie_id'],
                name='Relation'
            )
        ]
