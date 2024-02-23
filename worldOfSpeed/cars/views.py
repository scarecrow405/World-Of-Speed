from django.shortcuts import render, redirect

from worldOfSpeed.cars.forms import CarForm
from worldOfSpeed.cars.models import Car
from worldOfSpeed.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


def catalogue_cars(request):
    profile = get_profile()
    cars = profile.cars.all()
    cars_count = cars.count()

    context = {
        "cars": cars,
        "cars_count": cars_count,
        "profile": profile
    }

    return render(
        request,
        "cars/catalogue.html",
        context
    )


def create_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)

            profile = Profile.objects.first()
            car.owner = profile

            car.save()
            return redirect("catalogue_car")
    else:
        form = CarForm()

    context = {
        "form": form,
        "profile": get_profile()
    }

    return render(
        request,
        "cars/car-create.html",
        context
    )


def details_car(request, pk):
    car = Car.objects.get(pk=pk)

    context = {
        "car": car,
        "profile": get_profile()
    }

    return render(
        request,
        "cars/car-details.html",
        context
    )


def edit_car(request, pk):
    car = Car.objects.get(pk=pk)
    profile = get_profile()

    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue_car')
    else:
        form = CarForm(instance=car)

    context = {
        "car": car,
        "form": form,
        "profile": profile
    }

    return render(
        request,
        "cars/car-edit.html",
        context
    )


def delete_car(request, pk):
    car = Car.objects.get(pk=pk)
    profile = get_profile()

    if request.method == "POST":
        car.delete()
        return redirect('catalogue_car')

    form = CarForm(instance=car)
    for field in form.fields.values():
        field.widget.attrs['readonly'] = True
        field.widget.attrs['disabled'] = True

    context = {
        "car": car,
        "form": form,
        "profile": profile
    }

    return render(
        request,
        "cars/car-delete.html",
        context
    )
