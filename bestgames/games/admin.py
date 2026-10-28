from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'developer']
    list_filter = ['genre']
    search_fields = ['title']
    ordering = ['price']
