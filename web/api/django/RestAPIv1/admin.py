from django.contrib import admin
from django.db import models
from django.forms import widgets
from easy_select2 import select2_modelform

from RestAPIv1.models import Recipe, RecipeIngredient, Ingredient, Instruction, UnitMeasure


class InstructionInline(admin.TabularInline):
    model = Instruction
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': widgets.Textarea(attrs={'rows': 6, 'cols': 50})}
    }


class IngredientRecipeInline(admin.TabularInline):
    model = RecipeIngredient
    form = select2_modelform(model)
    extra = 1


@admin.register(UnitMeasure)
class RecipeAdmin(admin.ModelAdmin):
    fields = ['title_ru', 'title_en']


@admin.register(Ingredient)
class RecipeAdmin(admin.ModelAdmin):
    fields = ['title_ru', 'title_en']
    search_fields = ['title_ru']
    formfield_overrides = {
        models.TextField: {'widget': widgets.TextInput}
    }


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ['title_ru', 'title_en', 'type', 'portion', 'time', 'url_source', 'image']
    list_filter = ['type', 'url_source']
    search_fields = ['title_ru', 'type']
    inlines = [IngredientRecipeInline, InstructionInline]
    formfield_overrides = {
        models.TextField: {'widget': widgets.TextInput(attrs={'size': '40'})}
    }
