

from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.db import transaction
from tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    """
    Django management command to populate the database with test data for users, teams, activities, workouts, and leaderboard.
    This command creates test data for development and testing purposes.
    """
    help = 'Populate the database with test data for users, teams, activities, workouts, and leaderboard.'

    @transaction.atomic
    def handle(self, *args, **options):
        self.populate_test_data()

    def populate_test_data(self):
        """
        Create test data for users, teams, activities, workouts, and leaderboard.
        """
        today = date.today()

        # Users
        user1 = User.objects.create(username='alice', email='alice@example.com', display_name='Alice')
        user2 = User.objects.create(username='bob', email='bob@example.com', display_name='Bob')
        user3 = User.objects.create(username='charlie', email='charlie@example.com', display_name='Charlie')

        # Teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')
        team1.members.set([user1, user2])
        team2.members.set([user2, user3])

        # Activities
        Activity.objects.create(user=user1, type='run', duration=30, calories=250, date=today)
        Activity.objects.create(user=user2, type='bike', duration=45, calories=400, date=today)
        Activity.objects.create(user=user3, type='swim', duration=60, calories=500, date=today)

        # Workouts
        Workout.objects.create(user=user1, name='Morning Cardio', description='Cardio session', date=today, duration=30, calories=250)
        Workout.objects.create(user=user2, name='Evening Ride', description='Cycling', date=today, duration=45, calories=400)
        Workout.objects.create(user=user3, name='Swim Session', description='Swimming laps', date=today, duration=60, calories=500)

        # Leaderboard
        Leaderboard.objects.create(user=user1, score=100, rank=1, period='weekly')
        Leaderboard.objects.create(user=user2, score=80, rank=2, period='weekly')
        Leaderboard.objects.create
(user=user3, score=60, rank=3, period='weekly')

        self.stdout.write(self.style.SUCCESS('OctoFit test data created: 3 users, 2 teams, 3 activities, 3 workouts, 3 leaderboard entries.'))