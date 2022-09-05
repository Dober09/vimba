from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import MissingPerson,WantedPerson

class MissingPersonForm(ModelForm):
    class Meta:
        model = MissingPerson
        fields = "__all__"


class WantedPersonForm(ModelForm):
    class Meta:
        model = WantedPerson
        fields = "__all__"