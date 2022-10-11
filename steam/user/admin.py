from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'role', 'email', 'password1', 'password2', 'username', 'first_name', 'last_name',
                'phone_number',
            ),
        }),
    )


admin.site.register(User, CustomUserAdmin)
