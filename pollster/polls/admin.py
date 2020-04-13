from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# Register models at the admin module
# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.site_header = 'Polls Admin'
admin.site.site_title = 'Polls Admin Area'
admin.site.index_title = 'Welcome to Polls Admin Area'
# Options for inline editing of model instances.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                'fields': ['question_text']
            }
        ),
        (
            'Date Information',
            {
                'fields': ['pub_date'],
                'classes': ['collapse']
            }
        ),
    ]

    inlines = (ChoiceInline,)


admin.site.register(Question, QuestionAdmin)
