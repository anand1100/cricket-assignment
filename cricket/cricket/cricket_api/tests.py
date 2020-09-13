from django.test import TestCase , Client
from django.contrib.auth.models import User
from .serializers import *
from .models import *

class TeamTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="admin" , password="password")
        team_creation = Team.objects.create(
            name= "Chennai Super King",
            logo_url = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxITEhUTExMVFhUXFxgXGBgYFxYVGBcYFxUXHRgdH",
            club_state =  "Chennai"
        )
    def team_creation(self):
        self.client.login(username="admin" , password="password")
        response = self.client.get(self.team_creation)
        self.assertNotEqual(response.status_code, 301)

class PlayerTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="admin" , password="password")
        player_creation = Player.objects.create(
            firstname = "Vikart",
            lastname =  "Kohli",
            image_url = "https://google.com/virat",
            player_jercy_number =  18,
            country =  "India",
            player_history = "{\"matches\":40, \"run\":3000 , \"highest\":200,\"\"fiftys: 20,\"hundreds\": 6}",
        )
    def player_creation(self):
        self.client.login(username="admin" , password="password")
        response = self.client.get(self.player_creation)
        self.assertNotEqual(response.status_code, 301)
