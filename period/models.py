from django.db import models

class Period (models.Model):
    description = models.TextField()
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Announcement (models.Model):
    period = models.ForeignKey(Period)
    name = models.CharField(max_length=200)
    content = models.TextField()
    def __unicode__(self):
        return self.name

class Assignment (models.Model):
    period = models.ForeignKey(Period)
    name = models.CharField(max_length=200)
    content = models.TextField()
    def __unicode__(self):
        return self.name