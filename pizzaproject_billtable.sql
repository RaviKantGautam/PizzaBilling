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
-- Table structure for table `billtable`
--

DROP TABLE IF EXISTS `billtable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `billtable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date1` date DEFAULT NULL,
  `total` float DEFAULT NULL,
  `gst` float DEFAULT NULL,
  `netamount` float DEFAULT NULL,
  `customername` varchar(45) DEFAULT NULL,
  `mobileno` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `billtable`
--

LOCK TABLES `billtable` WRITE;
/*!40000 ALTER TABLE `billtable` DISABLE KEYS */;
INSERT INTO `billtable` VALUES (2,'2019-06-25',1460,73,1533,'sanjay','456475','sanjayshah@gmail.com'),(3,'2019-06-26',840,42,882,'kapil','98786785','kapilsharma@gmail.com'),(4,'2019-06-26',840,42,882,'kapil','325546677','kapilsharma@gmail.com'),(5,'2019-06-26',1680,84,1764,'kapil','37643498','kapilsharma@gmail.com'),(6,'2019-06-26',840,42,882,'Ravi','6280276218','ravikantgautamjazz@gmail.com'),(7,'2019-06-26',840,42,882,'ravi','6280276218','ravikantgautamjazz@gmail.com'),(8,'2019-06-26',840,42,882,'Ravi','6280276218','ravikantgautamjazz@gmail.com'),(9,'2019-06-27',3390,169.5,3559.5,'Kapil Sharma','6280276218','riteshvohra42@gmail.com'),(10,'2019-07-05',1890,0,0,'kapil sharma','6280276218','ravikantgautamjazz@gmail.com'),(11,'2019-07-05',5580,0,0,'sanjay shah','6280276218','ravikantgautamjazz@gmail.com'),(12,'2019-07-05',2584.5,0,0,'navneet kaur','6280276218','ravikantgautamjazz@gmail.com'),(13,'2019-07-05',300,0,0,'muskan chandri','9815264662','ravikantgautamjazz@gmail.com'),(14,'2019-07-05',200,0,0,'navrose kaur','9815264662','ravikantgautamjazz@gmail.com'),(15,'2019-07-05',200,0,0,'fahrad khan','9815462664','ravikantgautamjazz@gmail.com'),(16,'2019-07-05',2930.2,0,0,'Ravi','9646468921','ravikantgautamjazz@gmail.com'),(17,'2019-07-05',1298.4,0,0,'kapil sharma','8877888044','sanjaycool30509@gmail.com'),(18,'2019-07-05',2056.3,0,0,'jaykrishan','9646468921','ravikantgautamjazz@gmail.com'),(19,'2019-07-05',2056.3,0,0,'jaykrishan','9646468921','ravikantgautamjazz@gmail.com');
/*!40000 ALTER TABLE `billtable` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-10 16:06:05
