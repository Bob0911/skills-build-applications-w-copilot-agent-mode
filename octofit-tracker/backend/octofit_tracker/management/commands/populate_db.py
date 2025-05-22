
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email='student1@octofit.com', name='John Doe')
        user2 = User.objects.create(email='student2@octofit.com', name='Jane Smith')
        user3 = User.objects.create(email='student3@octofit.com', name='Emily Davis')

        # Create test teams
        team1 = Team.objects.create(name='Team A')
        team2 = Team.objects.create(name='Team B')
        team1.members.add(user1, user2)
        team2.members.add(user3)

        # Create test activities
        Activity.objects.create(user=user1, type='Running', duration=25)
        Activity.objects.create(user=user2, type='Cycling', duration=40)
        Activity.objects.create(user=user3, type='Swimming', duration=50)

        # Create test leaderboard
        Leaderboard.objects.create(team=team1, score=120)
        Leaderboard.objects.create(team=team2, score=180)

        # Create test workouts
        Workout.objects.create(name='Cardio Blast', description='High-energy cardio session')
        Workout.objects.create(name='Strength Training', description='Build muscle and endurance')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
