from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User.objects.create(email='captainamerica@marvel.com', name='Captain America', team='marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc'),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy'),
            Workout.objects.create(name='Running', description='Run 5km', difficulty='medium'),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Pushups', duration=10, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Pushups', duration=15, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Running', duration=25, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[1], score=90, rank=2)
        Leaderboard.objects.create(user=users[2], score=80, rank=3)
        Leaderboard.objects.create(user=users[3], score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
