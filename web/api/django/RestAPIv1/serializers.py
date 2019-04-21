from rest_framework import serializers

from RestAPIv1.models import Recipe, RecipeIngredient, Ingredient, Instruction


class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ('id_instruction', 'title_ru')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id_ingredient', 'title_ru')


class RecipeIngredientSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='ingredient.id_ingredient')
    ingredient_text = serializers.ReadOnlyField(source='ingredient.title_ru')
    id_unit_measure = serializers.ReadOnlyField(source='unit_measure.id_unit_measure')
    measure_title = serializers.ReadOnlyField(source='unit_measure.title_ru')

    class Meta:
        model = RecipeIngredient
        fields = ('id',
                  'ingredient_text',
                  'amount',
                  'id_unit_measure',
                  'measure_title')


class RecipeSerializer(serializers.ModelSerializer):
    """Main serializer for /getRecipes/ view"""
    recipe_ingredients = RecipeIngredientSerializer(many=True)
    instructions = InstructionSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('id_recipe',
                  'title_ru',
                  'time',
                  'image',
                  'url_source',
                  'portion',
                  'type',
                  'recipe_ingredients',
                  'instructions')
