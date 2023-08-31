/*
SQLyog 企业版 - MySQL GUI v8.14 
MySQL - 5.7.14-log : Database - weibo_db
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`weibo_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `weibo_db`;

/*Table structure for table `t_news` */

DROP TABLE IF EXISTS `t_news`;

CREATE TABLE `t_news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `oid` varchar(20) DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `intro` varchar(800) DEFAULT NULL,
  `media_name` varchar(64) DEFAULT NULL,
  `keywords` varchar(200) DEFAULT NULL,
  `ctime` varchar(20) DEFAULT NULL,
  `url` varchar(200) DEFAULT NULL,
  `wapurls` varchar(500) DEFAULT NULL,
  `content` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `oid` (`oid`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
