-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: staff
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `name` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  `department` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  `position` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  `salary` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES ('刘萍','技术部门','技术负责人',15000),('卢宇','技术部门','运维开发工程师',10000),('邹旭','技术部门','项目经理',10000),('陶晨','技术部门','后端开发工程师',10000),('曹坤','技术部门','后端开发工程师',10000),('周想','技术部门','前端开发工程师',8000),('刘桂英','总裁办','总裁秘书',4500),('张海燕','总裁办','普通员工',3000),('何倩','总裁办','普通员工',3000),('李华','总裁办','普通员工',3000),('汪雪','销售部门','销售主管',4500),('王丹','销售部门','普通员工',2500),('黄辉','销售部门','普通员工',2500),('黄平','销售部门','普通员工',2500),('刘瑜','销售部门','普通员工',2500),('殷文','销售部门','普通员工',2500),('罗桂兰','销售部门','普通员工',2500),('高桂香','销售部门','普通员工',2500),('黄玉','销售部门','普通员工',2500),('张琴','销售部门','普通员工',2500),('李阳','销售部门','普通员工',2500),('丁娜','生产部门','生成主管',5000),('曲旭','生产部门','普通员工',3500),('冉兵','生产部门','普通员工',3500),('刘淑珍','生产部门','普通员工',3500),('陈丽','生产部门','普通员工',3500),('裴欢','生产部门','实习员',2500),('徐凯','生产部门','实习员',2500),('陈伟','生产部门','普通员工',3500),('梁玉华','生产部门','实习员',2500);
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-08 20:04:15
