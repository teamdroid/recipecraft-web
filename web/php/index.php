<?php
header("Content-Type: application/json");

$mysqli = new mysqli('', '', '', '');

$mysqli->set_charset('utf8');

if ($mysqli->connect_errno) {
    echo "Error!";
    echo "\nErrorNo " . $mysqli->connect_errno . "\n";
    echo "Error: " . $mysqli->connect_error . "\n";
    exit;
}

if (!empty($_GET['lang'])) {
    if ($_GET['lang'] == "ru") {
        $sql_ingredients = "SELECT recipes.idRecipe, recipes.type as 'type', recipes.image, recipes.url_source, recipes.title_ru as 'title', recipe_ingredients.id, recipe_ingredients.idIngredient, recipes.time, recipes.portion, recipes.type, ingredients.title_ru as 'ingredientTitle', recipe_ingredients.amount, unit_measure.title_ru as 'measureTitle' FROM recipes 
                            LEFT JOIN recipe_ingredients ON recipes.idRecipe = recipe_ingredients.idRecipe LEFT JOIN ingredients ON recipe_ingredients.idIngredient = ingredients.idIngredient 
                            LEFT JOIN unit_measure ON recipe_ingredients.idUnitMeasure = unit_measure.idUnitMeasure";
        $sql_instructions = "SELECT instruction.idRecipe as 'idRecipe', instruction.idInstruction as 'idInstruction', instruction.title_ru as 'instructionTitle' FROM instruction";
//        $sql_typeRecipe = "SELECT recipes.idRecipe, recipes.title_ru as 'title', type_recipe.idType as 'idType', type_recipe.title_ru as 'typeTitle' FROM recipes
//                            LEFT JOIN recipe_types ON recipes.idRecipe = recipe_types.idRecipe
//                            LEFT JOIN type_recipe ON recipe_types.idType = type_recipe.idType";
    } else if ($_GET['lang'] == "en") {
        // language english
    } else {
        echo "Please enter correct language. For example, <b>?lang=ru</b> or <b>?lang=en</b>";
        exit;
    }
} else {
    echo "Please enter your language. For example, <b>?lang=ru</b> or <b>?lang=en</b>";
    exit;
}

//if (!$result_typeRecipe = $mysqli->query($sql_typeRecipe)) {
//    echo "Error!";
//    echo "\nQuery: " . $sql_typeRecipe . "\n";
//    echo "ErrorNo: " . $mysqli->errno . "\n";
//    echo "Error: " . $mysqli->error . "\n";
//    exit;
//}

if (!$result_ingredients = $mysqli->query($sql_ingredients)) {
    echo "Error!";
    echo "\nQuery: " . $sql_ingredients . "\n";
    echo "ErrorNo: " . $mysqli->errno . "\n";
    echo "Error: " . $mysqli->error . "\n";
    exit;
}

if (!$result_instructions = $mysqli->query($sql_instructions)) {
    echo "Error!";
    echo "\nQuery: " . $sql_instructions . "\n";
    echo "ErrorNo: " . $mysqli->errno . "\n";
    echo "Error: " . $mysqli->error . "\n";
    exit;
}

//if ($result_typeRecipe->num_rows === 0) {
//    echo "typeRecipe is empty";
//    exit;
//}

if ($result_ingredients->num_rows === 0) {
    echo "Ingredients is empty";
    exit;
}

if ($result_instructions->num_rows === 0) {
    echo "Instructions is empty";
    exit;
}

$data = array();

//foreach ($result_typeRecipe as $value) {
//    $data[$value['idRecipe']]['idRecipe'] = $value['idRecipe'];
//    $data[$value['idRecipe']]['title'] = $value['title'];
//    //$data[$value['idRecipe']]['typesRecipe'][] = ['idType' => $value['idType'], 'title' => $value['typeTitle']];
//}

foreach ($result_ingredients as $value) {
    $data[$value['idRecipe']]['idRecipe'] = $value['idRecipe'];
    $data[$value['idRecipe']]['title'] = $value['title'];
    $data[$value['idRecipe']]['time'] = $value['time'];
    $data[$value['idRecipe']]['image'] = $value['image'];
    $data[$value['idRecipe']]['url_source'] = $value['url_source'];
    $data[$value['idRecipe']]['portion'] = $value['portion'];
    $data[$value['idRecipe']]['type'] = $value['type'];
    $data[$value['idRecipe']]['ingredients'][] = ['id' => $value['id'],'idIngredient' => $value['idIngredient'], 'title' => $value['ingredientTitle'], 'amount' => $value['amount'], 'measureTitle' => $value['measureTitle']];
}

foreach ($result_instructions as $value) {
    $data[$value['idRecipe']]['idRecipe'] = $value['idRecipe'];
    $data[$value['idRecipe']]['instructions'][] = ['idInstruction' => $value['idInstruction'], 'title' => $value['instructionTitle']];
}

echo json_encode(array_values($data), JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);

$result_ingredients->free();
$result_instructions->free();
$mysqli->close();

?>
 
