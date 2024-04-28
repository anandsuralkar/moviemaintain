from django.urls import path,re_path as url
from MovieApp import views


urlpatterns=[
    #path("",views.actorApi),
    url(r'^actor/$',views.actorApi),
    url(r'^movie/$',views.movieApi),
    url(r'^relation/$',views.relationAPI),
    url(r'^actor$',views.actorApi),
    url(r'^movie$',views.movieApi),
    url(r'^relation$',views.relationAPI),
    #url(r'^api/upvote/  ',views.upvote),
    #url(r'^api/downvote/',views.downvote),
    #url(r'^api/actor/[0-9]',views.actorMoviesApi),
    #([a-z,A-Z]+)    url(r'^actor/$',views.actorApi),
    ]