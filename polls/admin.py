from django.contrib import admin

from .models import (Choice, InfoPersonal, Journey, Part, PartQuestion,
                     Question, Questionnaire, QuestionnairePart, Response,
                     ResponseCovid)

# Register your models here.

admin.site.register(Choice)
admin.site.register(Questionnaire)
admin.site.register(Journey)
admin.site.register(Response)
admin.site.register(QuestionnairePart)
admin.site.register(PartQuestion)
admin.site.register(Part)
admin.site.register(ResponseCovid)
admin.site.register(InfoPersonal)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields': ['questionnaire']}),
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Type', {'fields': ['question_type']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
