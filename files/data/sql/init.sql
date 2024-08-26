-- --------------------------------------------------------
-- Host:                         192.168.70.7
-- Server version:               10.6.18-MariaDB-0ubuntu0.22.04.1 - Ubuntu 22.04
-- Server OS:                    debian-linux-gnu
-- HeidiSQL Version:             12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table db.bigvolume
CREATE TABLE `bigvolume` (
	`id` VARCHAR(50) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
	`id_symbol` VARCHAR(50) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
	`status_open` INT(11) NOT NULL DEFAULT '1',
	PRIMARY KEY (`id`) USING BTREE,
	INDEX `status_open` (`status_open`) USING BTREE,
	INDEX `id_symbol` (`id_symbol`) USING BTREE
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
-- Data exporting was unselected.

-- Dumping structure for table db.signals
CREATE TABLE IF NOT EXISTS `signals` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `symbol` varchar(50) NOT NULL DEFAULT '',
  `waktu` datetime NOT NULL,
  `metod` int(11) NOT NULL,
  `open` float NOT NULL DEFAULT 0,
  `high` float NOT NULL DEFAULT 0,
  `low` float NOT NULL DEFAULT 0,
  `close` float NOT NULL DEFAULT 0,
  `volume` float NOT NULL DEFAULT 0,
  `stoploss` float NOT NULL DEFAULT 0,
  `takeprofit` float NOT NULL DEFAULT 0,
  `status_open` int(11) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `symbol` (`symbol`) USING BTREE,
  KEY `metod` (`metod`) USING BTREE,
  KEY `waktu` (`waktu`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Data exporting was unselected.

-- Dumping structure for table db.symbol
CREATE TABLE IF NOT EXISTS `symbol` (
  `id` varchar(50) NOT NULL DEFAULT '',
  `symbol` varchar(50) NOT NULL DEFAULT '',
  `timeframe` int(11) NOT NULL DEFAULT 0,
  `waktu` datetime NOT NULL,
  `waktu_date` date NOT NULL,
  `waktu_time` time NOT NULL,
  `open` float NOT NULL DEFAULT 0,
  `high` float NOT NULL DEFAULT 0,
  `low` float NOT NULL DEFAULT 0,
  `close` float NOT NULL DEFAULT 0,
  `volume` float NOT NULL DEFAULT 0,
  `volume_ma` float NOT NULL DEFAULT 0,
  `volume_delta` float NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `symbol` (`symbol`) USING BTREE,
  KEY `timeframe` (`timeframe`) USING BTREE,
  KEY `waktu` (`waktu`) USING BTREE,
  KEY `waktu_date` (`waktu_date`) USING BTREE,
  KEY `waktu_time` (`waktu_time`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Data exporting was unselected.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
