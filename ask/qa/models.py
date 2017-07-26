from django.db import models
import django.contrib.auth.models as auth

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255, null=True)
    text =models.TextField(null=True)
    added_at = models.DateField(null=True)
    rating= models.IntegerField(null=True)
    author = models.ForeignKey(auth.User, related_name='+')
    likes =models.ManyToManyField(auth.User, related_name='+')
#    objects = QuestionManager()
    class Meta:
        get_latest_by="added_at"

class Answer:
    text=models.TextField(null=True)
    added_at=models.DateField(null=True)
    question= models.ForeignKey(Question, related_name='+')
    author=models.ForeignKey(auth.User, related_name='+')


class QuestionManager:
    def new(self):
        return Question.objects.latest()
    def popular(self):
        return Question.objects.order_by('rating')