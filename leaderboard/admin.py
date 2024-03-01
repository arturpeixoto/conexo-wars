from django.contrib import admin
from .models import Player, DailyLeaderboard, TotalLeaderboard

admin.site.register(Player)
admin.site.register(DailyLeaderboard)
admin.site.register(TotalLeaderboard)
