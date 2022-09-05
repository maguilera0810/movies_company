
from django.urls import path, include


urlpatterns = [
    path('token/', include('api.token.routes')),
    path('v1/', include('api.v1.routes')),
]
