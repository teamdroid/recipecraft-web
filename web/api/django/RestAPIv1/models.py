from django.db import models


class Ingredient(models.Model):
    id_ingredient = models.AutoField(db_column='idIngredient', primary_key=True)
    title_en = models.TextField(blank=True, null=True)
    title_ru = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title_ru.__str__()

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

    def __str__(self):
        return "Инструкция #" + self.id_instruction.__str__()

    class Meta:
        managed = False
        db_table = 'instruction'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe',
                               on_delete=models.CASCADE,
                               related_name='ingredients',
                               db_column='idRecipe')
    ingredient = models.ForeignKey('Ingredient',
                                   on_delete=models.CASCADE,
                                   related_name='unit',
                                   db_column='idIngredient')
    amount = models.FloatField(blank=True, null=True)
    unit_measure = models.ForeignKey('UnitMeasure', models.CASCADE, db_column='idUnitMeasure')

    def __str__(self):
        return "Ингредиент #" + self.id.__str__()

    class Meta:
        managed = False
        db_table = 'recipe_ingredients'


class Recipe(models.Model):
    id_recipe = models.AutoField(db_column='idRecipe', primary_key=True)
    title_ru = models.CharField(max_length=100, blank=True, null=True)
    title_en = models.CharField(max_length=100, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    portion = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    url_source = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        managed = False
        db_table = 'recipes'


class ReportMessage(models.Model):
    id_report = models.AutoField(db_column='idReport', primary_key=True)
    date = models.DateField(blank=True, null=True, auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=False, null=False)

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

    def __str__(self):
        return self.title_ru

    class Meta:
        managed = False
        db_table = 'unit_measure'


class GoogleUser(models.Model):
    uid = models.CharField(max_length=50, primary_key=True, blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=False, null=False)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class UserFavoriteRecipe(models.Model):
    google_user = models.ForeignKey(GoogleUser, related_name='favorite_recipes', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("google_user", "recipe")

    def __str__(self):
        return self.recipe.title_ru

# TODO:refactor __str__ methods
