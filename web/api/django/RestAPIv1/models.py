from django.db import models


class Ingredient(models.Model):
    id_ingredient = models.AutoField(db_column='idIngredient', primary_key=True)
    title_en = models.TextField(blank=True, null=True)
    title_ru = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients'


class Instruction(models.Model):
    id_instruction = models.AutoField(db_column='idInstruction', primary_key=True)
    title_ru = models.TextField(blank=True, null=True)
    title_en = models.TextField(blank=True, null=True)
    recipe = models.ForeignKey('Recipe',
                               models.CASCADE,
                               related_name='instructions',
                               db_column='idRecipe',
                               blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instruction'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe',
                               on_delete=models.CASCADE,
                               related_name='recipe_ingredients',
                               db_column='idRecipe')
    ingredient = models.ForeignKey('Ingredient',
                                   on_delete=models.CASCADE,
                                   related_name='unit',
                                   db_column='idIngredient')
    amount = models.FloatField(blank=True, null=True)
    unit_measure = models.ForeignKey('UnitMeasure', models.CASCADE, db_column='idUnitMeasure')

    class Meta:
        managed = False
        db_table = 'recipe_ingredients'


class RecipeType(models.Model):
    recipe = models.ForeignKey('Recipe', models.CASCADE, db_column='idRecipe')
    type = models.ForeignKey('TypeRecipe', models.CASCADE, db_column='idType')

    class Meta:
        managed = False
        db_table = 'recipe_types'


class Recipe(models.Model):
    id_recipe = models.AutoField(db_column='idRecipe', primary_key=True)
    title_ru = models.CharField(max_length=100, blank=True, null=True)
    title_en = models.CharField(max_length=100, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    portion = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    url_source = models.CharField(max_length=100, blank=True, null=True)
    ingredients = models.ManyToManyField('Ingredient',
                                         related_name='recipes',
                                         related_query_name='recipes',
                                         through='RecipeIngredient',
                                         through_fields=('recipe', 'ingredient'))

    class Meta:
        managed = False
        db_table = 'recipes'


class ReportMessage(models.Model):
    id_report = models.AutoField(db_column='idReport', primary_key=True)
    date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_message'


class TypeRecipe(models.Model):
    id_type = models.AutoField(db_column='idType', primary_key=True)
    title_ru = models.CharField(max_length=100, blank=True, null=True)
    title_en = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_recipe'


class UnitMeasure(models.Model):
    id_unit_measure = models.AutoField(db_column='idUnitMeasure', primary_key=True)
    title_ru = models.CharField(max_length=100, blank=True, null=True)
    title_en = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unit_measure'
