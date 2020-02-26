from django.contrib import admin

from .models import Student
from .models import Parent
from .models import SchoolIn
from .models import SchoolOut


admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(SchoolIn)
admin.site.register(SchoolOut)
