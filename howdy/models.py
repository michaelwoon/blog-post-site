from django.db import models
#from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    date = models.DateField()
    text = models.TextField()
    relatedOne = models.ForeignKey('self',on_delete=models.CASCADE,related_name='first_article',null=True,blank=True)
    relatedTwo = models.ForeignKey('self',on_delete=models.CASCADE,related_name='second_article',null=True,blank=True)
    relatedThree = models.ForeignKey('self',on_delete=models.CASCADE,related_name='third_article',null=True,blank=True)
    postNum = models.IntegerField(default=1)
    #comments = ArrayField(models.CharField(max_length=200),default={})
