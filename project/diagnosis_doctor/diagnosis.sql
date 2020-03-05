-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `book`
--
CREATE DATABASE IF NOT EXISTS `diagnosis` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `diagnosis`;

-- --------------------------------------------------------

DROP TABLE IF EXISTS `diagnosis`;
CREATE TABLE IF NOT EXISTS `diagnosis` (
  `QueueID` varchar(10) NOT NULL,
  `Registration_time` datetime NOT NULL,
  `NRIC` varchar(10) NOT NULL,
  `Initial_diagnosis` varchar(100),
  `Doctor_diagnosis` varchar(100),
  `Hospital` varchar(50) NOT NULL,
  `Nurse_IC` varchar(20) NOT NULL,
  `Doctor_IC` varchar(20) NOT NULL,
  `Nurse_cleared` BOOLEAN NOT NULL,
  `Severe` BOOLEAN,
  `Complete` BOOLEAN NOT NULL,
  PRIMARY KEY (`QueueID`, `Registration_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `diagnosis` (`QueueID`, `Registration_time`, `NRIC`, `Initial_diagnosis`, `Doctor_diagnosis`,
`Hospital`, `Nurse_IC`, `Doctor_IC`, `Nurse_cleared`, `Severe`, `Complete`) VALUES
('4907', '2020-03-01 12:15:00', 'S6964907Z', null, null, 'JJBufflord Hospital', 'Lai ShiHo', 'Dr Tan', FALSE, null, FALSE),
('4908', '2020-03-01 12:30:00', 'S6964908Z', null, null, 'JJBufflord Hospital', 'Lai ShiHo', 'Dr Tan', FALSE, null, FALSE);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
