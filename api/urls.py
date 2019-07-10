from django.urls import path, include
from . import views
urlpatterns = [
    path('widget/<str:code>', views.get_stream_widget, name='get-stream-widget'),
    path('patch/<str:language>/<str:patch>', views.get_patch_info, name='get-patch-info'),
]
