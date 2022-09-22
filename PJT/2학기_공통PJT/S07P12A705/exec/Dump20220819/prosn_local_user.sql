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
-- Table structure for table `local_user`
--

DROP TABLE IF EXISTS `local_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `local_user` (
  `password` varchar(255) DEFAULT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK3ilvp82eg1mybm89lmcq0unvq` FOREIGN KEY (`id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `local_user`
--

LOCK TABLES `local_user` WRITE;
/*!40000 ALTER TABLE `local_user` DISABLE KEYS */;
INSERT INTO `local_user` VALUES ('$2a$10$A5R1iCiagdX8gyIAhVqQKOxUcSoiS/IT0inZ.0QOaA6i0EjGmoCoe','test2',1),('$2a$10$.NSZX9kVrlQ0VVIb1QHppOJQbkUwdIzAKP5zOLwe.ZylZtbNWmJyK','test3',2),('$2a$10$XZkosmQwlxmqyHisPxgCFOXeDb6JUlx1GzG7kWAe4GXv14y.XItfi','prosn',3),('$2a$10$yDP92XkbyuONsCKFTXHwhebFMBylnfmbG34LWTORHt2ECTQFBmJB.','hong',4),('$2a$10$NiIA5co81KowgjMsJQd.UuiuwaryTEQoYNd94giliuvFfj/TlBAxq','nse95',5),('$2a$10$5YmBVRVwjFQEOPsd4jCR3.2w/dvPXyQhESLoe1FhxXRkbQ4ycKoBK','testnam',6),('$2a$10$BQTc9xhk7jWgClW4KhFeIOtU9Cwi3zpEFkg7czVWyRv.dA.iVClu2','dhcoaud12',7),('$2a$10$RJXWE5FfZAv/4cnzgU/65eiXEmrPnutpQce248fAkvd24MfKAILfC','user1',12),('$2a$10$jOlM9Rm7gRZkdmtFZN49FuAeunQfj8BhIqopNbIameoRy7KGTCTG6','dbsxor',13),('$2a$10$n7IgapJ8tMziPmSmCok/JeJJEQjFCzeuNg7qZ3dU6NAqO.SExWp9i','dkssud',14),('$2a$10$AAr36naRN5qaLPIOrW/otuW1aNx/n9oia.O9SCSkZhqvj6VNPB9XK','gkdms',15),('$2a$10$N5PD7HcEHWtMDgsBv2p2g.oOukG2s4E11I/yZZonx9caZgG8xUBCu','test1',16),('$2a$10$OrxzSAmF.o9Sh.FfmG4x/.lAWey7mncDfrzl8vbjtDT1CS4c5mLwC','test4',17),('$2a$10$AGISLNOh.WyZCqOvos1lu.RLC8smQozydUTPc8JIVkKTLJwKFyNjS','park',18),('$2a$10$7SGGqpVXsmsM1wTzwMKow.JLWTeG0Wzbp1hcngQXxz61R3Ri1b2MS','winter',19);
/*!40000 ALTER TABLE `local_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-19 13:42:51
