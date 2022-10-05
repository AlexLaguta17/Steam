from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ProfileAPIView, InventoryAPIView, FriendAPIView, BalanceAPIView, VacBanAPIView, \
    ProfileCommentAPIView, BuyRequestAPIView

router = DefaultRouter()
router.register('profiles', ProfileAPIView, basename='profile')
router.register('inventories', InventoryAPIView, basename='inventory')
router.register('friends', FriendAPIView, basename='friend')
router.register('balances', BalanceAPIView, basename='balance')
router.register('vac_bans', VacBanAPIView, basename='vac_ban')
router.register('profile_comments', ProfileCommentAPIView, basename='profile_comment')
router.register('buy_requests', BuyRequestAPIView, basename='buy_request')

urlpatterns = router.urls
