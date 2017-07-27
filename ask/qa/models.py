from django.db import models
import django.contrib.auth.models as auth

# Create your models here.
class Question(models.Model):
    title = models.CharField(default="",max_length=255)
    text =models.TextField(default="")
    added_at = models.DateField(null=True)
    rating= models.IntegerField(default=0)
    author = models.ForeignKey(auth.User, null=True, related_name='+')
    likes =models.ManyToManyField(auth.User, related_name='+')
#    objects = QuestionManager()
    class Meta:
        get_latest_by="added_at"

class Answer:
    text=models.TextField(default="")
    added_at=models.DateField(null=True)
    question= models.ForeignKey(Question, null=True, related_name='+')
    author=models.ForeignKey(auth.User, null=True, related_name='+')


class QuestionManager:
    def new(self):
        return Question.objects.latest()
    def popular(self):
        return Question.objects.order_by('rating')