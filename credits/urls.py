from django.urls import include, path
from rest_framework import routers
from .views import ApplicationViewSet, BlacklistView, BorrowerViewSet, ProgramViewSet


router = routers.DefaultRouter()
router.register(r'applications', ApplicationViewSet)
router.register(r'blacklist', BlacklistView)
router.register(r'borrowers', BorrowerViewSet)
router.register(r'programs', ProgramViewSet)

urlpatterns = [
    path('', include(router.urls))
]
