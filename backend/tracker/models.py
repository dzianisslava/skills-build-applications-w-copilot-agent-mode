
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    display_name = models.CharField(max_length=120)
    joined_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.display_name or self.username

class Team(models.Model):
    name = models.CharField(max_length=120)
    members = models.ManyToManyField(User, related_name='teams')

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=80)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    calories = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.type} ({self.date})"

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    date = models.DateField()
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    calories = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField()
    rank = models.PositiveIntegerField()
    period = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.user.username} - {self.period} - #{self.rank}"
