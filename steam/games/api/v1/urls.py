from django.urls import path, include

from .views import ApplicationAPIView, LibraryAPIView, ItemAPIView, GameCommentAPIView

APIMethodsCR = {'get': 'list', 'post': 'create'}
APIMethodsRUD = {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}

urlpatterns = [
    path('application', ApplicationAPIView.as_view(APIMethodsCR)),
    path('application/<int:pk>', ApplicationAPIView.as_view(APIMethodsRUD)),
    path('library', LibraryAPIView.as_view(APIMethodsCR)),
    path('library/<int:pk>', LibraryAPIView.as_view(APIMethodsRUD)),
    path('item', ItemAPIView.as_view(APIMethodsCR)),
    path('item/<int:pk>', ItemAPIView.as_view(APIMethodsRUD)),
    path('game_comment', GameCommentAPIView.as_view(APIMethodsCR)),
    path('game_comment/<int:pk>', GameCommentAPIView.as_view(APIMethodsRUD)),
]
