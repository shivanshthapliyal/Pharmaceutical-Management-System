-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: pharmacy
-- ------------------------------------------------------
-- Server version	8.0.11

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
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(20) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `address` varchar(20) DEFAULT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=1029 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1023,'Shishir Goyal','1452365987','sgoyal@gmail.com','sdfafas','qwert'),(1024,'Shivansh Thapliyal','3698452353','sthap@yahoo.com','tyuityij','asdf'),(1025,'Souradeep Banerjee','2103968486','sbanerjee@gmail.com','fdhfgcn','zxcv'),(1026,'Siddharth Sharma','3239465167','ssharma@yahoo.com','vbmvcbn','!@#$'),(1027,'Shivam Sharma','9876513654','ssharma12@yahoo.com','asdad','Abc123');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufacturer`
--

DROP TABLE IF EXISTS `manufacturer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manufacturer` (
  `manid` int(11) NOT NULL,
  `mname` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`manid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufacturer`
--

LOCK TABLES `manufacturer` WRITE;
/*!40000 ALTER TABLE `manufacturer` DISABLE KEYS */;
INSERT INTO `manufacturer` VALUES (245,'Wolter Kluwer'),(1103,'Cerner'),(3569,'Reddys'),(4587,'Truven'),(5463,'Reiden Global'),(6945,'ashp');
/*!40000 ALTER TABLE `manufacturer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicine`
--

DROP TABLE IF EXISTS `medicine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medicine` (
  `mid` int(11) NOT NULL,
  `mname` varchar(20) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  `manid` int(11) DEFAULT NULL,
  `exp_date` date NOT NULL,
  PRIMARY KEY (`mid`),
  KEY `manid` (`manid`),
  CONSTRAINT `medicine_ibfk_1` FOREIGN KEY (`manid`) REFERENCES `manufacturer` (`manid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine`
--

LOCK TABLES `medicine` WRITE;
/*!40000 ALTER TABLE `medicine` DISABLE KEYS */;
INSERT INTO `medicine` VALUES (256,'Calpol',25,100,5463,'2019-02-23'),(1450,'Hetrazein',36,200,3569,'2019-01-12'),(2213,'Acetaminophen.',1200,145,245,'2019-04-14'),(2598,'Adderall.',2050,100,1103,'2018-08-15'),(3219,'Apex',25,250,1103,'2018-12-12'),(6544,'Aciloc',10,500,4587,'2019-05-15'),(7451,'Atorvastatin.',50,600,6945,'2019-05-15'),(9870,'Morphine',50,236,6945,'2019-03-11');
/*!40000 ALTER TABLE `medicine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `oid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `mid` int(11) NOT NULL,
  `status` varchar(20) DEFAULT 'pending',
  `dateoforder` datetime DEFAULT NULL,
  `qty` int(11) NOT NULL,
  PRIMARY KEY (`oid`,`mid`),
  KEY `cid` (`cid`),
  KEY `mid` (`mid`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `customer` (`cid`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`mid`) REFERENCES `medicine` (`mid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (18,1023,1450,'pending','2018-08-01 22:39:54',0),(18,1023,3219,'pending','2018-08-01 22:40:03',0),(19,1025,256,'pending','2018-08-01 22:41:30',0),(19,1025,2213,'pending','2018-08-01 22:41:20',0),(19,1025,2598,'pending','2018-08-01 22:41:13',0),(20,1024,6544,'pending','2018-08-01 22:43:22',0),(20,1024,9870,'pending','2018-08-01 22:43:33',0),(27,1026,2213,'pending','2018-08-01 22:57:29',0);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-02 15:17:07
