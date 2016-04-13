from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Questionaire(models.Model):
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(editable=False);
    updated_at = models.DateTimeField(editable=False);

    def __str__(self):
        return self.title;

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Questionaire, self).save(*args, **kwargs)

class Question(models.Model):
    QUESTION_TYPES = (
        ('TextQuestion', 'Text Question'),
        ('YesNoQuestion', 'Yes/No Question'),
        ('MultipleChoiceQuestion', 'Multiple Choice Question'),
    )
    questionaire = models.ForeignKey(Questionaire, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=512, unique=True)
    question_type = models.CharField(max_length=128, choices=QUESTION_TYPES)
    version = models.IntegerField(default=1, editable=False)
    created_at = models.DateTimeField(editable=False);
    updated_at = models.DateTimeField(editable=False);

    def __str__(self):
        return self.question_text;

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Question, self).save(*args, **kwargs)

class TextQuestion(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)

class YesNoQuestion(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)

class MultipleChoiceQuestion(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answers = models.CharField(max_length=512)

class AnswerSet(models.Model):
    questionaire = models.ForeignKey(Questionaire, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False);
    updated_at = models.DateTimeField(editable=False);

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(AnswerSet, self).save(*args, **kwargs)

class Answer(models.Model):
    ANSWER_TYPES = (
        ('TextAnswer', 'Text Answer'),
        ('YesNoAnswer', 'Yes/No Answer'),
        ('MultipleChoiceAnswer', 'Multiple Choice Answer'),
    )
    answer_set = models.ForeignKey(AnswerSet, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_type = models.CharField(max_length=128, choices=ANSWER_TYPES)
    created_at = models.DateTimeField(editable=False);
    updated_at = models.DateTimeField(editable=False);

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Answer, self).save(*args, **kwargs)

class TextAnswer(models.Model):
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1028)

class YesNoAnswer(models.Model):
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)
    yes = models.BooleanField();

class MultipleChoiceAnswer(models.Model):
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)
    answers = models.CharField(max_length=512)
