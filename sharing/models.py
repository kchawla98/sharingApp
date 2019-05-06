from django.db import models

class Subject(models.Model):
    owner = models.CharField(max_length=250)
    subject_title = models.CharField(max_length=100)

class Video(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    video_title= models.CharField(max_length=100)



