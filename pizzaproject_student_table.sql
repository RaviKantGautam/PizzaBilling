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
-- Table structure for table `student_table`
--

DROP TABLE IF EXISTS `student_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `student_table` (
  `roll_no.` int(11) NOT NULL,
  `student_name` varchar(100) DEFAULT NULL,
  `father_name` varchar(100) DEFAULT NULL,
  `mobile_no.` varchar(30) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `class` varchar(50) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `semester` int(11) DEFAULT NULL,
  `bloodgroup` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`roll_no.`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_table`
--

LOCK TABLES `student_table` WRITE;
/*!40000 ALTER TABLE `student_table` DISABLE KEYS */;
INSERT INTO `student_table` VALUES (23231,'DAMAN KUMAR','SHIVRAJ KUMAR','3454567867','JALANDHAR','B-PHARMACY',25,'1994-04-11',2,'O+ve'),(23234,'DANISH KUMAR','SHANKAR KUMAR','3454565467','MOHALI','D-PHARMACY',23,'1996-04-11',3,'B+ve'),(43546,'sanjay shah','muniram shah','3565678543','hall gate','CSE',55,'1996-07-03',3,'AB+ve'),(45457,'sonia khatri','rakesh khatri','2343454232','amritsar','ME',23,'1987-12-04',1,'B+ve'),(45546,'kapil sharma','laalchand sharma','4545656243','khazana gate to agli gully','CSE',64,'1990-05-06',6,'O-ve'),(58789,'muskaan sharma','praveen sharma','4565455443','lahore','CSE',34,'1997-11-03',2,'A-ve'),(78978,'rachit agarwal','vikas agarwal','3435345776','ludhiana','CE',43,'1983-06-08',3,'O-ve'),(98766,'ritesh vohra','niranjan vohra','2334332344','dehli','IT',56,'1995-07-21',4,'A+ve');
/*!40000 ALTER TABLE `student_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-10 16:06:08
