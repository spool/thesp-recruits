from django.db import models
from oxford import COLLEGE_CHOICES

class Recruit(models.Model):

    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    email       = models.EmailField()
    institution = models.CharField(max_length=100, default="Oxford", blank=True, null=True)
    college     = models.IntegerField(choices=COLLEGE_CHOICES, blank=True, null=True)
    acting      = models.BooleanField(default=False)
    production  = models.BooleanField(default=False)
    tech        = models.BooleanField(default=False)
    musician    = models.BooleanField(default=False)
    tickets     = models.BooleanField(default=False)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
