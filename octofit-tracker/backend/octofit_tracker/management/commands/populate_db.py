from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email='user1@octofit.com', name='Alice')
        user2 = User.objects.create(email='user2@octofit.com', name='Bob')
        user3 = User.objects.create(email='user3@octofit.com', name='Charlie')

        # Create test teams
        team1 = Team.objects.create(name='Team Octo')
        team2 = Team.objects.create(name='Team Fit')
        team1.members.add(user1, user2)
        team2.members.add(user3)

        # Create test activities
        Activity.objects.create(user=user1, type='Running', duration=30)
        Activity.objects.create(user=user2, type='Cycling', duration=45)
        Activity.objects.create(user=user3, type='Swimming', duration=60)

        # Create test leaderboard
        Leaderboard.objects.create(team=team1, score=150)
        Leaderboard.objects.create(team=team2, score=200)

        # Create test workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session')
        Workout.objects.create(name='HIIT', description='High-intensity interval training')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
