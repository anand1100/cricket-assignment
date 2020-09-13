from django.urls import path
from .api_logic import create_team , team_detail, \
    create_player, player_detail ,\
    create_match, match_detail, \
    create_points ,points_detail


urlpatterns = [
    # URl Configrations of cricket_api

    path('team/create', create_team),
    path('team/<int:id>', team_detail),
    path('player/create', create_player),
    path('player/<int:id>', player_detail),
    path('match/create', create_match),
    path('match/<int:id>', match_detail),
    path('points/create', create_points),
    path('points/<int:id>', points_detail),
    ]