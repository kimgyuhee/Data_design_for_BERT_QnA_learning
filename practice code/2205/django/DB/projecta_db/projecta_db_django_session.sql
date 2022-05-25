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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2ho005iaorseu81a9v1jq624gm028t0q','.eJxVjMsOwiAQRf-FtSEMHUpx6d5vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yjOAsTpd2MKj1R3EO9Ub02GVtdlZrkr8qBdXltMz8vh_h0U6uVbOwqM1mQcmMfRTaBhCpAtWQeoEFTQkY12dlApoklMmVAjB6XUQAbE-wPQpDdR:1ntRct:6zgcmbzeXBp7DfNX2NfMxbejIEtemSxS_2KOxn8_hkg','2022-06-07 10:18:55.118587'),('2vzk6u7cz2q39xd4u6fgglsa420mov8w','.eJxVjMsOwiAQRf-FtSEMHUpx6d5vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yjOAsTpd2MKj1R3EO9Ub02GVtdlZrkr8qBdXltMz8vh_h0U6uVbOwqM1mQcmMfRTaBhCpAtWQeoEFTQkY12dlApoklMmVAjB6XUQAbE-wPQpDdR:1ntkEL:0qO0bu_Jmq8_Q2TolkjDx7PcqRh1yzMmlyTI5mijKcA','2022-06-08 06:10:49.673398'),('ig92peqnqmfsq0pl6sksiwed351tlwuc','.eJxVjMsOwiAQRf-FtSEMHUpx6d5vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yjOAsTpd2MKj1R3EO9Ub02GVtdlZrkr8qBdXltMz8vh_h0U6uVbOwqM1mQcmMfRTaBhCpAtWQeoEFTQkY12dlApoklMmVAjB6XUQAbE-wPQpDdR:1ntRTA:7WTrODwv7RPWC6pRBOyL6W8NsIzi0pc6CuosSrT33so','2022-06-07 10:08:52.011471'),('zh89egklntym86xs06ogr4qg2xdaoxmw','.eJxVjMsOwiAQRf-FtSEMHUpx6d5vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yjOAsTpd2MKj1R3EO9Ub02GVtdlZrkr8qBdXltMz8vh_h0U6uVbOwqM1mQcmMfRTaBhCpAtWQeoEFTQkY12dlApoklMmVAjB6XUQAbE-wPQpDdR:1ntRr9:8mZRsrDiVx7HlfqgnRuPShFRKttY90kDCnfkuvHn-04','2022-06-07 10:33:39.986369');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-25 17:38:49
