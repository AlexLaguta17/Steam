from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ApplicationAPIView, LibraryAPIView, ItemAPIView, GameCommentAPIView, GetApplicationInfoAPIView, \
    GetUserAppAPIView, GetTopUserAppsAPIView

router = DefaultRouter()
router.register('applications', ApplicationAPIView, basename='application')
router.register('libraries', LibraryAPIView, basename='library')
router.register('items', ItemAPIView, basename='item')
router.register('game_comments', GameCommentAPIView, basename='game_comment')

urlpatterns = [
    path('get_application_info/', GetApplicationInfoAPIView.as_view()),
    path('get_user_apps/', GetUserAppAPIView.as_view()),
    path('get_top_user_apps/<int:pk>/', GetTopUserAppsAPIView.as_view())
]

urlpatterns += router.urls
