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
-- Table structure for table `like_dislike`
--

DROP TABLE IF EXISTS `like_dislike`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `like_dislike` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `type` bit(1) NOT NULL,
  `post_id` bigint DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKsm96eh7udkbrbvlj4nsxmyr9e` (`post_id`),
  KEY `FK6xhbchneohj3puylx0cwje448` (`user_id`),
  CONSTRAINT `FK6xhbchneohj3puylx0cwje448` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `FKsm96eh7udkbrbvlj4nsxmyr9e` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `like_dislike`
--

LOCK TABLES `like_dislike` WRITE;
/*!40000 ALTER TABLE `like_dislike` DISABLE KEYS */;
INSERT INTO `like_dislike` VALUES (4,'2022-08-18 07:56:29','2022-08-18 07:56:29',_binary '\0',1,2),(5,'2022-08-18 07:56:29','2022-08-18 07:56:29',_binary '',1,2),(6,'2022-08-18 13:08:57','2022-08-18 13:08:57',_binary '',1,7),(8,'2022-08-18 17:35:13','2022-08-18 17:35:13',_binary '',5,6),(9,'2022-08-18 18:07:13','2022-08-18 18:07:13',_binary '',9,4),(10,'2022-08-18 18:07:31','2022-08-18 18:07:31',_binary '',7,4),(11,'2022-08-19 00:59:41','2022-08-19 00:59:41',_binary '',13,18),(12,'2022-08-19 00:59:48','2022-08-19 00:59:48',_binary '',4,7),(13,'2022-08-19 01:42:05','2022-08-19 01:42:05',_binary '',26,7);
/*!40000 ALTER TABLE `like_dislike` ENABLE KEYS */;
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
