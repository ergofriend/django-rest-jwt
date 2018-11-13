from django.urls import path, include
from .routers import router as api_router

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(api_router.urls)),
]
