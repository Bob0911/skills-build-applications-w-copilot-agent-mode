from djongo import models
import uuid

class User(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    # ... other fields ...

class Team(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = models.CharField(max_length=255, unique=True)
    members = models.ManyToManyField(User)
    # ... other fields ...

class Activity(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=lambda: str(uuid.uuid4()))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    # ... other fields ...

class Leaderboard(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=lambda: str(uuid.uuid4()))
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()
    # ... other fields ...

class Workout(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = models.CharField(max_length=255)
    description = models.TextField()
    # ... other fields ...