from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User,related_name='friends',blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    experience = models.IntegerField(default=0)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,related_name='receiver')

class Comment(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

class Exercise(models.Model):
    NAME_CHOICES = [
                ('Running', 'RUNNING'),
                ('Swimming', 'SWIMMING'),
                ('Biking', 'BIKING'),
                ('Walking', 'WALKING')
            ]
    SUFFIX_CHOICES = [
            ('Repetitions', 'repetitions'),
            ('Minutes', 'minutes'),
            ('Hours', 'hours'),
            ('Laps', 'laps')
        ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    finished = models.BooleanField(default=False)
    duration = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.CharField(max_length=20)
    name = models.CharField(max_length=50, choices=NAME_CHOICES)
    exp = models.IntegerField(default=100)
    duration_suffix = models.CharField(max_length=50, choices=SUFFIX_CHOICES)

    def get_absolute_url(self):
        return reverse('gamifi:activity-log')

class ExerciseChoice(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField()
    image_url=models.CharField(max_length=100)
    category=models.CharField(max_length=20)



# class AerobicExercise(Exercise):
#     NAME_CHOICES = [
#         ('Running', 'RUNNING'),
#         ('Swimming', 'SWIMMING'),
#         ('Biking', 'BIKING'),
#         ('Walking', 'WALKING')
#     ]
#     SUFFIX_CHOICES = [
#         ('Repetitions', 'repetitions'),
#         ('Minutes', 'minutes'),
#         ('Hours', 'hours'),
#         ('Laps', 'laps')
#     ]
#     name = models.CharField(max_length=50, choices=NAME_CHOICES)
#     exp = models.IntegerField(default=100)
#     duration_suffix = models.CharField(max_length=50,choices =SUFFIX_CHOICES)
#
#     @property
#     def type(self):
#         "Returns the exercise type(aerobic)."
#         return 'Aerobic'
#
# class StrengthExercise(Exercise):
#     NAME_CHOICES = [
#         ('Push-Ups', 'PUSH-UPS'),
#         ('Deadlift', 'DEADLIFT'),
#         ('Pull-ups', 'PULL-UPS')
#     ]
#
#     SUFFIX_CHOICES = [
#         ('Repetitions', 'repetitions'),
#         ('Sets', 'sets'),
#         ('Minutes', 'minutes')
#     ]
#     name = models.CharField(max_length=50, choices=NAME_CHOICES)
#     exp = models.IntegerField(default=217)
#     duration_suffix = models.CharField(max_length=50,choices =SUFFIX_CHOICES)
#
#     @property
#     def type(self):
#         "Returns the exercise type(aerobic)."
#         return 'Strength'
#
# class FlexibilityExercise(Exercise):
#     NAME_CHOICES = [
#         ('Lunges', 'LUNGES'),
#         ('Butterfly Stretch', 'BUTTERFLY STRETCH'),
#         ('Yoga', 'YOGA')
#     ]
#     SUFFIX_CHOICES = [
#         ('Repetitions', 'repetitions'),
#         ('Sets', 'sets'),
#         ('Minutes', 'minutes')
#     ]
#     name = models.CharField(max_length=50, choices=NAME_CHOICES)
#     exp = models.IntegerField(default=50)
#     duration_suffix = models.CharField(max_length=50,choices =SUFFIX_CHOICES)
#
#     @property
#     def type(self):
#         "Returns the exercise type(aerobic)."
#         return 'Flexibility'


