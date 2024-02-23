from django.urls import path

from worldOfSpeed.home_page.views import index

urlpatterns = [
    path('', index, name='index'),
]
