from django.contrib import admin
from .models import Actor, Movie, Review
# Register your models here.

class ActorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

admin.site.register(Actor, ActorAdmin)
admin.site.register(Movie)
admin.site.register(Review)