-- MySQL dump 10.13  Distrib 5.6.28, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: ecoData
-- ------------------------------------------------------
-- Server version	5.6.28-0ubuntu0.15.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Current1`
--

DROP TABLE IF EXISTS `Current1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Current1` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TYPE` varchar(20) DEFAULT NULL,
  `DATA` varchar(50) DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Current1`
--

LOCK TABLES `Current1` WRITE;
/*!40000 ALTER TABLE `Current1` DISABLE KEYS */;
/*!40000 ALTER TABLE `Current1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Current2`
--

DROP TABLE IF EXISTS `Current2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Current2` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TYPE` varchar(20) DEFAULT NULL,
  `DATA` varchar(50) DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Current2`
--

LOCK TABLES `Current2` WRITE;
/*!40000 ALTER TABLE `Current2` DISABLE KEYS */;
/*!40000 ALTER TABLE `Current2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DriverInstructions`
--

DROP TABLE IF EXISTS `DriverInstructions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DriverInstructions` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `THROTTLE` int(6) DEFAULT NULL,
  `DISPLAYSWITCH` int(6) DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DriverInstructions`
--

LOCK TABLES `DriverInstructions` WRITE;
/*!40000 ALTER TABLE `DriverInstructions` DISABLE KEYS */;
/*!40000 ALTER TABLE `DriverInstructions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GBInstructions`
--

DROP TABLE IF EXISTS `GBInstructions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GBInstructions` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `FCPOWER` int(6) DEFAULT NULL,
  `THROTTLEADVICE` int(6) DEFAULT NULL,
  `STEERADVICE` int(6) DEFAULT NULL,
  `MOTORSETTINGS` int(6) DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GBInstructions`
--

LOCK TABLES `GBInstructions` WRITE;
/*!40000 ALTER TABLE `GBInstructions` DISABLE KEYS */;
/*!40000 ALTER TABLE `GBInstructions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GPS`
--

DROP TABLE IF EXISTS `GPS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GPS` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `LONGTITUDE` varchar(20) DEFAULT NULL,
  `LATTITUDE` varchar(20) DEFAULT NULL,
  `SPEED` float(3,2) DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GPS`
--

LOCK TABLES `GPS` WRITE;
/*!40000 ALTER TABLE `GPS` DISABLE KEYS */;
/*!40000 ALTER TABLE `GPS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Power1`
--

DROP TABLE IF EXISTS `Power1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Power1` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TYPE` varchar(20) DEFAULT NULL,
  `DATA` varchar(50) DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Power1`
--

LOCK TABLES `Power1` WRITE;
/*!40000 ALTER TABLE `Power1` DISABLE KEYS */;
/*!40000 ALTER TABLE `Power1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Power2`
--

DROP TABLE IF EXISTS `Power2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Power2` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TYPE` varchar(20) DEFAULT NULL,
  `DATA` varchar(50) DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Power2`
--

LOCK TABLES `Power2` WRITE;
/*!40000 ALTER TABLE `Power2` DISABLE KEYS */;
/*!40000 ALTER TABLE `Power2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Power3`
--

DROP TABLE IF EXISTS `Power3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Power3` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TYPE` varchar(20) DEFAULT NULL,
  `DATA` varchar(50) DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Power3`
--

LOCK TABLES `Power3` WRITE;
/*!40000 ALTER TABLE `Power3` DISABLE KEYS */;
/*!40000 ALTER TABLE `Power3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rpm1`
--

DROP TABLE IF EXISTS `Rpm1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Rpm1` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TYPE` varchar(20) DEFAULT NULL,
  `DATA` varchar(50) DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rpm1`
--

LOCK TABLES `Rpm1` WRITE;
/*!40000 ALTER TABLE `Rpm1` DISABLE KEYS */;
/*!40000 ALTER TABLE `Rpm1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rpm2`
--

DROP TABLE IF EXISTS `Rpm2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Rpm2` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TYPE` varchar(20) DEFAULT NULL,
  `DATA` varchar(50) DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rpm2`
--

LOCK TABLES `Rpm2` WRITE;
/*!40000 ALTER TABLE `Rpm2` DISABLE KEYS */;
/*!40000 ALTER TABLE `Rpm2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rpm3`
--

DROP TABLE IF EXISTS `Rpm3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Rpm3` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TYPE` varchar(20) DEFAULT NULL,
  `DATA` varchar(50) DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rpm3`
--

LOCK TABLES `Rpm3` WRITE;
/*!40000 ALTER TABLE `Rpm3` DISABLE KEYS */;
/*!40000 ALTER TABLE `Rpm3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `StrategyInstructions`
--

DROP TABLE IF EXISTS `StrategyInstructions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `StrategyInstructions` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `FCPOWER` int(6) DEFAULT NULL,
  `THROTTLEADVICE` int(6) DEFAULT NULL,
  `MOTORSETTINGS` int(6) DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StrategyInstructions`
--

LOCK TABLES `StrategyInstructions` WRITE;
/*!40000 ALTER TABLE `StrategyInstructions` DISABLE KEYS */;
/*!40000 ALTER TABLE `StrategyInstructions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Voltage1`
--

DROP TABLE IF EXISTS `Voltage1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Voltage1` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TYPE` varchar(20) DEFAULT NULL,
  `DATA` varchar(50) DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Voltage1`
--

LOCK TABLES `Voltage1` WRITE;
/*!40000 ALTER TABLE `Voltage1` DISABLE KEYS */;
/*!40000 ALTER TABLE `Voltage1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Voltage2`
--

DROP TABLE IF EXISTS `Voltage2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Voltage2` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TYPE` varchar(20) DEFAULT NULL,
  `DATA` varchar(50) DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Voltage2`
--

LOCK TABLES `Voltage2` WRITE;
/*!40000 ALTER TABLE `Voltage2` DISABLE KEYS */;
/*!40000 ALTER TABLE `Voltage2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-02 16:35:00
