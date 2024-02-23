from django import forms

from worldOfSpeed.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    #

    class Meta:
        model = Profile
        fields = "__all__"
        help_texts = {
            "Age requirement: 21 years and above.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].label = "First Name"
        self.fields["last_name"].label = "Last Name"
        self.fields["profile_picture"].label = "Profile Picture"
        self.fields["password"].widget = forms.PasswordInput()
