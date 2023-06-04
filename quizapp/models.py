from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(unique = True, null = True)
    bio = models.TextField(
        default = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    )
    avatar = models.ImageField(null = True, default = "captain-america.jpg", verbose_name = 'Profile pic', upload_to = 'images/')

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username


class Quiztopic(models.Model):
    topics = models.CharField(unique = True, max_length = 100)
    image = models.ImageField(default = "captain-america.jpg", upload_to = 'images/')
    def __str__(self) -> str:
        return self.topics


class Subtopic(models.Model):
    topic = models.ForeignKey(Quiztopic, on_delete = models.CASCADE)
    sub_topic = models.CharField(unique = True, max_length = 100)
    image = models.ImageField(default = "captain-america.jpg", upload_to = 'images/')

    def __str__(self) -> str:
        return self.sub_topic


class Quizquestion(models.Model):
    sub_topic_name = models.ForeignKey(Subtopic, on_delete = models.CASCADE)
    question = models.CharField(unique = True, max_length = 500)
    option_1 = models.CharField(max_length = 100)
    option_2 = models.CharField(max_length = 100)
    option_3 = models.CharField(max_length = 100)
    option_4 = models.CharField(max_length = 100)

    correct_answer = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.question


class Score(models.Model):
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE, null = True)
    sub_topic = models.ForeignKey(Subtopic, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now = True)
    no_of_correctanswers = models.IntegerField(default = 0)
    no_of_questions = models.IntegerField(default = 0)
    score = models.FloatField(default = 0)

    def __str__(self) -> str:
        return f'{self.no_of_correctanswers}/{self.no_of_questions}'