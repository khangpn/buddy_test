from django.contrib import admin

from .models import *

admin.site.register(Questionaire)
admin.site.register(Question)
admin.site.register(TextQuestion)
admin.site.register(YesNoQuestion)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(Answer)
admin.site.register(TextAnswer)
admin.site.register(YesNoAnswer)
admin.site.register(MultipleChoiceAnswer)
