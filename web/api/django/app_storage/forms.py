from django.forms import ModelForm
from .models import File as Upload


class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ['file']
