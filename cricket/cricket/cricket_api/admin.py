from django.contrib import admin
from  .models import  Team, Player, Matches, Points

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Matches)
admin.site.register(Points)

