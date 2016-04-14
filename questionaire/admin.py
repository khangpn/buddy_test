from django.contrib import admin

from .models import *

class QuestionInline(admin.StackedInline):
    model = Question

class QuestionaireAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:
            form.question_type = obj.question_type
        obj.save()

admin.site.register(Questionaire, QuestionaireAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(TextQuestion)
admin.site.register(YesNoQuestion)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(AnswerSet)
admin.site.register(Answer)
admin.site.register(TextAnswer)
admin.site.register(YesNoAnswer)
admin.site.register(MultipleChoiceAnswer)
