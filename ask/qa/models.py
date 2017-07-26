from django.db import models
import django.contrib.auth.models as auth

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text =models.TextField()
    added_at = models.DateField()
    rating= models.IntegerField()
    author = models.ForeignKey(auth.User)
    likes =models.ManyToManyField(auth.User)
#    objects = QuestionManager()
    class Meta:
        get_latest_by="added_at"

class Answer:
    text=models.TextField()
    added_at=models.DateField()
    question= models.ForeignKey(Question)
    author=models.ForeignKey(auth.User)


class QuestionManager:
    def new(self):
        return Question.objects.latest()
    def popular(self):
        return Question.objects.order_by('rating')