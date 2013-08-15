from django.shortcuts import get_object_or_404, render
from classroom.models import *
from datetime import date, timedelta, datetime

def index(request):    
    return render(request, 'classroom/index.html')

def period(request, period_id):
    time = datetime.today() - timedelta(days=1)
    
    period = get_object_or_404(Period, pk=period_id)
    announcements = Announcement.objects.filter(period_id=period_id).order_by('-createtime')[:10]                            
    assignments = Assignment.objects.filter(period_id=period_id).filter(due_date__gt=time).order_by('due_date')[:10]
    tests = Test.objects.filter(period_id=period_id).order_by('-test_date')[:10]
    
    context = {
                'period':period,
                'announcements':announcements,
                'assignments':assignments,
                'tests':tests
            }
    
    return render(request, 'classroom/period.html', context)

def contact(request):
    return render(request, 'classroom/contact.html')
                      
    