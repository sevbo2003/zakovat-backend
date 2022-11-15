from django.db import models


class Developer(models.Model):
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=5)
    university = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    image = models.ImageField(upload_to='developers/')
    description = models.CharField(max_length=50)
    site = models.URLField(null=True, blank=True)
    telegram = models.URLField()
    instagram = models.URLField()
    github = models.URLField()


class BestPlayer(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='best_players/')
    description = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    group = models.CharField(max_length=5)


class BestPlayerInfo(models.Model):
    description = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.description


class CurrentGame(models.Model):
    team1 = models.ForeignKey('zakovat.Team', on_delete=models.CASCADE, related_name='current_game_team1')
    team2 = models.ForeignKey('zakovat.Team', on_delete=models.CASCADE, related_name='current_game_team2')
    score1 = models.IntegerField()
    score2 = models.IntegerField()


    def __str__(self) -> str:
        return f'{self.team1} - {self.team2}'


class YouTubeLink(models.Model):
    link = models.URLField()
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.description


