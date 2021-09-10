from django.urls import path,include
from rest_framework.routers import DefaultRouter
from inventory_api import views


router = DefaultRouter()
router.register(r'clubs', views.ClubViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

