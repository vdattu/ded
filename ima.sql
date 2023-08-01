-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: doctors
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `game`
--

DROP TABLE IF EXISTS `game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game` (
  `ID` int DEFAULT NULL,
  `GAME` enum('ATHLETICS','ARCHERY','BADMINTON','CARROM','CHESS','CYCLOTHON','JUMPS','WALKATHON','SWIMMING','TENNKOIT','THROW','ROWING','ROLLER SKATING','FENCING','SHOOTING','TABLETENNIS','LAWNTENNIS','CRICKET_WHITE_BALL','HARD_TENNIS_CRICKET','WOMEN_BOX_CRICKET','VOLLEYBALL','FOOTBALL','KHO KHO','KABADDI','THROW BALL','TUG_OF_WAR','BALL_BADMINTON') DEFAULT NULL,
  `AMOUNT` int unsigned DEFAULT NULL,
  KEY `ID` (`ID`),
  CONSTRAINT `game_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `register` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game`
--

LOCK TABLES `game` WRITE;
/*!40000 ALTER TABLE `game` DISABLE KEYS */;
INSERT INTO `game` VALUES (230025,'ARCHERY',4000),(230025,'KABADDI',10000);
/*!40000 ALTER TABLE `game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `games` (
  `game_name` varchar(30) DEFAULT NULL,
  `amount` int unsigned DEFAULT NULL,
  `team_count` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES ('ATHLETICS',1500,1),('ARCHERY',1500,1),('BADMINTON',10000,2),('BASKET_BALL',10000,9),('CARROM',1500,2),('CHESS',1500,1),('CYCLOTHON',1500,1),('JUMPS',1500,1),('SWIMMING',1500,1),('THROW',1500,1),('ROWING',1500,1),('ROLLER_SKATING',1500,1),('FENCING',1500,1),('TENNIKOIT',1500,1),('TABLETENNIS',1500,2),('LAWNTENNIS',1500,2),('BALL_BADMINTON',10000,7),('CRICKET_WHITE_BALL',30000,14),('HARD_TENNIS_CRICKET',20000,14),('WOMEN_BOX_CRICKET',10000,7),('VOLLEYBALL',10000,9),('FOOTBALL',10000,11),('KHO_KHO',10000,12),('KABADDI',10000,10),('THROW_BALL',10000,10),('TUG_OF_WAR',5000,10);
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `ordid` varchar(36) NOT NULL,
  `id` int DEFAULT NULL,
  `game` enum('ATHLETICS','ARCHERY','BADMINTON','CARROM','CHESS','CYCLOTHON','JUMPS','WALKATHON','SWIMMING','TENNKOIT','THROW','ROWING','ROLLER SKATING','FENCING','SHOOTING','TABLETENNIS','LAWNTENNIS','CRICKET_WHITE_BALL','HARD_TENNIS_CRICKET','WOMEN_BOX_CRICKET','VOLLEYBALL','FOOTBALL','KHO KHO','KABADDI','THROW BALL','TUG_OF_WAR','BALL_BADMINTON') DEFAULT NULL,
  `amount` int unsigned DEFAULT NULL,
  `date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ordid`),
  KEY `id` (`id`),
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`id`) REFERENCES `register` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES ('5020d8b1-6471-4893-aa60-f0d3d03921f4',230025,'KABADDI',10000,'2023-07-31 16:55:03'),('5aa71819-1e11-40fb-8954-2b342aab27ae',230025,'ARCHERY',4000,'2023-07-31 15:36:26'),('6f73044d-bba0-4d35-979a-67e848156fe1',230025,'KABADDI',10000,'2023-07-31 16:50:19'),('c3ad6124-ec9c-41a4-903b-500623ea46a8',230025,'BALL_BADMINTON',10000,'2023-07-31 16:41:39'),('edf7b814-9560-4f05-a24c-705bd9d12d07',230025,'KABADDI',10000,'2023-07-31 15:48:23');
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(25) DEFAULT NULL,
  `LastName` varchar(25) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `PASSWORD` longblob,
  `mobileno` bigint DEFAULT NULL,
  `age` int DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `city` text,
  `address` text,
  `state` text,
  `country` text,
  `degree` varchar(10) DEFAULT NULL,
  `MCI_ID` varchar(20) DEFAULT NULL,
  `member` varchar(20) DEFAULT NULL,
  `SHIRT_SIZE` enum('S','M','L','XL','XXL','XXXL','XXXXL') DEFAULT NULL,
  `acception` varchar(30) DEFAULT 'No',
  `status` varchar(20) NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `mobileno` (`mobileno`)
) ENGINE=InnoDB AUTO_INCREMENT=230026 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register`
--

LOCK TABLES `register` WRITE;
/*!40000 ALTER TABLE `register` DISABLE KEYS */;
INSERT INTO `register` VALUES (230024,'Anuroop','Thota','anuroopt@gmail.com',_binary '$2b$12$yTqkvlqFo3A3XTZJ1NBnD.d3FlpdM9X7CWTtYWnTALSgo0hpr55Bi',8977030023,36,'Male','1986-03-20','vijayawad','29-8-40/A, Chiluku Durgaiah Street, Suryaraopet','Andhra Pradesh','India','MS','63937','IMA Member','XXL','Yes','pending'),(230025,'eswar','Nandivada','eswar@codegnan.com',_binary '$2b$12$3xUIdBgqYfFJmLrV4cUS/OqxunG9KelzSTHK42jwS8LkF2dPD9HR2',9177806313,20,'Male','2023-07-21','vijayawad','yanamalakushru','Andhra Pradesh','India','MBBS','63937','Non IMA Member','XL','Yes','success');
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sub_games`
--

DROP TABLE IF EXISTS `sub_games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sub_games` (
  `game` enum('ATHLETICS','ARCHERY','BADMINTON','CARROM','CHESS','CYCLOTHON','JUMPS','WALKATHON','SWIMMING','TENNKOIT','THROW','ROWING','ROLLER SKATING','FENCING','SHOOTING','TABLETENNIS','LAWNTENNIS','CRICKET_WHITE_BALL','HARD_TENNIS_CRICKET','WOMEN_BOX_CRICKET','VOLLEYBALL','FOOTBALL','KHO KHO','KABADDI','THROW BALL','TUG_OF_WAR') DEFAULT NULL,
  `id` int DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `team_number` int DEFAULT NULL,
  `date` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `team_number` (`team_number`),
  KEY `id` (`id`),
  CONSTRAINT `sub_games_ibfk_1` FOREIGN KEY (`id`) REFERENCES `register` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sub_games`
--

LOCK TABLES `sub_games` WRITE;
/*!40000 ALTER TABLE `sub_games` DISABLE KEYS */;
INSERT INTO `sub_games` VALUES ('ARCHERY',230025,'mens_singles',NULL,'2023-07-31 15:37:22');
/*!40000 ALTER TABLE `sub_games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teams`
--

DROP TABLE IF EXISTS `teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teams` (
  `teamid` int DEFAULT NULL,
  `id` int DEFAULT NULL,
  `status` enum('Accept','Pending') DEFAULT NULL,
  KEY `teamid` (`teamid`),
  KEY `id` (`id`),
  CONSTRAINT `teams_ibfk_1` FOREIGN KEY (`teamid`) REFERENCES `sub_games` (`team_number`),
  CONSTRAINT `teams_ibfk_2` FOREIGN KEY (`id`) REFERENCES `register` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams`
--

LOCK TABLES `teams` WRITE;
/*!40000 ALTER TABLE `teams` DISABLE KEYS */;
/*!40000 ALTER TABLE `teams` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-01  9:58:18
