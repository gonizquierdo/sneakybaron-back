from django.urls import path, include
from django.contrib import admin
from . import views
urlpatterns = [
    path('culo/', admin.site.urls),
    path('new-waitlist-summoner/', views.new_waitlist_summoner, name='new-waitlist-summoner'),
    path('get-patch-info/', views.get_patch_info, name='get-patch-info'),
    path('riot-api-test/<str:summoner_name>', views.riot_api_test, name='riot-api-test'),

]
