from django.db import models


class Ingredients(models.Model):
    idingredient = models.AutoField(db_column='idIngredient', primary_key=True)
    title_en = models.TextField(blank=True, null=True)
    title_ru = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients'


class Instruction(models.Model):
    idinstruction = models.AutoField(db_column='idInstruction', primary_key=True)
    title_ru = models.TextField(blank=True, null=True)
    title_en = models.TextField(blank=True, null=True)
    idrecipe = models.ForeignKey('Recipes', models.DO_NOTHING, db_column='idRecipe', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instruction'


class RecipeIngredients(models.Model):
    idrecipe = models.ForeignKey('Recipes', models.DO_NOTHING, db_column='idRecipe')
    idingredient = models.ForeignKey(Ingredients, models.DO_NOTHING, db_column='idIngredient')
    amount = models.FloatField(blank=True, null=True)
    idunitmeasure = models.ForeignKey('UnitMeasure', models.DO_NOTHING, db_column='idUnitMeasure')

    class Meta:
        managed = False
        db_table = 'recipe_ingredients'


class RecipeTypes(models.Model):
    idrecipe = models.ForeignKey('Recipes', models.DO_NOTHING, db_column='idRecipe')
    idtype = models.ForeignKey('TypeRecipe', models.DO_NOTHING, db_column='idType')

    class Meta:
        managed = False
        db_table = 'recipe_types'


class Recipes(models.Model):
    idrecipe = models.AutoField(db_column='idRecipe', primary_key=True)
    title_ru = models.CharField(max_length=100, blank=True, null=True)
    title_en = models.CharField(max_length=100, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    portion = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    url_source = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipes'


class ReportMessage(models.Model):
    idreport = models.AutoField(db_column='idReport', primary_key=True)
    date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_message'


class TypeRecipe(models.Model):
    idtype = models.AutoField(db_column='idType', primary_key=True)
    title_ru = models.CharField(max_length=100, blank=True, null=True)
    title_en = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_recipe'


class UnitMeasure(models.Model):
    idunitmeasure = models.AutoField(db_column='idUnitMeasure', primary_key=True)
    title_ru = models.CharField(max_length=100, blank=True, null=True)
    title_en = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unit_measure'
