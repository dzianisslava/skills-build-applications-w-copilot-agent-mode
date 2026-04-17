"""
REST API endpoints are available at:
    https://$CODESPACE_NAME-8000.app.github.dev/api/[component]/
Example: https://$CODESPACE_NAME-8000.app.github.dev/api/activities/
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)
router.register(r'workouts', views.WorkoutViewSet)

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('api/', include(router.urls)),
]
