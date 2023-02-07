from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Quiztopic)
admin.site.register(Subtopic)
admin.site.register(Quizquestion)
admin.site.register(Score)