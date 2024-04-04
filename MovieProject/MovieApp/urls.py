from django.urls import path,re_path as url
from MovieApp import views


urlpatterns=[
    path("",views.actorApi),
    url(r'^actor/$',views.actorApi),
    url(r'^movie/$',views.movieApi),
    url(r'^relation/$',views.relationAPI),
    #url(r'^upvote/  ',views.upvote),
    #url(r'^downvote/',views.downvote),
    #url(r'^actor/[0-9]',views.actorMoviesApi),
    #([a-z,A-Z]+)

    ]