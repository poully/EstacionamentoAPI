from django.urls import path, include
from alocaVaga import views
from rest_framework import routers

app_name = 'alocaVaga'

router = routers.DefaultRouter()
router.register('alocada', views.AlocadaViewSet)
router.register('vazia', views.VaziaViewSet)

urlpatterns = [
        path('',include(router.urls)),
]