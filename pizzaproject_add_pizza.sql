-- MySQL dump 10.13  Distrib 8.0.14, for Win64 (x86_64)
--
-- Host: localhost    Database: pizzaproject
-- ------------------------------------------------------
-- Server version	8.0.14

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `add_pizza`
--

DROP TABLE IF EXISTS `add_pizza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `add_pizza` (
  `PID` int(11) NOT NULL AUTO_INCREMENT,
  `p_name` varchar(100) DEFAULT NULL,
  `MRP` float DEFAULT NULL,
  `Discount` float DEFAULT NULL,
  `Disprice` float DEFAULT NULL,
  `categoryname` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`PID`),
  KEY `categoryname_idx` (`categoryname`),
  CONSTRAINT `categorynamewe` FOREIGN KEY (`categoryname`) REFERENCES `categorytable` (`categoryname`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `add_pizza`
--

LOCK TABLES `add_pizza` WRITE;
/*!40000 ALTER TABLE `add_pizza` DISABLE KEYS */;
INSERT INTO `add_pizza` VALUES (2,'mixed pizza',234.45,30.2,180.9,'fish'),(4,'dinner',234,33,345,'fish'),(5,'rajma chawal',120,20,100,'Indian'),(6,'chicken barbeque',450,10,420,'Indian'),(7,'extra cheese pizza',500,23,430,'Indian'),(8,'Mixed-veg',150,20,120,'Indian'),(9,'Deluxe Veggie',450,10,405,'VEG-PIZZAS'),(10,'Veg Extravaganza',450,5,427.5,'BURGER PIZZAS'),(11,'Aussie Barbecue',450,2,441,'VEG-PIZZAS'),(12,'Indi Tandoori Paneer',450,3,436.5,'VEG-PIZZAS'),(13,'Farmhouse',395,4,379.2,'VEG-PIZZAS'),(14,'Peppy Paneer',395,2,387.1,'VEG-PIZZAS'),(15,'MexicanGreen Wave',395,6,371.3,'VEG-PIZZAS'),(16,'Veggie Paradise',395,7,367.35,'VEG-PIZZAS'),(17,'Paneer Makhani',395,3,383.15,'VEG-PIZZAS'),(18,'African Peri Peri Veg',395,2,387.1,'VEG-PIZZAS'),(19,'Jamiacan Jerk Veg',395,2,387.1,'VEG-PIZZAS'),(20,'English Cheddar And Veggies',335,2,328.3,'VEG-PIZZAS'),(21,'Double Cheese Margherita',335,3,324.95,'VEG-PIZZAS'),(22,'Cheese n Corn',305,2,298.9,'VEG-PIZZAS'),(23,'Cheese n Tomato',305,2,298.9,'VEG-PIZZAS'),(24,'Margherita',199,20,159.2,'VEG-PIZZAS'),(25,'Non Veg Supreme',570,4,547.2,'NON-VEG PIZZAS'),(26,'Chicken Pepperoni',570,3,552.9,'NON-VEG PIZZAS'),(27,'Chicken Dominator',570,2,558.6,'NON-VEG PIZZAS'),(28,'Aussie Barbecue Chicken',570,2,558.6,'NON-VEG PIZZAS'),(29,'Jamaican Jerk Chicken',570,3,552.9,'NON-VEG PIZZAS'),(30,'Indi Chicken Tikka',570,5,541.5,'NON-VEG PIZZAS'),(31,'Chicken Golden Delight',450,1,445.5,'NON-VEG PIZZAS'),(32,'Chicken Fiesta',450,2,441,'NON-VEG PIZZAS'),(33,'African Peri Peri Chicken',450,1,445.5,'NON-VEG PIZZAS'),(34,'English Cheddar And Chicken Sausage',450,2,441,'NON-VEG PIZZAS'),(35,'Pepper Barbecue And Onion',395,3,383.15,'NON-VEG PIZZAS'),(36,'Pepper Barbecue Chicken',335,2,328.3,'NON-VEG PIZZAS'),(37,'Chicken Sausage',305,2,298.9,'NON-VEG PIZZAS'),(38,'Non Veg Loaded',155,2,151.9,'PIZZA MANIA'),(39,'Veg Loaded',135,2,132.3,'PIZZA MANIA'),(40,'Pepper Barbecue Chicken',105,3,101.85,'PIZZA MANIA'),(41,'Cheesy',99,1,98.01,'PIZZA MANIA'),(42,'Panner And Onion',95,5,90.25,'PIZZA MANIA'),(43,'Chicken Sausage',95,5,90.25,'PIZZA MANIA'),(44,'Golden Corn',79,4,75.84,'PIZZA MANIA'),(45,'Capsicum',75,3,72.75,'PIZZA MANIA'),(46,'Onion',59,9,53.69,'PIZZA MANIA'),(47,'Tomato',59,15,50.15,'PIZZA MANIA'),(48,'Classic Veg',70,2,68.6,'BURGER PIZZAS'),(49,'Premium Veg',75,2,73.5,'BURGER PIZZAS'),(50,'Classic Non Veg',90,3,87.3,'BURGER PIZZAS');
/*!40000 ALTER TABLE `add_pizza` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-10 16:06:09
