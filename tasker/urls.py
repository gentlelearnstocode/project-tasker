from django.contrib import admin
from django.urls import path, include

from tasks.views import HomePageView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('', HomePageView.as_view(), name='home-page')
]
