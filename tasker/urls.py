from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from tasks.views import HomePageView, SignupView
from django.conf.urls.static import static
from django.contrib.auth.views import  LogoutView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('workers/', include('workers.urls', namespace='workers')),
    path('', HomePageView.as_view(), name='home-page'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)