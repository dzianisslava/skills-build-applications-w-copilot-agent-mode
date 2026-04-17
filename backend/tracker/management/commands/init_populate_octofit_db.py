from datetime import date, timedelta

from django.core.management.base import BaseCommand
from django.db import transaction

from tracker.models import Goal, Member, WorkoutPlan, WorkoutSession


class Command(BaseCommand):
    help = 'Initialize and populate the OctoFit database with sample data.'

    @transaction.atomic
    def handle(self, *args, **options):
        today = date.today()

        members = [
            {
                'name': 'Avery Stone',
                'email': 'avery@octofit.local',
                'fitness_level': 'intermediate',
                'weekly_goal': 4,
                'joined_on': today - timedelta(days=90),
            },
            {
                'name': 'Jordan Lee',
                'email': 'jordan@octofit.local',
                'fitness_level': 'beginner',
                'weekly_goal': 3,
                'joined_on': today - timedelta(days=45),
            },
            {
                'name': 'Morgan Cruz',
                'email': 'morgan@octofit.local',
                'fitness_level': 'advanced',
                'weekly_goal': 5,
                'joined_on': today - timedelta(days=120),
            },
        ]

        goals = {
            'avery@octofit.local': {
                'title': 'Monthly cardio streak',
                'target_value': 12,
                'current_value': 8,
                'unit': 'sessions',
                'deadline': today + timedelta(days=21),
            },
            'jordan@octofit.local': {
                'title': 'Consistency ramp-up',
                'target_value': 10,
                'current_value': 5,
                'unit': 'sessions',
                'deadline': today + timedelta(days=30),
            },
            'morgan@octofit.local': {
                'title': 'Calorie burn milestone',
                'target_value': 8000,
                'current_value': 6200,
                'unit': 'kcal',
                'deadline': today + timedelta(days=14),
            },
        }

        plans = {
            'avery@octofit.local': {
                'title': 'Balanced Performance',
                'focus_area': 'strength + cardio',
                'difficulty': WorkoutPlan.Difficulty.INTERMEDIATE,
                'sessions_per_week': 4,
                'duration_minutes': 50,
            },
            'jordan@octofit.local': {
                'title': 'Starter Momentum',
                'focus_area': 'habit building',
                'difficulty': WorkoutPlan.Difficulty.BEGINNER,
                'sessions_per_week': 3,
                'duration_minutes': 35,
            },
            'morgan@octofit.local': {
                'title': 'Peak Conditioning',
                'focus_area': 'hiit + endurance',
                'difficulty': WorkoutPlan.Difficulty.ADVANCED,
                'sessions_per_week': 5,
                'duration_minutes': 60,
            },
        }

        sessions = {
            'avery@octofit.local': [
                ('Tempo Run', today - timedelta(days=2), 45, 420, WorkoutSession.Status.COMPLETED),
                ('Upper Body Strength', today + timedelta(days=1), 50, 0, WorkoutSession.Status.PLANNED),
            ],
            'jordan@octofit.local': [
                ('Intro Mobility', today - timedelta(days=1), 30, 180, WorkoutSession.Status.COMPLETED),
                ('Core Basics', today + timedelta(days=2), 35, 0, WorkoutSession.Status.PLANNED),
            ],
            'morgan@octofit.local': [
                ('VO2 Max Intervals', today - timedelta(days=3), 55, 610, WorkoutSession.Status.COMPLETED),
                ('Long Endurance Ride', today + timedelta(days=3), 75, 0, WorkoutSession.Status.PLANNED),
            ],
        }

        created_members = 0
        created_goals = 0
        created_plans = 0
        created_sessions = 0

        for member_data in members:
            member, member_created = Member.objects.update_or_create(
                email=member_data['email'],
                defaults=member_data,
            )
            created_members += int(member_created)

            goal_defaults = goals[member.email] | {'member': member}
            _, goal_created = Goal.objects.update_or_create(
                member=member,
                title=goal_defaults['title'],
                defaults=goal_defaults,
            )
            created_goals += int(goal_created)

            plan_defaults = plans[member.email] | {'member': member}
            plan, plan_created = WorkoutPlan.objects.update_or_create(
                member=member,
                title=plan_defaults['title'],
                defaults=plan_defaults,
            )
            created_plans += int(plan_created)

            for title, scheduled_for, duration, calories, status in sessions[member.email]:
                _, session_created = WorkoutSession.objects.update_or_create(
                    member=member,
                    title=title,
                    scheduled_for=scheduled_for,
                    defaults={
                        'plan': plan,
                        'duration_minutes': duration,
                        'calories_burned': calories,
                        'status': status,
                        'notes': 'Seeded by init_populate_octofit_db.',
                    },
                )
                created_sessions += int(session_created)

        self.stdout.write(
            self.style.SUCCESS(
                'OctoFit database initialized: '
                f'{Member.objects.count()} members, '
                f'{Goal.objects.count()} goals, '
                f'{WorkoutPlan.objects.count()} plans, '
                f'{WorkoutSession.objects.count()} sessions '
                f'({created_members}/{created_goals}/{created_plans}/{created_sessions} newly created).'
            )
        )