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
    createtime = models.DateTimeField("Date Created",auto_now_add = True)
    def __unicode__(self):
        return self.name

class Assignment (models.Model):
    period = models.ForeignKey(Period)
    name = models.CharField(max_length=200)
    createtime = models.DateTimeField("Date Created", auto_now_add = True)
    due_date = models.DateTimeField("Due Date")
    content = models.TextField()
    def __unicode__(self):
        return self.name
    
class Test (models.Model):
    period = models.ForeignKey(Period)
    name = models.CharField(max_length=200)
    createtime = models.DateTimeField("Date Created", auto_now_add = True)
    test_date = models.DateTimeField("Test Date")
    def __unicode__(self):
        return self.name