from django import forms
from django.shortcuts import render, redirect

from worldOfSpeed.profiles.forms import ProfileForm
from worldOfSpeed.profiles.models import Profile


def create_profile(request):
    hidden_fields = ["first_name", "last_name", "profile_picture"]

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue_car")
    else:
        form = ProfileForm()

    for field_name, field in form.fields.items():
        if field_name in hidden_fields:
            field.widget = forms.HiddenInput()

    context = {
        "form": form
    }

    return render(
        request,
        'profiles/profile-create.html',
        context
    )


def details_profile(request):
    profile = Profile.objects.first()
    cars = profile.cars.all()

    total_price = sum([car.price for car in cars])

    context = {
        "profile": profile,
        "total_price": total_price
    }

    return render(
        request,
        'profiles/profile-details.html',
        context
    )


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("details_profile")
    else:
        form = ProfileForm(instance=profile)

    form.fields["password"].widget = forms.TextInput()

    context = {
        "form": form,
        "profile": profile
    }

    return render(
        request,
        'profiles/profile-edit.html',
        context
    )


def delete_profile(request):
    profile = Profile.objects.first()

    if request.method == "POST":
        profile.delete()
        return redirect("index")

    context = {
        "profile": profile
    }

    return render(
        request,
        'profiles/profile-delete.html',
        context
    )
