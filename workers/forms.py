from django import forms
from tasks.models import Worker

class WorkerModelForm (forms.ModelForm):
    class Meta:
        model = Worker
        fields = (
            'user',
        )