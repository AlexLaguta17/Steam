from django.urls import path, include

from .views import ProfileAPIView, InventoryAPIView, FriendAPIView, BalanceAPIView, VacBanAPIView, \
    ProfileCommentAPIView, BuyRequestAPIView

APIMethodsCR = {'get': 'list', 'post': 'create'}
APIMethodsRUD = {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}

urlpatterns = [
    path('profile', ProfileAPIView.as_view(APIMethodsCR)),
    path('profile/<int:pk>', ProfileAPIView.as_view(APIMethodsRUD)),
    path('inventory', InventoryAPIView.as_view(APIMethodsCR)),
    path('inventory/<int:pk>', InventoryAPIView.as_view(APIMethodsRUD)),
    path('friend', FriendAPIView.as_view(APIMethodsCR)),
    path('friend/<int:pk>', FriendAPIView.as_view(APIMethodsRUD)),
    path('balance', BalanceAPIView.as_view(APIMethodsCR)),
    path('balance/<int:pk>', BalanceAPIView.as_view(APIMethodsRUD)),
    path('vac_ban', VacBanAPIView.as_view(APIMethodsCR)),
    path('vac_ban/<int:pk>', VacBanAPIView.as_view(APIMethodsRUD)),
    path('profile_comment', ProfileCommentAPIView.as_view(APIMethodsCR)),
    path('profile_comment/<int:pk>', ProfileCommentAPIView.as_view(APIMethodsRUD)),
    path('buy_request', BuyRequestAPIView.as_view(APIMethodsCR)),
    path('buy_request/<int:pk>', BuyRequestAPIView.as_view(APIMethodsRUD)),
]
