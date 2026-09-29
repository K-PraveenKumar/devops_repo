from django.contrib import admin

from .models import (
    Member,
    Workout,
    Diet
)

admin.site.register(Member)
admin.site.register(Workout)
admin.site.register(Diet)