from django.urls import path, include

from worldOfSpeed.cars.views import catalogue_cars, create_car, details_car, edit_car, delete_car

urlpatterns = [
    path("catalogue/", catalogue_cars, name="catalogue_car"),
    path("create/", create_car, name="create_car"),
    path("<int:pk>/",
         include([
             path("details/", details_car, name="details_car"),
             path("edit/", edit_car, name="edit_car"),
             path("delete/", delete_car, name="delete_car"),
         ])),
]
