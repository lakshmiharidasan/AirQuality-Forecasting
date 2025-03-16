from django.db import models

# Create your models here.
class logintbl(models.Model):
    username=models.CharField(max_length=200)
    pasword=models.CharField(max_length=200)
    utype=models.CharField(max_length=200)

class usertbl(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    mobileno=models.BigIntegerField(max_length=10)
    place=models.CharField(max_length=200)
    latitude=models.FloatField()
    longitude=models.FloatField()
    LOGIN=models.ForeignKey(logintbl,on_delete=models.CASCADE)

class feedbacktbl(models.Model):
    feedback=models.CharField(max_length=500)
    USERID=models.ForeignKey(usertbl,on_delete=models.CASCADE)
    date=models.DateField()

class experttbl(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    Post = models.CharField(max_length=100)
    mobileno = models.BigIntegerField(max_length=10)
    place = models.CharField(max_length=200)
    LOGIN = models.ForeignKey(logintbl, on_delete=models.CASCADE)


class tips_table(models.Model):
    tips=models.CharField(max_length=200)
    details=models.CharField(max_length=100)
    date=models.DateField()
    EXPERT=models.ForeignKey(experttbl,on_delete=models.CASCADE)



class dataset_table(models.Model):
    question=models.CharField(max_length=400)
    answer=models.CharField(max_length=400)
    date=models.DateField()
    EXPERT=models.ForeignKey(experttbl,on_delete=models.CASCADE)

class Solutions(models.Model):
    solution=models.CharField(max_length=200)
    date=models.DateField()
    EXPERT=models.ForeignKey(experttbl,on_delete=models.CASCADE)
class alert_table(models.Model):
    alert=models.CharField(max_length=200)
    # details=models.CharField(max_length=100)
    date=models.DateField()
