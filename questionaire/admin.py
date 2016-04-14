from django.contrib import admin

from .models import *

def set_selected(modeladmin, request, queryset):
    queryset.update(selected = True)
set_selected.short_description = "Set selected question version"

class QuestionInline(admin.StackedInline):
    model = Question

class QuestionaireAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'version', 'index', 'selected']
    actions = [set_selected]
    def save_model(self, request, obj, form, change):
        if change:
            new_version = Question(
                question_text = obj.question_text, 
                question_type = obj.question_type, 
                index = obj.index, 
                version = obj.version + 1, 
                selected = True,
                questionaire_id = obj.questionaire.id,
            )
            new_version.save()

            obj.selected = False
            obj.save()
        else:
            questionaire = obj.questionaire
            obj.index = questionaire.size
            questionaire.size = questionaire.size + 1
            obj.save()
            questionaire.save()

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
