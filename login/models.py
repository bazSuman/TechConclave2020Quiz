from django.db import models
from django.contrib.auth.models import User


class QuizQA(models.Model):
    round_choices = (
        ('Round 1', 'Round 1'),
        ('Round 2', 'Round 2'),
        ('Finale', 'Finale')
    )

    group_choices = (
        ('Group A', 'Group A'),
        ('Group B', 'Group B'),
        ('Group C', 'Group C'),
        ('Group D', 'Group D'),
        ('Group E', 'Group E'),
        ('Group F', 'Group F'),
        ('Group G', 'Group G'),
        ('Group H', 'Group H'),
        ('Group I', 'Group I'),
        ('Group J', 'Group J'),
    )

    question_category_choices = (
        ('Recents', 'Recents'),
        ('Sports', 'Sports'),
        ('Tech', 'Tech'),
        ('Geography', 'Geography'),
        ('GK', 'GK'),
    )

    round = models.CharField('round', choices = round_choices, max_length = 55)
    group = models.CharField('group', choices = group_choices, max_length = 55)
    category = models.CharField('category', choices = question_category_choices, max_length = 55)
    question = models.CharField('question', max_length=125)
    answer = models.CharField('answer', max_length=125)

    def __str__(self):
        return self.question


class GrandFinale(models.Model):
    round_choices = (
        ('General Round', 'General ROund'),
        ('Buzzer Round', 'Buzzer Round'),
        ('Risk Round', 'Risk Round'),
    )

    question_category_choices = (
        ('Recents', 'Recents'),
        ('Sports', 'Sports'),
        ('Tech', 'Tech'),
        ('Geography', 'Geography'),
        ('GK', 'GK'),
        ('Buzzer', 'Buzzer'),
        ('Platinum', 'Platinum'),
        ('Gold', 'Gold'),
        ('Silver', 'Silver')
    )

    round = models.CharField('round', choices = round_choices, max_length = 55)
    category = models.CharField('category', choices = question_category_choices, max_length = 55)
    question = models.CharField('question', max_length=125)
    image_question = models.ImageField(upload_to='quiz_images', blank=True, null=True)
    answer = models.CharField('answer', max_length=125)

    def __str__(self):
        return self.question



class LoggedIn(models.Model):
    name = models.CharField('name', max_length=120)
    is_logged_in = models.BooleanField(blank= True, default=False)

    def __str__(self):
        return self.name
