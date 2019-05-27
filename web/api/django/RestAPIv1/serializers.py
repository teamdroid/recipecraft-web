from rest_framework import serializers

from RestAPIv1.models import Recipe, RecipeIngredient, Ingredient, Instruction, ReportMessage, GoogleUser, \
    UserFavoriteRecipe


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


class ReportMessageSerializer(serializers.ModelSerializer):
    """Serializer for /report/ view"""
    email = serializers.EmailField(max_length=100, allow_null=False)
    message = serializers.CharField(allow_blank=False, allow_null=False)

    class Meta:
        model = ReportMessage
        fields = ('name', 'email', 'message')


class UserFavoriteRecipeWriteSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)

    class Meta:
        model = UserFavoriteRecipe
        fields = ('id', 'recipe')


class UserFavoriteRecipeReadSerializer(serializers.ModelSerializer):
    recipe = serializers.IntegerField(source='recipe.id_recipe')

    class Meta:
        model = UserFavoriteRecipe
        fields = ('recipe',)


class GoogleUserWriteSerializer(serializers.ModelSerializer):
    favorite_recipes = UserFavoriteRecipeWriteSerializer(many=True)

    class Meta:
        model = GoogleUser
        fields = ('uid', 'first_name', 'last_name', 'email', 'favorite_recipes')


class GoogleUserReadSerializer(serializers.ModelSerializer):
    favorite_recipes = UserFavoriteRecipeReadSerializer(many=True)

    class Meta:
        model = GoogleUser
        fields = ('uid', 'first_name', 'last_name', 'email', 'favorite_recipes')

    def create(self, validated_data):
        favorite_recipes_data = validated_data.pop('favorite_recipes')
        google_user = GoogleUser.objects.create(**validated_data)

        try:
            for item in favorite_recipes_data:
                UserFavoriteRecipe.objects.create(google_user=google_user, recipe_id=item['recipe']['id_recipe'])
        except:
            google_user.delete()
            raise
        return google_user


class GoogleUserUpdateRecipesSerializer(serializers.ModelSerializer):
    favorite_recipes = UserFavoriteRecipeReadSerializer(many=True)

    class Meta:
        model = GoogleUser
        fields = ('favorite_recipes',)

    def update(self, instance, validated_data):
        favorite_recipes_data = validated_data.get('favorite_recipes')

        for item in favorite_recipes_data:
            UserFavoriteRecipe.objects.create(google_user=instance, recipe_id=item['recipe']['id_recipe'])

        return instance


class GoogleUserDeleteRecipesSerializer(serializers.ModelSerializer):
    favorite_recipes = UserFavoriteRecipeReadSerializer(many=True)

    class Meta:
        model = GoogleUser
        fields = ('favorite_recipes',)

    def update(self, instance, validated_data):
        favorite_recipes_data = validated_data.get('favorite_recipes')

        for item in favorite_recipes_data:
            temp = UserFavoriteRecipe.objects.filter(recipe_id=item['recipe']['id_recipe'])
            if temp:
                temp.delete()

        return instance
