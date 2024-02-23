from django import forms

from worldOfSpeed.cars.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

        widgets = {
            "image_url": forms.URLInput(attrs={"placeholder": "https://..."}),
            "owner": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["owner"].required = False
        self.fields["image_url"].label = "Image URL"
