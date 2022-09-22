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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `dtype` varchar(31) NOT NULL,
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `authority` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `point` int DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('LocalUser',1,'2022-08-18 07:42:32','2022-08-18 07:42:32','ROLE_USER','test2@gmail.com','지미니',0),('LocalUser',2,'2022-08-18 07:48:15','2022-08-18 07:48:33','ROLE_USER','test3@gmail.com','남남쪽',10),('LocalUser',3,'2022-08-18 08:42:41','2022-08-19 01:26:02','ROLE_USER','ssafy@ssafy.com','프로즌',40),('LocalUser',4,'2022-08-18 08:45:16','2022-08-18 17:46:21','ROLE_USER','hong@gmail.com','홍길동',10),('LocalUser',5,'2022-08-18 12:25:49','2022-08-18 12:25:49','ROLE_USER','nse95@gmail.com','남성은',0),('LocalUser',6,'2022-08-18 12:54:17','2022-08-18 18:01:13','ROLE_USER','testnam@gmail.com','테스트남',20),('LocalUser',7,'2022-08-18 13:07:29','2022-08-19 01:31:05','ROLE_USER','dhcoaud12@gmail.com','오채명',60),('SocialUser',8,'2022-08-18 15:40:42','2022-08-18 15:40:42','ROLE_USER','koyura183982@naver.com','고유라',0),('SocialUser',9,'2022-08-18 15:53:05','2022-08-18 15:53:05','ROLE_USER','koyura183982@naver.com','고유라',0),('SocialUser',10,'2022-08-18 16:04:50','2022-08-18 16:04:50','ROLE_USER','duaudy@naver.com','정여명',0),('SocialUser',11,'2022-08-18 16:05:12','2022-08-18 16:05:12','ROLE_USER','duaudy@naver.com','정여명',0),('LocalUser',12,'2022-08-18 17:11:40','2022-08-18 17:11:40','ROLE_USER','user1@gmail.com','윤택',0),('LocalUser',13,'2022-08-18 17:24:23','2022-08-18 17:24:23','ROLE_USER','dbsxor@gmail.com','윤택',0),('LocalUser',14,'2022-08-18 17:26:08','2022-08-18 17:26:08','ROLE_USER','dkssud@ssafy.com','김싸피',0),('LocalUser',15,'2022-08-18 17:26:53','2022-08-18 17:27:26','ROLE_USER','gkdms@gmail.com','하은',10),('LocalUser',16,'2022-08-18 17:53:59','2022-08-18 18:04:41','ROLE_USER','test1@gmail.com','홍길동',10),('LocalUser',17,'2022-08-18 17:56:05','2022-08-18 17:56:27','ROLE_USER','test4@gmail.com','김철수',20),('LocalUser',18,'2022-08-19 00:42:56','2022-08-19 00:59:53','ROLE_USER','park@gmail.com','성민',10),('LocalUser',19,'2022-08-19 03:58:58','2022-08-19 04:21:25','ROLE_USER','winter@gmail.com','장겨울',10);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-19 13:42:53
