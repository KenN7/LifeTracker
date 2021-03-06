from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from tracker.models import *
#from tracker.forms import * 
#import tracker.graph as flot

# Create your views here.

@login_required
def tracker_page(request):
    user = User.objects.get(username=request.user)
    pad = user.pad.name
    notifications = user.events.order_by('-date')[:6]
    todos = user.todo.filter(done=False)
    daily = user.daily_events()
    tomorrow = user.tomorrow_events()
    later = user.later_events()
    
    c = {
            'pad': pad,
            'notifications': notifications,
            'todos': todos,
            'daily': daily,
            'tomorrow': tomorrow,
            'later': later,

            }
    return render(request, 'tracker_page.html', c)

@login_required
def door_opener(request):
    #if connected
    if True:
    #send message to electronic card to open
        messages.success(request, 'Door opened')
    else:
        messages.warning(request, 'Opening failed')
    return redirect('tracker-page')

