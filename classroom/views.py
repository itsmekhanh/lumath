from django.shortcuts import get_object_or_404, render
from classroom.models import *
from datetime import datetime

def index(request):
    latestAnnouncements = Announcement.objects.all().order_by('-createtime')[:5]
    latestAssignments = Assignment.objects.all().order_by('-createtime')[:6]
    latestTests = Test.objects.all().order_by('-createtime')[:5]
    
    context = {'latestAnnouncements' : latestAnnouncements,
               'latestAssignments': latestAssignments, 
               'latestTests' : latestTests}
    
    return render(request, 'classroom/index.html')

def period(request, period_id):
    time = datetime.now()
    
    period = get_object_or_404(Period, pk=period_id)
    announcements = Announcement.objects.filter(period_id=period_id).order_by('-createtime')[:5]                            
    assignments = Assignment.objects.filter(period_id=period_id).filter(due_date__gt=time).order_by('due_date')[:10]
    tests = Test.objects.filter(period_id=period_id).order_by('-test_date')[:5]
    
    context = {
                'period':period,
                'announcements':announcements,
                'assignments':assignments,
                'tests':tests
            }
    
    return render(request, 'classroom/period.html', context)
    