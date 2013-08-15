from classroom.models import Period

def load_context(request):
    periods = Period.objects.all()
    return {'periods':periods}