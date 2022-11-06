from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ProfileAPIView, InventoryAPIView, FriendAPIView, BalanceAPIView, VacBanAPIView, \
    ProfileCommentAPIView, BuyRequestAPIView, GetProfileInfoAPIView, GetUserFriendsAPIView, GetUserInventoryAPIView, \
    GetActiveLotsAPIView, GetSellingItemsAPIView

router = DefaultRouter()
router.register('profiles', ProfileAPIView, basename='profile')
router.register('inventories', InventoryAPIView, basename='inventory')
router.register('friends', FriendAPIView, basename='friend')
router.register('balances', BalanceAPIView, basename='balance')
router.register('vac_bans', VacBanAPIView, basename='vac_ban')
router.register('profile_comments', ProfileCommentAPIView, basename='profile_comment')
router.register('buy_requests', BuyRequestAPIView, basename='buy_request')

urlpatterns = [
    path('get_profile_info/<int:pk>/', GetProfileInfoAPIView.as_view()),
    path('get_user_friends/<int:user_id>/', GetUserFriendsAPIView.as_view()),
    path('get_user_inventory/', GetUserInventoryAPIView.as_view()),
    path('get_active_lots/<int:user_id>/', GetActiveLotsAPIView.as_view()),
    path('get_selling_items/', GetSellingItemsAPIView.as_view()),
]

urlpatterns += router.urls
