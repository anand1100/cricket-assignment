from django.db import models


class Team(models.Model):
    name = models.CharField(max_length = 100 , blank=False)
    logo_url = models.CharField(max_length = 100 , blank=False)
    club_state = models.CharField(max_length = 100 , blank=False)

    def __str__(self):
        return "Team Name- "+self.name

class Player(models.Model):
    firstname = models.CharField(max_length = 100 , blank=False)
    lastname = models.CharField(max_length=100, blank=False)
    image_url = models.CharField(max_length=100, blank=False)
    player_jercy_number = models.IntegerField()
    country = models.CharField(max_length=100, blank=False)
    player_history = models.TextField(max_length=1000 , blank=False)
    teams = models.ForeignKey('Team', on_delete = models.CASCADE, null=True)

    def __str__(self):
        return "Player Name- "+self.firstname+" "+self.lastname



class Matches(models.Model):
    teams_A = models.ForeignKey(Team, related_name ='team1', on_delete = models.CASCADE, null=True)
    teams_B = models.ForeignKey(Team, related_name ='team2' ,  on_delete = models.CASCADE, null=True)
    winner = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return "Winner Match - " + self.winner

class Points(models.Model):
    winner = models.ForeignKey('Matches', on_delete = models.CASCADE)
    rewards = models.IntegerField()

    def __str__(self):
        return "Winner Team Points - " + str(self.winner)



