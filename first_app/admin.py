from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(CommentForm)
admin.site.register(Art)
admin.site.register(Word)
admin.site.register(Note)
admin.site.register(Consultant)
admin.site.register(Task)
