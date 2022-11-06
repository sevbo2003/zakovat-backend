from django.db import models
from apps.zakovat.models import Team


class Group(models.Model):
    name = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.name

class Game(models.Model):
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    team1 = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='team2')
    time = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.team1.name + ' - ' + self.team2.name
    

class Result(models.Model):
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    winner = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    score1 = models.IntegerField()
    score2 = models.IntegerField()

    def __str__(self):
        return self.team.name + ' - ' + str(self.score)