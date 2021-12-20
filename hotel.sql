-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 20, 2021 at 05:18 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.3.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel`
--

-- --------------------------------------------------------

--
-- Table structure for table `checkin`
--

CREATE TABLE `checkin` (
  `Phoneno` varchar(20) NOT NULL,
  `date` varchar(25) NOT NULL,
  `ndays` varchar(11) NOT NULL,
  `roomtype` varchar(11) NOT NULL,
  `roomno` varchar(11) NOT NULL,
  `adults` varchar(11) NOT NULL,
  `children` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `checkin`
--

INSERT INTO `checkin` (`Phoneno`, `date`, `ndays`, `roomtype`, `roomno`, `adults`, `children`) VALUES
('789456123', '13/10/2021', '4', 'DOUBLE', '67', '2', '4');

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `name` varchar(20) NOT NULL,
  `Phoneno` varchar(25) NOT NULL,
  `Gmail` varchar(25) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `country` varchar(20) NOT NULL,
  `id` varchar(20) NOT NULL,
  `idnumber` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`name`, `Phoneno`, `Gmail`, `Address`, `country`, `id`, `idnumber`) VALUES
('Ashish', '8566077814', 'Ash@gmail.com', 'Ludhiana', 'India', 'AADHAR CARD', '4561225465455'),
('Abhishek', '9023678376', 'Abhi@gmail.com', 'Ludhiana', 'India', 'AADHAR CARD', '1245632589'),
('Abhishek', '789456123', 'abhi@gmail.com', 'Ludhiana', 'india', 'VOTER ID', '561452356798');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `checkin`
--
ALTER TABLE `checkin`
  ADD PRIMARY KEY (`roomno`),
  ADD UNIQUE KEY `Phoneno` (`Phoneno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
