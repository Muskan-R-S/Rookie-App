from django.contrib import admin
from .models import Job, Candidate, User, Mandate

# Register your models here.

admin.site.register(User)
admin.site.register(Job)
admin.site.register(Candidate)
admin.site.register(Mandate)
