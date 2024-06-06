from django.contrib import admin
from .models import FoodType, Food, Comment

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('food', 'text', 'created', 'author')


admin.site.register(FoodType)
admin.site.register(Food)
