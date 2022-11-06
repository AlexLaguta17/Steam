from django.contrib import admin

# Register your models here.
from account.models import Profile, Inventory, Friend, Balance, VacBan, ProfileComment, BuyRequest

admin.site.register(Profile)
admin.site.register(Inventory)
admin.site.register(Friend)
admin.site.register(Balance)
admin.site.register(VacBan)
admin.site.register(ProfileComment)
admin.site.register(BuyRequest)
