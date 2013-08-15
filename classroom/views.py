from django.shortcuts import render
from classroom.models import *

def index(request):
    latestAnnouncements = Announcement.objects.all().order_by('-createtime')[:5]
    latestAssignments = Assignment.objects.all().order_by('-createtime')[:6]
    latestTests = Test.objects.all().order_by('-createtime')[:5]
    
    context = {'latestAnnouncements' : latestAnnouncements,
               'latestAssignments': latestAssignments, 
               'latestTests' : latestTests}
    
    return render(request, 'classroom/index.html', context)