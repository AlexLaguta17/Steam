from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ApplicationAPIView, LibraryAPIView, ItemAPIView, GameCommentAPIView

router = DefaultRouter()
router.register('applications', ApplicationAPIView, basename='application')
router.register('libraries', LibraryAPIView, basename='library')
router.register('items', ItemAPIView, basename='item')
router.register('game_comments', GameCommentAPIView, basename='game_comment')

urlpatterns = router.urls
