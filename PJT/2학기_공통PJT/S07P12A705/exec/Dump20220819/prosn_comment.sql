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
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `main_text` varchar(255) DEFAULT NULL,
  `post_id` bigint DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKs1slvnkuemjsq2kj4h3vhx7i1` (`post_id`),
  KEY `FKqm52p1v3o13hy268he0wcngr5` (`user_id`),
  CONSTRAINT `FKqm52p1v3o13hy268he0wcngr5` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `FKs1slvnkuemjsq2kj4h3vhx7i1` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (1,'2022-08-18 07:46:57','2022-08-18 07:46:57','제 글 많이 사랑해주세요',2,1),(2,'2022-08-18 07:47:46','2022-08-18 07:47:46','극악의 난이도',1,1),(3,'2022-08-18 07:48:47','2022-08-18 07:48:47','와 겨우 마자따',1,2),(4,'2022-08-18 13:09:07','2022-08-18 13:09:07','문제 좋아여',1,7),(5,'2022-08-18 13:10:22','2022-08-18 13:10:22','어렵..',4,7),(6,'2022-08-18 17:47:22','2022-08-18 17:47:22','조아여',2,3),(7,'2022-08-18 17:47:58','2022-08-18 17:47:58','안녕',2,4),(8,'2022-08-18 18:03:33','2022-08-18 18:03:33','와 이거 어렵네요',9,6),(9,'2022-08-18 18:04:00','2022-08-18 18:04:00','무슨 이런 문제가 있나요',7,6),(10,'2022-08-18 18:06:33','2022-08-18 18:06:33','댓글 하나 더 달겠습니다.',7,6),(11,'2022-08-18 18:07:29','2022-08-18 18:07:29','저도 달고싶어요',7,16),(12,'2022-08-18 18:07:40','2022-08-18 18:07:40','-cm-',7,16),(13,'2022-08-18 18:08:20','2022-08-18 18:08:20','난 다 보고있다',7,16),(14,'2022-08-18 18:09:42','2022-08-18 18:09:42','아하 신난다',7,16),(15,'2022-08-18 19:17:22','2022-08-18 19:17:22','dfdf',9,3),(16,'2022-08-18 19:17:32','2022-08-18 19:17:32','edfd',11,3),(17,'2022-08-19 01:00:16','2022-08-19 01:00:16','문제 어려워요',13,7),(18,'2022-08-19 01:31:31','2022-08-19 01:31:31','문제 별론데..?내가 틀렷다니',24,7),(19,'2022-08-19 02:52:43','2022-08-19 02:52:43','아아',24,7),(20,'2022-08-19 04:21:47','2022-08-19 04:21:47','문제가 어렵네요ㅠ',25,19);
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-19 13:42:47
