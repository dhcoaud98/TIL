-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 3.38.166.208    Database: prosn
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `wrong_answer`
--

DROP TABLE IF EXISTS `wrong_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wrong_answer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `is_write` varchar(255) NOT NULL,
  `memo` varchar(255) DEFAULT NULL,
  `reason` varchar(255) DEFAULT NULL,
  `study_content` varchar(255) DEFAULT NULL,
  `wrong_answer` varchar(255) DEFAULT NULL,
  `post_id` bigint DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKj0vj9w5ebsuugh3qsud558ati` (`post_id`),
  KEY `FKjacrhfircqjjn0spcbqni85ga` (`user_id`),
  CONSTRAINT `FKj0vj9w5ebsuugh3qsud558ati` FOREIGN KEY (`post_id`) REFERENCES `problem` (`id`),
  CONSTRAINT `FKjacrhfircqjjn0spcbqni85ga` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wrong_answer`
--

LOCK TABLES `wrong_answer` WRITE;
/*!40000 ALTER TABLE `wrong_answer` DISABLE KEYS */;
INSERT INTO `wrong_answer` VALUES (2,'2022-08-18 07:51:14','2022-08-18 07:51:14','N',NULL,NULL,NULL,'3',1,2),(3,'2022-08-18 13:10:13','2022-08-19 01:00:27','N',NULL,NULL,NULL,'2',4,7),(4,'2022-08-18 15:40:12','2022-08-18 15:47:24','N',NULL,NULL,NULL,'4',1,6),(6,'2022-08-18 17:54:56','2022-08-18 17:55:19','Y','운영체제','모름','운영체제','4',1,3),(7,'2022-08-18 18:01:02','2022-08-18 18:01:09','N',NULL,NULL,NULL,'3',9,6),(8,'2022-08-18 18:04:50','2022-08-18 18:05:59','Y','까먹지말자!!','헷갈렸다.','트랜잭션에 대해서','4',5,16),(9,'2022-08-18 18:37:54','2022-08-18 18:37:54','N',NULL,NULL,NULL,'4',9,3),(10,'2022-08-19 00:59:43','2022-08-19 00:59:51','N',NULL,NULL,NULL,'4',13,18),(11,'2022-08-19 01:00:36','2022-08-19 01:00:36','N',NULL,NULL,NULL,'2',5,7),(12,'2022-08-19 01:00:48','2022-08-19 01:00:48','N',NULL,NULL,NULL,'2',1,7),(13,'2022-08-19 01:14:34','2022-08-19 02:56:11','Y','틀리지 말기!!!','몰라','프로세서 1장','4',21,7),(14,'2022-08-19 01:25:32','2022-08-19 01:25:37','N',NULL,NULL,NULL,'3',21,3),(15,'2022-08-19 01:31:15','2022-08-19 01:41:21','Y','다음에 또보기!!!!!','뭐지','DBMS 6장','3',24,7),(16,'2022-08-19 04:10:34','2022-08-19 04:10:34','N',NULL,NULL,NULL,'4',4,6),(17,'2022-08-19 04:21:08','2022-08-19 04:25:23','Y','틀리지말기!!!!!!!!!!!!!','UNIX','1장 공부','4',25,19);
/*!40000 ALTER TABLE `wrong_answer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-19 13:42:50
