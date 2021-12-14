from django import forms
from django.forms import fields, models, widgets
from .models import Task, User, Worker
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()
#better form
class DateInput(forms.DateInput):
    input_type = 'date'

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = fields = '__all__'
        widgets = {
            'on_date': DateInput()
        }

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email')
        field_classes = {'username': UsernameField}

class AssignWorkerForm(forms.Form):
    worker = forms.ModelChoiceField(queryset=Worker.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        workers = Worker.objects.filter(department=request.user.userprofile)
        super(AssignWorkerForm, self).__init__(*args, **kwargs)
        self.fields['worker'].queryset = workers


# LOCATION_CHOICES = (
#     ('Elizah Hall', 'Elizah Hall'),
#     ('Solomon Hall', 'Solomon Hall'),
#     ('Eve Hall', 'Eve Hall'),
#     ('Sarah Hall', 'Sarah Hall'),
#     ('Esther Hall', 'Esther Hall'),
#     ('Ruth Hall', 'Ruth Hall'),
#     ('Guest House', 'Guest House'),
#     ('Library', 'Library'),
#     ('Cafeteria', 'Cafeteria'),
#     ('IT Building', 'IT Building'),
#     ('Admin Building', 'Admin Building'),
#     ('Science Building', 'Science Building'),
#     ('Hope Channel', 'Hope Channel'),
#     ('Church', 'Church')
#     )

# CATEGORY_CHOICES = (
#     ('Assistant', 'Assistant'),
#     ('Monitor', 'Monitor'),
#     ('Janitor', 'Janitor'),
#     ('Supervisor', 'Supervisor'),
#     ('Video Editor', 'Video Editor'),
#     ('Chaplain', 'Chaplain')
#     )

#     title = models.CharField(max_length=100)
#     date_added = models.DateTimeField(auto_now_add=True)
#     location = models.CharField(choices=LOCATION_CHOICES, max_length=100)
#     category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
#     description = models.TextField(null=True, blank=True)
#     worker = models.ForeignKey('Worker', on_delete=CASCADE)
# class TaskForm(forms.Form):
#     title = forms.CharField()
#     date = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'date'}))
#     location = forms.ChoiceField(choices=LOCATION_CHOICES)
#     category = forms.ChoiceField(choices=CATEGORY_CHOICES)
#     description = forms.CharField(widget=forms.Textarea)

