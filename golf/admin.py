from django.contrib import admin
from golf.models import Golfer, GolfCourse
# Register your models here.
admin.site.register([Golfer, GolfCourse])


