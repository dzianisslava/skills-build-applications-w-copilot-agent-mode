from django.test import TestCase

from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTests(TestCase):
    def test_string_representation(self):
        user = User(username='testuser', email='test@example.com', display_name='Test User')
        self.assertEqual(str(user), 'Test User')

class TeamModelTests(TestCase):
    def test_string_representation(self):
        team = Team(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

class ActivityModelTests(TestCase):
    def test_string_representation(self):
        user = User(username='testuser', email='test@example.com', display_name='Test User')
        activity = Activity(user=user, type='run', duration=30, calories=200, date='2026-01-01')
        self.assertIn('testuser', str(activity))

class WorkoutModelTests(TestCase):
    def test_string_representation(self):
        user = User(username='testuser', email='test@example.com', display_name='Test User')
        workout = Workout(user=user, name='Morning Run', date='2026-01-01', duration=30, calories=200)
        self.assertIn('Morning Run', str(workout))

class LeaderboardModelTests(TestCase):
    def test_string_representation(self):
        user = User(username='testuser', email='test@example.com', display_name='Test User')
        entry = Leaderboard(user=user, score=100, rank=1, period='weekly')
        self.assertIn('weekly', str(entry))
