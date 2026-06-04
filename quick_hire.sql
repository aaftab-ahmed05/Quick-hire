-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 23, 2025 at 07:10 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quick hire`
--

-- --------------------------------------------------------

--
-- Table structure for table `addjobs`
--

CREATE TABLE `addjobs` (
  `department` varchar(30) NOT NULL,
  `job_id` varchar(4) NOT NULL,
  `job_title` varchar(30) NOT NULL,
  `vacancies` int(4) NOT NULL,
  `last_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `addjobs`
--

INSERT INTO `addjobs` (`department`, `job_id`, `job_title`, `vacancies`, `last_date`) VALUES
('IT', '1001', 'Software Developer', 8, '2025-10-22'),
('IT', '1002', 'web developer', 10, '2025-07-08'),
('Finance & Accounting', '1003', 'Accountant', 2, '2025-09-18'),
('Design', '1004', 'Graphic Designer', 4, '2025-10-08'),
('HR', '1005', 'Resourse Manager', 2, '2025-11-12');

-- --------------------------------------------------------

--
-- Table structure for table `applicants`
--

CREATE TABLE `applicants` (
  `id` int(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `dob` date NOT NULL,
  `phone` bigint(10) NOT NULL,
  `email` varchar(40) NOT NULL,
  `address` varchar(100) NOT NULL,
  `department` varchar(30) NOT NULL,
  `jobselected` varchar(30) NOT NULL,
  `qualification` varchar(20) NOT NULL,
  `skills` varchar(50) NOT NULL,
  `applicant_image` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `applicants`
--

INSERT INTO `applicants` (`id`, `name`, `gender`, `dob`, `phone`, `email`, `address`, `department`, `jobselected`, `qualification`, `skills`, `applicant_image`) VALUES
(1001, 'David', 'Male', '2000-07-05', 9565684875, 'david@gmail.com', 'Main street 12, H.No. 78,Delhi\n', 'IT', 'Software Developer', 'B.Tech', 'Java, Mysql, DSA\n', '43342face2.jpeg'),
(1002, 'Aman', 'Male', '2001-05-16', 8545672564, 'aman34@gmail.com', 'H.No. 65, Modal Town, Jalandhar,Punjab \n', 'Design', 'Graphic Designer', 'BCA', 'Adobe Photoshope\n', '43625facee3.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `username` varchar(30) NOT NULL,
  `password` int(8) NOT NULL,
  `user_type` varchar(5) NOT NULL,
  `user_image` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`username`, `password`, `user_type`, `user_image`) VALUES
('aaftab', 1234, 'Admin', '43239captured_image.png'),
('user1', 1000, 'User', '43299face2.jpeg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addjobs`
--
ALTER TABLE `addjobs`
  ADD PRIMARY KEY (`job_id`),
  ADD UNIQUE KEY `job_title` (`job_title`);

--
-- Indexes for table `applicants`
--
ALTER TABLE `applicants`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
