from django.urls import path, include
from django.contrib import admin
from . import views
urlpatterns = [
    path('widget/<str:region>/<str:summoner_name>', views.get_stream_widget, name='get-stream-widget'),

]
