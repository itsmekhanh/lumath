from django.shortcuts import get_object_or_404, render
from classroom.models import *
from datetime import date, timedelta, datetime

def index(request):    
    return render(request, 'classroom/index.html')

def period(request, period_id):
    time = datetime.today() - timedelta(days=1)
    
    period = get_object_or_404(Period, pk=period_id)
    announcements = Announcement.objects.filter(period_id=period_id).reverse().order_by('-createtime')[:5]                            
    assignments = Assignment.objects.filter(period_id=period_id).reverse().order_by('-due_date')[:5]
    tests = Test.objects.filter(period_id=period_id).reverse().order_by('-test_date')[:5]
    
    context = {
                'period':period,
                'announcements':announcements,
                'assignments':assignments,
                'tests':tests
            }
    
    return render(request, 'classroom/period.html', context)

def contact(request):
    return render(request, 'classroom/contact.html')

def assignments(request, period_id):
    period = get_object_or_404(Period, pk=period_id)
    assignments = Assignment.objects.filter(period_id=period_id).order_by('due_date')
    context = {
               'assignments': assignments,
               'period':period
    }
    return render(request, 'classroom/assignments.html', context)

def announcements(request, period_id):
    period = get_object_or_404(Period, pk=period_id)
    announcements = Announcement.objects.filter(period_id=period_id).order_by('createtime')
    
    context = {
               'announcements': announcements,
               'period':period
    }
    return render(request, 'classroom/announcements.html', context)

def tests(request, period_id):
    period = get_object_or_404(Period, pk=period_id)
    tests = Test.objects.filter(period_id=period_id).order_by('test_date')
    
    context = {
               'tests': tests,
               'period':period
    }
    return render(request, 'classroom/tests.html', context)


                      
    