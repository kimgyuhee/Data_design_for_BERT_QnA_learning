-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: projecta_db
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions` (
  `question_id` int(11) NOT NULL AUTO_INCREMENT,
  `context_id` int(11) NOT NULL,
  `question` varchar(100) NOT NULL,
  `answer` varchar(100) NOT NULL,
  PRIMARY KEY (`question_id`),
  KEY `question_context_fk_idx` (`context_id`),
  CONSTRAINT `question_context_fk` FOREIGN KEY (`context_id`) REFERENCES `context` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1,1,'북한의 위치는?','동아시아의 한반도 북부'),(2,1,'북한의 수도는 어디인가?','평양'),(3,1,'북한은 남쪽으로 어느나라와 접하는가?','대한민국'),(4,1,'북한은 북쪽으로 어느나라와 접하는가?','중국 및 러시아'),(5,1,'북한의 공용어는?','조선어'),(6,1,'북한의 표준어는?','문화어'),(7,1,'북한은 언제 북조선 임시인민위원회를 수립했는가?','1946년 2월'),(8,1,'북위 38도 경계로 이북 지역을 누가 맡아 군정을 실시했는가?','소련군'),(9,1,'한반도는 어디를 경계로 이북 지역을 소련군이 맡아 군정을 실시했는가?','북위 38도'),(10,1,'북한이 공식적으로 출범한 날은 언제인가?','1948년 9월 9일'),(11,1,'북한의 공식적 출범 때 수상은 누구인가?','김일성'),(12,1,'김일성의 아들은 누구인가?','김정일'),(13,1,'김일성의 손자는 누구인가?','김정은'),(14,1,'김정일의 아들은 누구인가?','김정은'),(15,1,'사실상 북한의 1당 체제인 당은 어느 당인가?','조선노동당'),(16,1,'북한의 정치이념은 무엇인가?','주체사상과 선군정치'),(17,1,'주체사상이 최조로 등장한 시기는?','1972년');
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-25 17:38:50
