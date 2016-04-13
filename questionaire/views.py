from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import *

def index(request):
    questionaires = Questionaire.objects.order_by('updated_at')
    context = {
        'questionaires': questionaires
    }
    return render(request, 'questionaire/index.html', context)

def detail(request, questionaire_id):
    if request.user.is_authenticated():
        questionaire = get_object_or_404(Questionaire, pk=questionaire_id)
        return render(request, 'questionaire/index.html',
        {
            'questionaire': questionaire
        })
    else:
        return redirect('/login')
