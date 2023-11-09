from rest_framework import routers
from weather_api.api import DescriptionViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r"descriptions", DescriptionViewSet)