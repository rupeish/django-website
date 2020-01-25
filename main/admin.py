from django.contrib import admin
from .models import Tutorial, TutorialCategory, TutorialSeries
from tinymce.widgets import TinyMCE
from django.db import models

class TutorialAdmin(admin.ModelAdmin):

	fieldsets = [
	('Title/Date', {"fields" : ["tutorial_title","tutorial_published"]}),
	('URl', {"fields": ["tutorial_slug"]}),
	('Series', {"fields": ["tutorial_series"]}),
	('Content', {"fields": ["tutorial_content"]})
	]

	formfield_overrides = {
	models.TextField: {'widget': TinyMCE()}
	}

admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
# Register your models here.
admin.site.register(Tutorial,TutorialAdmin)