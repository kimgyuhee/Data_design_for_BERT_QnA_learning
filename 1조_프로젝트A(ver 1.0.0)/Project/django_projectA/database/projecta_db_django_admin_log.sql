-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
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
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-05-24 10:40:37.218470','0','context object (0)',1,'[{\"added\": {}}]',7,1),(2,'2022-05-24 10:52:06.596998','4','context object (4)',3,'',7,1),(3,'2022-06-08 06:11:37.634777','13','context object (13)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(4,'2022-06-08 06:12:03.019364','14','context object (14)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(5,'2022-06-08 06:12:33.530795','11','context object (11)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(6,'2022-06-08 06:12:54.654574','2','context object (2)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(7,'2022-06-08 06:13:16.451142','1','context object (1)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(8,'2022-06-08 06:13:44.389397','3','context object (3)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(9,'2022-06-08 06:14:06.603777','4','context object (4)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(10,'2022-06-08 06:14:28.411597','5','context object (5)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(11,'2022-06-08 06:15:03.571665','6','context object (6)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(12,'2022-06-08 06:15:19.096679','7','context object (7)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(13,'2022-06-08 06:15:41.419036','8','context object (8)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(14,'2022-06-08 06:15:59.531895','9','context object (9)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(15,'2022-06-08 06:16:03.584134','9','context object (9)',2,'[]',7,1),(16,'2022-06-08 06:16:26.579466','10','context object (10)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(17,'2022-06-08 06:16:30.553409','10','context object (10)',2,'[]',7,1),(18,'2022-06-08 06:16:33.666530','11','context object (11)',2,'[]',7,1),(19,'2022-06-08 06:16:50.891195','12','context object (12)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(20,'2022-06-08 06:16:55.480843','14','context object (14)',2,'[]',7,1),(21,'2022-06-08 06:17:27.779150','15','context object (15)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(22,'2022-06-08 06:18:08.082809','6','context object (6)',2,'[{\"changed\": {\"fields\": [\"Country num\"]}}]',7,1),(23,'2022-06-08 06:18:39.084801','1','context object (1)',2,'[{\"changed\": {\"fields\": [\"Country num\"]}}]',7,1),(24,'2022-06-08 06:20:07.727627','15','context object (15)',2,'[]',7,1),(25,'2022-06-08 06:20:10.528919','14','context object (14)',2,'[]',7,1),(26,'2022-06-08 06:20:12.753585','13','context object (13)',2,'[]',7,1),(27,'2022-06-08 06:20:15.359943','12','context object (12)',2,'[]',7,1),(28,'2022-06-08 06:20:17.417025','11','context object (11)',2,'[]',7,1),(29,'2022-06-08 06:20:19.496241','10','context object (10)',2,'[]',7,1),(30,'2022-06-08 06:20:21.290168','9','context object (9)',2,'[]',7,1),(31,'2022-06-08 06:20:23.119663','8','context object (8)',2,'[]',7,1),(32,'2022-06-08 06:20:24.808547','7','context object (7)',2,'[]',7,1),(33,'2022-06-08 06:20:26.808884','6','context object (6)',2,'[]',7,1),(34,'2022-06-08 06:20:28.735818','5','context object (5)',2,'[]',7,1),(35,'2022-06-08 06:20:30.585683','4','context object (4)',2,'[]',7,1),(36,'2022-06-08 06:20:32.984959','3','context object (3)',2,'[]',7,1),(37,'2022-06-08 06:20:35.785879','2','context object (2)',2,'[]',7,1),(38,'2022-06-08 06:20:38.145901','1','context object (1)',2,'[]',7,1),(39,'2022-06-08 08:31:18.270231','1','questions object (1)',2,'[]',8,1),(40,'2022-06-08 08:39:47.591300','1','questions object (1)',2,'[{\"changed\": {\"fields\": [\"Context id\"]}}]',8,1),(41,'2022-06-10 00:23:29.887460','2','context object (2)',2,'[]',7,1),(42,'2022-06-10 00:31:27.006208','1','context object (1)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(43,'2022-06-10 00:32:58.633486','3','context object (3)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(44,'2022-06-10 00:34:22.879564','4','context object (4)',2,'[]',7,1),(45,'2022-06-10 00:35:56.824370','5','context object (5)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(46,'2022-06-10 00:36:44.924380','6','context object (6)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(47,'2022-06-10 00:37:40.152037','7','context object (7)',2,'[]',7,1),(48,'2022-06-10 00:38:22.063616','8','context object (8)',2,'[]',7,1),(49,'2022-06-10 00:39:02.288617','9','context object (9)',2,'[]',7,1),(50,'2022-06-10 00:44:07.139482','10','context object (10)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(51,'2022-06-10 00:46:09.545138','11','context object (11)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(52,'2022-06-10 00:50:48.624466','12','context object (12)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(53,'2022-06-10 00:52:44.074849','13','context object (13)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(54,'2022-06-10 00:53:47.928095','14','context object (14)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1),(55,'2022-06-10 00:55:23.408714','15','context object (15)',2,'[]',7,1),(56,'2022-06-10 00:58:25.664426','15','context object (15)',2,'[]',7,1),(57,'2022-06-15 02:51:31.998330','11','context object (11)',2,'[{\"changed\": {\"fields\": [\"Text\"]}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-16  9:58:50
