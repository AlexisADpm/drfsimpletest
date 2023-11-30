from rest_framework import routers
from .api import ProyectViewSet

routers = routers.DefaultRouter()

routers.register('api/projects', ProyectViewSet, 'projects')

urlpatterns = routers.urls