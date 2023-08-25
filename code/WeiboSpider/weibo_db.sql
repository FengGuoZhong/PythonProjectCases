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

/*Table structure for table `t_weibo` */

DROP TABLE IF EXISTS `t_weibo`;

CREATE TABLE `t_weibo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `weibo_id` varchar(20) DEFAULT NULL COMMENT '微博ID',
  `user_id` varchar(20) DEFAULT NULL COMMENT '发布人ID',
  `screen_name` varchar(100) DEFAULT NULL COMMENT '发布人昵称',
  `created_at` varchar(50) DEFAULT NULL COMMENT '发布时间',
  `region_name` varchar(20) DEFAULT NULL COMMENT '发布地点',
  `source` varchar(64) DEFAULT NULL COMMENT '来源',
  `text` mediumtext COMMENT '内容',
  `reposts_count` int(11) DEFAULT '0' COMMENT '转发数',
  `comments_count` int(11) DEFAULT '0' COMMENT '评论数',
  `attitudes_count` int(11) DEFAULT '0' COMMENT '点赞数',
  `pic_num` int(11) DEFAULT '0' COMMENT '图片数',
  `pic` varchar(800) DEFAULT NULL COMMENT '图片',
  `media_video` varchar(200) DEFAULT NULL COMMENT '视频',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 CHECKSUM=1 DELAY_KEY_WRITE=1 ROW_FORMAT=DYNAMIC;

/*Data for the table `t_weibo` */

LOCK TABLES `t_weibo` WRITE;

UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
