from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import *

def index(request):
    questionaires = Questionaire.objects.order_by('created_at')
    context = {
        'questionaires': questionaires
    }
    return render(request, 'questionaire/index.html', context)

def detail(request, questionaire_id):
    if request.user.is_authenticated():
        questionaire = get_object_or_404(Questionaire, pk=questionaire_id)

        questions = questionaire.question_set.order_by('created_at')

        # Create answer_set for first time visit
        try:
            answer_set = AnswerSet.objects.get(
            user_id = request.user.id,
            questionaire_id = questionaire.id)
        except ObjectDoesNotExist:
            answer_set = AnswerSet()
            answer_set.user = request.user
            answer_set.questionaire = questionaire
            answer_set.save()

        return render(request, 'questionaire/detail.html',
        {
            'questionaire': questionaire,
            'questions': questions
        })
    else:
        return redirect('/login')

def question_detail(request, questionaire_id, question_id):
    if not request.user.is_authenticated():
        return redirect('/login')

    questionaire = get_object_or_404(Questionaire, pk=questionaire_id)
    question = get_object_or_404(Question, pk=question_id)
    # Create answer_set for first time visit
    answer_set = None
    try:
        answer_set = AnswerSet.objects.get(
            user_id = request.user.id,
            questionaire_id = question.questionaire.id
        )
    except ObjectDoesNotExist:
        answer_set = AnswerSet()
        answer_set.user = request.user
        answer_set.questionaire = questionaire
        answer_set.save()

    answer = None
    try:
        answer = answer_set.answer_set.get(
            question = question.id
        )
    except ObjectDoesNotExist:
        pass

    # Special case for multiplchoice, this should be moved to a separate form
    multiple = {}
    if question.question_type == "MultipleChoiceQuestion":
        choices_list = question.multiplechoicequestion.answers.split(',')
        for choice in choices_list:
            multiple[choice] = 0
        if answer:
            answers = answer.multiplechoiceanswer.answers.split(',')
            for answer in answers:
                multiple[answer] = 1
        
    question_type = question.question_type
    return render(request, "question/%s.html" % question_type.lower(),
    {
        'question': question,
        'answer_set': answer_set,
        'answer': answer,
        'multiple': multiple
    })

def answer(request):
    if not request.user.is_authenticated():
        return redirect('/login')

    question = get_object_or_404(Question, pk=request.POST['question_id'])
    answer_set = get_object_or_404(AnswerSet, pk=request.POST['answer_set_id'])
    try:
        answer = answer_set.answer_set.get(
            question = question.id
        )
    except ObjectDoesNotExist:
        answer = Answer()
        answer.answer_set = answer_set
        answer.question = question
        answer.answer_type = question.question_type.replace("Question", "Answer")
        answer.save()

    answer_text = request.POST['answer_text']
    answer_meta = None
    error_message = ""
    if answer.answer_type == "TextAnswer":
        answer_meta = answer.textanswer
        answer_meta.answer_text = answer_text
    elif answer.answer_type == "YesNoAnswer":
        answer_meta = answer.yesnoanswer
        if answer_text == "yes":
            answer_meta.yes = True
        elif answer_text == "no":
            answer_meta.yes = False
    elif answer.answer_type == "MultipleChoiceAnswer":
        answer_text = ",".join(request.POST.getlist('answer_text'))
        answer_meta = answer.multiplechoiceanswer
        answer_meta.answers = answer_text

    if not error_message and answer_meta:
        answer_meta.save()
        return redirect("/questionaire/%d" % question.questionaire.id)
    else:
        question_type = question.question_type
        return render(request, "question/%s.html" % question_type.lower(),
        {
            'error_message': error_message,
            'question': question,
            'answer_set': answer_set
        })
