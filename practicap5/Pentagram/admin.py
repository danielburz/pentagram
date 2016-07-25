from django.contrib import admin

# Register your models here.
from Pentagram.models import Photo, Comments

admin.site.register(Photo)
admin.site.register(Comments)
#admin.site.register(Likes)