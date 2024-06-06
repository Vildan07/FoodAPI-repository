from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register('food-type', FoodTypeViewSet)
router.register('food', FoodViewSet)
router.register('comment', CommentViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]