from django.shortcuts import render
from django.http import HttpResponse
import datetime

def homepage_view(request):
    now = datetime.datetime.now()

    context_dict = {'current_date': now}

    return render(request, 'index.html', context_dict)

def temp_view(request):
	now = datetime.datetime.now()

	context_dict = {'current_date': now}

	return render(request, 'temp.html', context_dict)