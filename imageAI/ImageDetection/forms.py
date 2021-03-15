from django.forms import ModelForm
from .models import *

class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = '__all__'