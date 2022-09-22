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
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post` (
  `ptype` varchar(31) NOT NULL,
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `is_deleted` varchar(255) NOT NULL,
  `main_text` text,
  `num_of_dislikes` bigint DEFAULT '0',
  `num_of_likes` bigint DEFAULT '0',
  `title` varchar(255) DEFAULT NULL,
  `views` int DEFAULT '0',
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK7ky67sgi7k0ayf22652f7763r` (`user_id`),
  CONSTRAINT `FK7ky67sgi7k0ayf22652f7763r` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES ('Problem',1,'2022-08-18 07:43:27','2022-08-18 13:08:57','N','다음 중 운영체제의 풀네임으로 올바른 것은?',0,2,'운영체제 기본',14,1),('Information',2,'2022-08-18 07:46:32','2022-08-19 01:21:45','Y','다음에 알아보도록하자',0,0,'운영체제 관련 정보',7,1),('Workbook',3,'2022-08-18 07:50:53','2022-08-18 07:51:06','N',NULL,0,0,'운영체제 기본 수정',2,2),('Problem',4,'2022-08-18 12:28:13','2022-08-19 00:59:48','N','데이터베이스를 사용자 관점에서 이해한 구조로 각 사용자에게 필요한 데이터베이스의 구조를 정의하여 하나의 데이터베이스에 여러 개가 존재할 수 있는 스키마는?',0,1,'3단계 데이터베이스 구조에서의 스키마',7,5),('Problem',5,'2022-08-18 17:26:15','2022-08-18 17:35:13','N','트랜잭션은 데이터베이스에서 하나의 논리적 기능을 수행하기 위한 작업의 단위를 말하며 데이터베이스에 접근하는 방법은 쿼리이므로, 즉 여러 개의 쿼리들을 하나로 묶는 단위를 말한다. 이에 대한 특징으로 옳지 않은 것은?',0,1,'다음 중 옳지 않은 것을 고르시오.',9,13),('Workbook',6,'2022-08-18 17:29:07','2022-08-18 17:29:07','N',NULL,0,0,'데이터베이스 문제집_he',4,15),('Problem',7,'2022-08-18 17:50:49','2022-08-19 01:14:12','Y','네트워크, 운영체제',0,1,'네트워크, 운영체제',4,3),('Information',8,'2022-08-18 17:51:18','2022-08-18 17:51:18','N','알고리즘 객체지향',0,0,'알고리즘 객체지향',113,3),('Problem',9,'2022-08-18 17:55:19','2022-08-18 18:07:13','N','운영체제의 구조로 포함되지 않는 것을 고르시오.',0,1,'다음 중 옳지 않은 것은?',12,16),('Workbook',10,'2022-08-18 17:57:36','2022-08-18 17:57:36','N',NULL,0,0,'운영체제_철수1',1,17),('Information',11,'2022-08-18 18:01:11','2022-08-18 18:01:11','N','1. CPU 스케줄링과 프로세스 관리\n2. 메모리 관리\n3. 디스크 파일 관리\n4. I/O 디바이스 관리',0,0,'운영체제의 역할',123,17),('Workbook',12,'2022-08-18 18:48:52','2022-08-18 18:48:52','N',NULL,0,0,'기본1',2,3),('Problem',13,'2022-08-18 21:31:10','2022-08-19 00:59:41','N','HTTP 응답헤더로 옳지 않은 것은 무엇인가요?',0,1,'HTTP 응답헤더',8,6),('Workbook',14,'2022-08-18 21:39:07','2022-08-18 21:39:07','N',NULL,0,0,'좋은 문제들',2,6),('Information',15,'2022-08-19 00:46:49','2022-08-19 00:46:49','N','SQL Injection은 코드 인젝션의 한 기법으로 클라이언트의 입력값을 조작하여 서버의 데이터베이스를 공격할 수 있는 공격방식을 말한다.\n인젝션 공격은 OWASP Top10 중 첫 번째에 속해 있으며, 공격이 비교적 쉬운 편이고 공격에 성공할 경우 큰 피해를 입힐 수 있다.\n\n공격 방법으로는 Error based SQL Injection, Union based SQL Injection 등이 있다.',0,0,'SQL Injection',103,18),('Information',16,'2022-08-19 00:47:41','2022-08-19 00:47:41','N','XSS는 Cross-site Scripting의 줄임말로, 웹사이트에 악성 스크립트를 주입하는 행위를 말한다.\n공격에 성공하면 사이트에 접속한 사용자는 삽입된 코드를 실행하게 되며, 보통 의도치 않은 행동을 수행시키거나 쿠키나 세션 토큰 등의 민감한 정보를 탈취한다.\nSQL Injection과 마찬가지로 OWASP Top10에 포함되어 있다.',0,0,'XSS',105,18),('Information',17,'2022-08-19 00:58:14','2022-08-19 00:58:14','N','원자성(Atomicity) : 트랜잭션이 DB에 모두 반영되거나, 혹은 전혀 반영되지 않아야 한다.\n일관성(Consistency) : 트랜잭션이 실행을 성공적으로 완료하면 언제나 일관성 있는 데이터베이스 상태로 유지되어야 한다.\n격리성(Isolation) : 트랜잭션을 수행 시 다른 트랜잭션의 연산 작업이 끼어들지 못하도록 보장해야 한다.\n지속성(Durability) : 성공적으로 수행된 트랜잭션은 영원히 반영되어야 한다.',0,0,'트랜잭션 ACID',174,18),('Information',18,'2022-08-19 00:59:01','2022-08-19 00:59:01','N','인덱스(:index)는 데이터베이스 분야에 있어서 추가적인 쓰기 작업과 저장공간을 활용하여 테이블에 대한 검색 속도를 높여주는 자료 구조를 일컫는다.\n인덱스는 테이블 내의 1개의 컬럼, 혹은 여러 개의 컬럼을 이용하여 생성될 수 있다.\n고속의 검색 동작뿐만 아니라 레코드 접근과 관련 효율적인 순서 매김 동작에 대한 기초를 제공한다.\n인덱스의 자료구조 : B+Tree',0,0,'Index',171,18),('Problem',19,'2022-08-19 00:59:26','2022-08-19 00:59:26','N','네트워크 토폴로지(network topology)는 노드와 링크가 어떻게 배치되어 있는지에 대한 방식이자 연결 형태를 의미한다. 그 중 중앙 통신 회선 하나에 여러 개의 노드가 연결되어 공유하는 네트워크 구성을 말하며 근거리 통신망(LAM)에서 사용되는 토폴로지는?',0,0,'네트워크 토폴로지 종류',3,7),('Problem',20,'2022-08-19 01:02:37','2022-08-19 01:02:37','N','다음 중 인덱스에 대한 설명 중 옳지 않은 것은?',0,0,'Index(인덱스)',6,18),('Problem',21,'2022-08-19 01:06:28','2022-08-19 01:06:28','N','프로세스에 대한 설명으로 틀린 것은?',0,0,'프로세스(Process)',16,18),('Problem',22,'2022-08-19 01:15:44','2022-08-19 01:15:44','N','객체지향 프로그램에서 데이터를 추상화하는 단위는?',0,0,'객체지향 데이터 추상화',1,3),('Workbook',23,'2022-08-19 01:16:17','2022-08-19 01:16:17','N',NULL,0,0,'채명1',4,7),('Problem',24,'2022-08-19 01:16:47','2022-08-19 01:16:47','N','DBMS 분석 시 고려사항으로 거리가 먼 것은?',0,0,'DBMS 분석',11,3),('Problem',25,'2022-08-19 01:23:48','2022-08-19 01:23:48','N','UNIX의 쉘(Shell)에 관한 설명으로 옳지 않은 것은?',0,0,'UNIX',11,3),('Problem',26,'2022-08-19 01:24:41','2022-08-19 01:42:05','N','TCP/IP 프로토콜 중 전송계층 프로토콜은?',0,1,'전송계층 프로토콜',12,3),('Information',27,'2022-08-19 01:27:08','2022-08-19 01:27:08','N','애플리케이션 계층을 나누면 총 4가지로 나눌 수 있다. \n\n1. 애플리케이션 계층 : FTP/HTTP/SSH/SMTP/DNS\n2. 전송계층 : TCP/UDP/QUIC\n3. 인터넷 계층 : IP/ARP/ICMP\n4. 링크 계층 : 이더넷\n',0,0,'TCP/IP에 4계층에 대해서',172,7),('Information',28,'2022-08-19 01:30:20','2022-08-19 01:30:20','N','데이터가 4차 산업혁명 시대의 중요한 요소 중 하나라는 것에 많은 사람들이 동의한다. 또한, 새롭게 출범하\n는 이번 정부의 경제 정책 중에서도 데이터플랫폼 거버먼트, 데이터 경제가 매우 중요한 위치를 차지하고\n있다. 디지털 데이터 중 70% 이상이 개인과 관련된 데이터이며, 공공은 물론 민간의 데이터를 활용하기\n위해서는 개인정보의 안전한 활용이 필수적이다. 개인정보를 처리하는 제품 및 서비스의 안전성 검증은 국민\n과 소비자의 신뢰로 이어지기 때문이다. 국내에서는 정보통신망에 연결되어 정보를 송ㆍ수신할 수 있는 IoT\n기기에 대한 정보보호 인증이 시행되고 있으나, 개인정보보호 중심 설계(Privacy by Design) 적용 여부에\n대해 평가하고 있지 않다. 한편, EU에서는 독일 EuroPriSe, 이탈리아 ISDPⓒ 10003, 룩셈부르크의\nGDPR-CARPA 등 각 국가별로 인증제도가 운영되고 있다. 이 중 IT 제품 및 서비스에 대한 개인정보보호\n인증은 독일 EuroPriSe 사례가 유일하고, 그 외는 제품 단위가 아닌 개인정보처리자의 개인정보 처리 절차\n및 보호조치 여부에 대해 검증하고 있다',0,0,'프라이버시를 고려한 설계',163,3),('Workbook',29,'2022-08-19 01:34:26','2022-08-19 01:34:26','N',NULL,0,0,'채명_운영체제1',2,7),('Information',30,'2022-08-19 01:40:18','2022-08-19 01:40:18','N','HTTPS(Hypertext Transfer Protocol Secure)\nHTTP 통신하는 소켓 부분을 인터넷 상에서 암호화하는 SSL (Secure Sockets Layer) 사용.\nHTTP는 TCP와 통신했지만, HTTPS에서는 SSL과 통신하고 SSL이 TCP와 통신한다.\nSSL은 서버와 브라우저 사이에 안전하게 암호화된 연결을 만들 수 있게 도와주고, 서버와 브라우저가 민감한 정보를 주고받을 때 해당 정보가 도난당하는 것을 막아준다.\nHTTPS는 HTTP 자체를 암호화 하는것이 아니라, HTTP를 사용해서 운반하는 내용(HTTP message body)을 암호화한다.\nHTTPS의 SSL에서는 대칭키 암호화 방식, 공개키 암호화 방식 모두 사용한다.\n\n왜 HTTPS를 사용할까?\n\n1. 보안성\n- 데이터를 전송할 때 HTTP를 사용하면 중간에 가로챘을 때 어떤 내용인지 알 수 있다.\n- HTTPS를 사용하면 암호화 되어 있어 어떤 내용인지 알 수 없다.\n2. SEO(검색 엔진 최적화)\n- 구글은 HTTPS 웹 사이트에 가산점을 준다. HTTPS를 사용해야 검색 엔진에 빈번하게 노출될 확률이 증가한다.\n3. AMP(가속화된 모바일 페이지)\n- AMP를 만들 때 HTTPS를 사용해야 한다.',0,0,'HTTPS',153,18),('Workbook',31,'2022-08-19 02:54:09','2022-08-19 02:54:09','N',NULL,0,0,'채명_운영체제2',2,7),('Workbook',32,'2022-08-19 04:23:18','2022-08-19 04:23:18','N',NULL,0,0,'0819문제',0,19),('Information',33,'2022-08-19 04:38:27','2022-08-19 04:38:27','N','다들 너무 수고했어 행복하진 않았어도 보람됐다 다들 만나서 정말 다행이었어',0,0,'705둥이들',3,1);
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
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
