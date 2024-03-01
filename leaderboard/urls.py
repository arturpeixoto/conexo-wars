from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView)

app_name = "leaderboard"

urlpatterns = [
    path("", views.total_leaderboard, name="total_leaderboard"),
    path(
        "daily_leaderboard/", views.daily_leaderboard, name="daily_leaderboard"
    ),
    path(
        "daily_leaderboard/<str:date>/",
        views.daily_leaderboard,
        name="daily_leaderboard_detail",
    ),
    path('create_game/', views.create_game, name='create_game'),
    path('create_player/', views.create_player, name='create_player'),
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
    path(
      "delete_entry/<int:entry_id>/", views.delete_entry, name="delete_entry"
    ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

handler404 = views.custom_page_not_found
