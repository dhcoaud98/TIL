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
-- Table structure for table `problem`
--

DROP TABLE IF EXISTS `problem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `problem` (
  `answer` varchar(255) DEFAULT NULL,
  `example1` varchar(255) DEFAULT NULL,
  `example2` varchar(255) DEFAULT NULL,
  `example3` varchar(255) DEFAULT NULL,
  `example4` varchar(255) DEFAULT NULL,
  `id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FKj2itd14e2vrlj9xr8yx3vcu06` FOREIGN KEY (`id`) REFERENCES `post` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problem`
--

LOCK TABLES `problem` WRITE;
/*!40000 ALTER TABLE `problem` DISABLE KEYS */;
INSERT INTO `problem` VALUES ('operating system','operating system','operation system','operation structure','operating structure',1),('외부 스키마','외부 스키마','개념 스키마','내부 스키마','슈퍼 스키마',4),('다중성','다중성','원자성','독립성','지속성',5),('네','네','트','워','크',7),('CPU','CPU','GUI','커널','드라이버',9),('Post 헤더','Post 헤더','Allow 헤더','Server 헤더','Location 헤더',13),('버스 토폴로지','버스 토폴로지','스타 토폴로지','링형 토폴로지','메시 토폴로지',19),('delete 시 기존의 인덱스를 삭제한다.','delete 시 기존의 인덱스를 삭제한다.','B+ 자료구조를 사용한다.','테이블에서 데이터를 조회하는 속도와 성능을 향상시킬 수 있다.','인덱스를 관리하기 위해 추가 작업이 필요하다',20),('독립된 스택 영역과 레지스터를 할당 받는다.','독립된 스택 영역과 레지스터를 할당 받는다.','프로세스는 한 개 이상의 스레드를 갖는다.','프로그램이 시작되면 프로세스이다.','병행 실행이 가능하다.',21),('클래스','클래스','메소드','상속성','메시지',22),('네트워크 구성도','네트워크 구성도','가용성','성능','상호 호환성',24),('프로세스, 기억장치, 입출력 관리를 수행한다. ','프로세스, 기억장치, 입출력 관리를 수행한다. ','명령어 해석기이다','시스템과 사용자 간의 인터페이스를 담당한다.','여러 종류의 쉘이 있다.',25),('TCP','TCP','HTTP','SMTP','FTP',26);
/*!40000 ALTER TABLE `problem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-19 13:42:48
