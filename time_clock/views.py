from django.shortcuts import render, redirect
from datetime import datetime


# Create your views here.
def root(request):
    return redirect('/time_display')


def time_display(request):
    context = {
        'date' : datetime.now().strftime('%B %d, %Y'),
        'time' : datetime.now().strftime('%I:%M:%S %p')
    }
    return render(request, 'time_display.html', context)