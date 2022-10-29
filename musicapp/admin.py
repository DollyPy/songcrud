from django.contrib import admin
from .models import Artiste, Song
# Register your models here.
@admin.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "age")

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("title", "singer", "date_released")
    ordering = ["-date_released"]

