from django.db import models
from django.utils import timezone

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    def __str__(self):
        return self.title


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)