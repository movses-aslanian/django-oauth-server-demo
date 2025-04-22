from django.contrib import admin
from django.urls import path, include

from api.views import MeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/me/', MeView.as_view(), name='me'),
]
