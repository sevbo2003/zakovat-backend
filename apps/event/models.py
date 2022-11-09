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
    winner = models.ForeignKey(Team, on_delete=models.DO_NOTHING, null=True, blank=True)
    loser = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='loser', null=True, blank=True)
    draw = models.BooleanField(default=False)
    score1 = models.IntegerField()
    score2 = models.IntegerField()

    def save(self, *args, **kwargs):
        game = self.game
        game.is_finished = True
        game.save()
        super(Result, self).save(*args, **kwargs)

    def __str__(self):
        return self.game.team1.name + ' - ' + self.game.team2.name + ' ' + str(self.score1) + ' - ' + str(self.score2)