from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    # relationship name
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # ForeignKey Class is default to many_to_one
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # relationship name
    def __str__(self):
        return self.choice_text
