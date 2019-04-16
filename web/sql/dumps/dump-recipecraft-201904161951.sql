-- MySQL dump 10.17  Distrib 10.3.14-MariaDB, for Linux (x86_64)
--
-- Host: ih1430391.vds.myihor.ru    Database: recipecraft
-- ------------------------------------------------------
-- Server version	10.1.37-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ingredients`
--

DROP TABLE IF EXISTS `ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ingredients` (
  `idIngredient` int(11) NOT NULL AUTO_INCREMENT,
  `title_en` text,
  `title_ru` text,
  PRIMARY KEY (`idIngredient`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredients`
--

LOCK TABLES `ingredients` WRITE;
/*!40000 ALTER TABLE `ingredients` DISABLE KEYS */;
INSERT INTO `ingredients` VALUES (1,'','Филе куриное'),(2,NULL,'Шампиньоны'),(3,NULL,'Яйцо куриное'),(4,NULL,'Арахис'),(5,NULL,'Лук репчатый'),(6,NULL,'Морковь'),(7,NULL,'Майонез'),(8,NULL,'Маслины'),(9,NULL,'Кукуруза'),(10,NULL,'Сливки 20%'),(11,NULL,'Сливки 33%'),(12,'','Молоко 3,2% '),(13,NULL,'Желтки'),(14,NULL,'Сахар'),(15,NULL,'Ваниль'),(16,NULL,'Коньяк'),(17,NULL,'Ягоды'),(18,NULL,'Хлеб белый');
/*!40000 ALTER TABLE `ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `instruction`
--

DROP TABLE IF EXISTS `instruction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `instruction` (
  `idInstruction` int(11) NOT NULL AUTO_INCREMENT,
  `title_ru` text,
  `title_en` text,
  `idRecipe` int(11) DEFAULT NULL,
  PRIMARY KEY (`idInstruction`),
  KEY `instruction_recipes_FK` (`idRecipe`),
  CONSTRAINT `instruction_recipes_FK` FOREIGN KEY (`idRecipe`) REFERENCES `recipes` (`idRecipe`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `instruction`
--

LOCK TABLES `instruction` WRITE;
/*!40000 ALTER TABLE `instruction` DISABLE KEYS */;
INSERT INTO `instruction` VALUES (1,'Варим куриное филе (за 15 минут до готовности необходимо посолить и поперчить по вкусу). Варим яйцо и морковь.',NULL,1),(2,'Обжариваем порезанные грибы.',NULL,1),(3,'Тушим нарезанный кубиками лук на маленьком огне.',NULL,1),(4,'Измельчаем арахис на блендере.',NULL,1),(5,'Разделываем сваренное филе на волокна и смешиваем с половиной майонеза. Натираем морковь и белок яйца на терке.',NULL,1),(6,'Выкладываем слои салата в следующем порядке (важно выложить первый слой предельно похожим на силуэт нашей будущей \"белочки\"):\n- лук;\n- половина арахиса;\n- филе с майонезом;\n- вторая половина арахиса;\n- грибы (оставьте немного на украшение);\n- сеточка из майонеза;\n- морковь.','',1),(7,'Из белка украшаем хвостик и животик \"белочки\".',NULL,1),(8,'Из грибов делаем лапки. Носик и ушки делаем из маслин. Глазик из кукурузы или другого продукта. Желток от яйца даем белочке в лапки.\nСалат \"Белочка\" готов к подаче на стол.',NULL,1),(9,'В жаропрочную ёмкость выливаем молоко и сливки. Ставим на огонь и нагреваем до тех пор, пока по краям не появятся пузырьки. Ни в коем случае не даем им закипеть!',NULL,2),(10,'Взбиваем желтки, пока они не увеличатся в объеме и не посветлеют. Постепенно всыпаем сахар и взбиваем до полного растворения. Ароматизируем ванилью.',NULL,2),(11,'Смешиваем обе приготовленные смеси, постоянно взбивая венчиком.',NULL,2),(12,'Чтобы немного изменить вкус мороженого, можно добавить коньяк или ром. Также по желанию можно дополнить сливочное мороженое ягодами с сахаром, перетертыми блендером. ',NULL,2),(13,'Остужаем, накрываем крышкой и отправляем в морозилку на 3-4 часа. Каждый час достаем и взбиваем миксером или блендером. После того как перемешали 4-5 раз, оставляем в морозилке на ночь (7-8 часов).',NULL,2),(14,'Сливочное мороженое готово. Для подачи скатываем шарики из мороженого ложкой. Так как в нем нет стабилизаторов, то при комнатной температуре оно быстро тает.',NULL,2),(15,'Подготовим главный ингредиент для панировочных сухарей - белый хлеб.\nВ Японии для приготовления сухарей используют специальный хлеб без корочки. В нашем случае подойдет магазинный или домашний хлебушек. Для приготовления сухарей \"Панко\" желательно использовать вчерашний хлеб, чтобы при нарезке он не крошился.',NULL,3),(16,'Возьмите нож и со всех сторон обрежьте корочку с хлеба.',NULL,3),(17,'Нарежьте мякиш небольшими кусочками.',NULL,3),(18,'Маленькими порциями выкладывайте нарезанный хлеб в чашу блендера или кухонного комбайна и слегка измельчайте в режиме пульсации до крупной крошки. Периодически встряхивайте чашу, чтобы хлеб равномерно измельчился.',NULL,3),(19,'Противень застелите пергаментом. Выложите на него ровным слоем хлебные крошки. Разогрейте духовку до самой минимальной температуры, примерно 80-100 градусов. Отправьте противень в духовку. Дверцу слегка приоткройте. Подсушите хлебные крошки 20-25 минут. Возможно, понадобится больше времени, в зависимости от особенностей духовки. Периодически перемешивайте, чтобы сухари не подгорели. Они не должны поменять цвет, а должны остаться белыми. После того, как отключили духовку, оставьте сухари в духовке с приоткрытой дверцей еще на час.',NULL,3),(20,'Остудите. Храните панко в таре с закрывающейся крышкой.',NULL,3),(21,'Теперь и вы знаете, как приготовить сухари \"Панко\"!\nКрупная, воздушная сухарная панировка при обжаривании во фритюре меньше впитывает масло, и корочка получается более хрустящая.\nВкусных Вам блюд!',NULL,3);
/*!40000 ALTER TABLE `instruction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe_ingredients`
--

DROP TABLE IF EXISTS `recipe_ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipe_ingredients` (
  `idRecipe` int(11) NOT NULL,
  `idIngredient` int(11) NOT NULL,
  `amount` int(11) DEFAULT NULL,
  `idUnitMeasure` int(11) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `recipe_ingredients_recipe_FK` (`idRecipe`),
  KEY `recipe_ingredients_ingredient_FK` (`idIngredient`),
  KEY `recipe_ingredients_unit_measure_FK` (`idUnitMeasure`),
  CONSTRAINT `recipe_ingredients_ingredient_FK` FOREIGN KEY (`idIngredient`) REFERENCES `ingredients` (`idIngredient`),
  CONSTRAINT `recipe_ingredients_recipe_FK` FOREIGN KEY (`idRecipe`) REFERENCES `recipes` (`idRecipe`),
  CONSTRAINT `recipe_ingredients_unit_measure_FK` FOREIGN KEY (`idUnitMeasure`) REFERENCES `unit_measure` (`idUnitMeasure`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe_ingredients`
--

LOCK TABLES `recipe_ingredients` WRITE;
/*!40000 ALTER TABLE `recipe_ingredients` DISABLE KEYS */;
INSERT INTO `recipe_ingredients` VALUES (1,1,400,1,1),(1,2,300,1,2),(1,3,1,2,3),(1,4,100,1,4),(1,5,2,2,5),(1,6,2,2,6),(1,7,150,1,7),(1,8,2,2,8),(1,9,1,2,9),(2,10,200,3,10),(2,11,100,3,11),(2,12,100,3,12),(2,13,4,2,13),(2,14,100,1,14),(2,15,NULL,4,15),(2,16,20,3,16),(2,17,NULL,4,17),(3,18,300,1,18);
/*!40000 ALTER TABLE `recipe_ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe_types`
--

DROP TABLE IF EXISTS `recipe_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipe_types` (
  `idRecipe` int(11) NOT NULL,
  `idType` int(11) NOT NULL,
  KEY `recipe_types_recipe_FK` (`idRecipe`),
  KEY `recipe_types_type_recipe_FK` (`idType`),
  CONSTRAINT `recipe_types_recipe_FK` FOREIGN KEY (`idRecipe`) REFERENCES `recipes` (`idRecipe`),
  CONSTRAINT `recipe_types_type_recipe_FK` FOREIGN KEY (`idType`) REFERENCES `type_recipe` (`idType`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe_types`
--

LOCK TABLES `recipe_types` WRITE;
/*!40000 ALTER TABLE `recipe_types` DISABLE KEYS */;
INSERT INTO `recipe_types` VALUES (1,1);
/*!40000 ALTER TABLE `recipe_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes`
--

DROP TABLE IF EXISTS `recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes` (
  `idRecipe` int(11) NOT NULL AUTO_INCREMENT,
  `title_ru` varchar(100) DEFAULT NULL,
  `title_en` varchar(100) DEFAULT NULL,
  `time` int(11) DEFAULT NULL,
  `image` text,
  `portion` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `url_source` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idRecipe`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
INSERT INTO `recipes` VALUES (1,'Салат \"Белочка\"',NULL,80,NULL,4,'Основные блюда','https://www.russianfood.com'),(2,'Сливочное мороженое',NULL,720,NULL,3,'Десерты','https://www.russianfood.com'),(3,'Сухари \"Панко\"',NULL,25,NULL,10,'Смесь','https://www.russianfood.com');
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_message`
--

DROP TABLE IF EXISTS `report_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `report_message` (
  `idReport` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `message` text,
  PRIMARY KEY (`idReport`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_message`
--

LOCK TABLES `report_message` WRITE;
/*!40000 ALTER TABLE `report_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `report_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type_recipe`
--

DROP TABLE IF EXISTS `type_recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `type_recipe` (
  `idType` int(11) NOT NULL AUTO_INCREMENT,
  `title_ru` varchar(100) DEFAULT NULL,
  `title_en` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idType`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type_recipe`
--

LOCK TABLES `type_recipe` WRITE;
/*!40000 ALTER TABLE `type_recipe` DISABLE KEYS */;
INSERT INTO `type_recipe` VALUES (1,'Основные блюда',NULL),(2,'Десерты',NULL);
/*!40000 ALTER TABLE `type_recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unit_measure`
--

DROP TABLE IF EXISTS `unit_measure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unit_measure` (
  `idUnitMeasure` int(11) NOT NULL AUTO_INCREMENT,
  `title_ru` varchar(100) DEFAULT NULL,
  `title_en` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idUnitMeasure`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unit_measure`
--

LOCK TABLES `unit_measure` WRITE;
/*!40000 ALTER TABLE `unit_measure` DISABLE KEYS */;
INSERT INTO `unit_measure` VALUES (1,'г',NULL),(2,'шт',NULL),(3,'мл',NULL),(4,'по вкусу',NULL);
/*!40000 ALTER TABLE `unit_measure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'recipecraft'
--
