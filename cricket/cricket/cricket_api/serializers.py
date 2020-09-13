from rest_framework import serializers
from .models  import Team , Player , Matches, Points

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields= "__all__"

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields= "__all__"

class MatchesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Matches
        fields= "__all__"

class PointsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Points
        fields= "__all__"
