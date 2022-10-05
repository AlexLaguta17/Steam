from rest_framework.routers import DefaultRouter

from user.api.v1.views import UserAPIView

router = DefaultRouter()
router.register('users', UserAPIView, basename='user')

urlpatterns = router.urls
