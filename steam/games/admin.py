from django.contrib import admin

from games.models import Application, Library, Item, GameComment


admin.site.register(Application)
admin.site.register(Library)
admin.site.register(Item)
admin.site.register(GameComment)

