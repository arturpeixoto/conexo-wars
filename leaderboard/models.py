from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.name}"


class DailyLeaderboard(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    date = models.DateField()
    score = models.IntegerField()

    class Meta:
        unique_together = ("player", "date")

    def __str__(self):
        return f"{self.player.name} - {self.date} - {self.score}"


class TotalLeaderboard(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player.name} - {self.total_score}"

    @staticmethod
    def update_total_leaderboard():
        players = Player.objects.all()
        for player in players:
            total_score = DailyLeaderboard.objects.filter(
                player=player).aggregate(
                models.Sum("score")
            )["score__sum"]
            if total_score is None:
                total_score = 0
            total_leaderboard, created = TotalLeaderboard.objects.get_or_create(
                player=player
            )
            total_leaderboard.total_score = total_score
            total_leaderboard.save()
