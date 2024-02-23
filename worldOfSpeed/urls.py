from django.contrib import admin
from django.urls import path, include

"""
http://localhost:8000/ - Index page
http://localhost:8000/car/catalogue/ - Catalogue page
http://localhost:8000/car/create/ - Car create page
http://localhost:8000/car/<id>/details/ - Car details page
http://localhost:8000/car/<id>/edit/ - Car edit page
http://localhost:8000/car/<id>/delete/ - Car delete page
http://localhost:8000/profile/create - Profile create page
http://localhost:8000/profile/details/ - Profile details page
http://localhost:8000/profile/edit/ - Profile edit page
http://localhost:8000/profile/delete/ - Profile delete page
"""

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home Page
    path("", include("worldOfSpeed.home_page.urls")),

    # Cars
    path("car/", include("worldOfSpeed.cars.urls")),

    # Profiles
    path("profile/", include("worldOfSpeed.profiles.urls")),
]
