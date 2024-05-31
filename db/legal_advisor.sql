-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 11, 2020 at 11:13 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `legal_advisor`
--

-- --------------------------------------------------------

--
-- Table structure for table `advocate`
--

CREATE TABLE IF NOT EXISTS `advocate` (
  `adv_id` int(100) NOT NULL AUTO_INCREMENT,
  `adv_img` varchar(100) DEFAULT NULL,
  `adv_name` varchar(100) DEFAULT NULL,
  `adv_enroll_no` varchar(100) DEFAULT NULL,
  `adv_qual` varchar(100) DEFAULT NULL,
  `adv_age` varchar(100) DEFAULT NULL,
  `adv_gender` varchar(100) DEFAULT NULL,
  `adv_email` varchar(100) DEFAULT NULL,
  `adv_phone` varchar(100) DEFAULT NULL,
  `adv_address` varchar(100) DEFAULT NULL,
  `adv_category` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`adv_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `advocate`
--

INSERT INTO `advocate` (`adv_id`, `adv_img`, `adv_name`, `adv_enroll_no`, `adv_qual`, `adv_age`, `adv_gender`, `adv_email`, `adv_phone`, `adv_address`, `adv_category`) VALUES
(5, 'static/Media/download_DAgcNnV.jpg', 'Aneeja', 'k/222/2', 'aadasfsdfshjh', '23', 'female', 'aneeja@gmail.com', '9074368129', 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', 'Civil Cases'),
(7, 'static/Media/images%20(1)_HIB4FBn.jpg', 'Akbersha', 'k/111/10', 'aaaaaa', '50', 'male', 'akbersha@gmail.com', '8089186044', 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', 'Bail Applications.'),
(8, 'static/Media/bg21.jpg', 'Vishnu', 'k/333/', 'asafaf', '23', 'male', 'vishnu@gmail.com', '9746249297', 'dgfggja', 'Domestic Relations'),
(11, 'static/Media/1.0.png', 'aneejaaa', 'k/110/28', 'sdfsdfs', '23', 'male', 'aneejaaa@gmail.com', '8978796869', 'gh', 'Criminal Cases');

-- --------------------------------------------------------

--
-- Table structure for table `case_request`
--

CREATE TABLE IF NOT EXISTS `case_request` (
  `case_id` int(100) NOT NULL AUTO_INCREMENT,
  `adv_id` varchar(100) DEFAULT NULL,
  `user_id` varchar(100) DEFAULT NULL,
  `case_title` varchar(100) DEFAULT NULL,
  `case_desc` varchar(100) DEFAULT NULL,
  `case_file` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `ipc_sections` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`case_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `case_request`
--

INSERT INTO `case_request` (`case_id`, `adv_id`, `user_id`, `case_title`, `case_desc`, `case_file`, `status`, `ipc_sections`) VALUES
(1, '7', '5', 'Educational Loan', 'shjahjhdj', 'static/Media/how_to_apply.pdf', 'Completed', 'section 125, 260A'),
(2, '5', '5', 'private bus rude driving', 'request you to please accept my application', 'static/Media/global%20medifile%20usecase%20diagram.docx', 'Applied', NULL),
(3, '5', '7', 'motor', 'sdgfjgfgagk', 'static/Media/Screenshot%20(43).png', 'Proceeding', 'Section 23, Section 44');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE IF NOT EXISTS `category` (
  `cat_id` int(100) NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(100) DEFAULT NULL,
  `cat_description` varchar(500) NOT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`cat_id`, `cat_name`, `cat_description`) VALUES
(3, 'Civil Cases', ''),
(4, 'Criminal Cases', ''),
(5, 'Bail Applications.', ''),
(7, 'Common', ''),
(8, 'Domestic Relations', 'adafafjagfkjgaf'),
(9, 'aaaaaaaa', 'dsdfdhgjdjjgf');

-- --------------------------------------------------------

--
-- Table structure for table `documents`
--

CREATE TABLE IF NOT EXISTS `documents` (
  `doc_id` int(100) NOT NULL AUTO_INCREMENT,
  `case_id` varchar(100) DEFAULT NULL,
  `u_id` varchar(100) DEFAULT NULL,
  `adv_id` varchar(100) DEFAULT NULL,
  `doc_name` varchar(100) DEFAULT NULL,
  `document` varchar(100) DEFAULT NULL,
  `posted_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`doc_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `documents`
--

INSERT INTO `documents` (`doc_id`, `case_id`, `u_id`, `adv_id`, `doc_name`, `document`, `posted_date`) VALUES
(1, '1', '5', '7', 'doc1', 'static/Media/Ananya_Musical....._ZEJgQGNZ_U9rsFWA.jpg', '2019-12-29'),
(2, '1', '5', '7', 'doc2', 'static/Media/Ananya_Musical....._ZEJgQGNZ_FUVX2Lz.jpg', '2019-12-29'),
(3, '3', '7', '5', 'doc100', 'static/Media/1.0_jeCkOos.png', '2019-12-30');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `feed_id` int(100) NOT NULL AUTO_INCREMENT,
  `u_id` varchar(100) DEFAULT NULL,
  `feed_subject` varchar(100) DEFAULT NULL,
  `feed_description` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `posted_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`feed_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`feed_id`, `u_id`, `feed_subject`, `feed_description`, `type`, `posted_date`) VALUES
(1, '5', 'Ipc', 'Please add some more ipc sessions', 'user', '2019-12-28'),
(2, '7', 'About Case category', 'I request you to add more case categories.. I hope will consider my request.', 'advocate', '2019-12-28'),
(3, '8', 'dfsdf', 'fsfsf', 'advocate', '2019-12-30'),
(4, '5', 'case detials', 'dfghjkjhg', 'user', '2019-12-30'),
(5, '5', 'happy', 'on going', 'user', '2019-12-30'),
(6, '8', 'aaaaa', 'ssdsdsdfsfs', 'advocate', '2019-12-30'),
(7, '8', 'details about cases', 'sdmadbmabma', 'advocate', '2019-12-30'),
(8, '5', 'aaaa', 'hfghhgjg', 'user', '2019-12-30');

-- --------------------------------------------------------

--
-- Table structure for table `ipc`
--

CREATE TABLE IF NOT EXISTS `ipc` (
  `ipc_id` int(100) NOT NULL AUTO_INCREMENT,
  `ipc_section` varchar(100) DEFAULT NULL,
  `ipc_description` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`ipc_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `ipc`
--

INSERT INTO `ipc` (`ipc_id`, `ipc_section`, `ipc_description`) VALUES
(1, 'Section 129B', 'CRiminal punishment : .hfdghdgshgbxncbnzxbvz,'),
(4, 'Section 150', 'sfhgjdfjs'),
(5, 'Section 1', 'This Act shall be called the Indian Penal Code, and shall extend to the whole of India except the State of Jammu and Kashmir.'),
(6, 'Section 2', 'Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within India.'),
(7, 'Section 59', 'ashdahdad');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `log_id` int(100) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=21 ;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`log_id`, `user_id`, `username`, `password`, `type`, `status`) VALUES
(1, '0', 'admin', 'admin123', 'admin', '1'),
(9, '5', 'aneeja@gmail.com', 'aneeja', 'advocate', '1'),
(11, '4', 'disha@gmail.com', 'dishadisha', 'user', '1'),
(12, '5', 'meenu@gmail.com', 'meenu', 'user', '1'),
(13, '7', 'akbersha@gmail.com', 'akber', 'advocate', '1'),
(14, '6', 'priya@gmail.com', 'priya', 'user', '1'),
(15, '8', 'vishnu@gmail.com', 'vishu', 'advocate', '1'),
(17, '7', 'ammu@gmail.com', '9856322222', 'user', '1'),
(19, '11', 'aneejaaa@gmail.com', 'aaa', 'advocate', '1'),
(20, '8', 'abi@gmail.com', '9999999999', 'user', '0');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE IF NOT EXISTS `payment` (
  `pay_id` int(100) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) DEFAULT NULL,
  `adv_id` varchar(100) DEFAULT NULL,
  `case_id` varchar(100) DEFAULT NULL,
  `posted_date` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `paid_date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`pay_id`, `user_id`, `adv_id`, `case_id`, `posted_date`, `amount`, `paid_date`, `status`) VALUES
(2, '5', '7', '1', '2019-12-28', '2500', '2019-12-30', 'Paid'),
(3, '5', '7', '1', '2019-12-29', '3000', '2019-12-30', 'Paid'),
(4, '7', '5', '3', '2019-12-30', '1000', '2019-12-30', 'Paid');

-- --------------------------------------------------------

--
-- Table structure for table `rating`
--

CREATE TABLE IF NOT EXISTS `rating` (
  `rate_id` int(100) NOT NULL AUTO_INCREMENT,
  `case_id` varchar(100) NOT NULL,
  `user_id` varchar(100) NOT NULL,
  `adv_id` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `rate_desc` varchar(100) NOT NULL,
  PRIMARY KEY (`rate_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `rating`
--

INSERT INTO `rating` (`rate_id`, `case_id`, `user_id`, `adv_id`, `rating`, `rate_desc`) VALUES
(1, '1', '5', '7', '6', 'fafa'),
(3, '2', '5', '5', '10', 'aaa');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `u_id` int(100) NOT NULL AUTO_INCREMENT,
  `u_img` varchar(100) DEFAULT NULL,
  `u_name` varchar(100) DEFAULT NULL,
  `u_age` varchar(100) DEFAULT NULL,
  `u_gender` varchar(100) DEFAULT NULL,
  `u_email` varchar(100) DEFAULT NULL,
  `u_phone` varchar(100) DEFAULT NULL,
  `u_aadhar` varchar(50) NOT NULL,
  `u_address` varchar(100) DEFAULT NULL,
  `u_account` varchar(100) DEFAULT NULL,
  `u_cvv` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`u_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`u_id`, `u_img`, `u_name`, `u_age`, `u_gender`, `u_email`, `u_phone`, `u_aadhar`, `u_address`, `u_account`, `u_cvv`) VALUES
(4, 'static/Media/images%20(1)_fglNRHz.jpg', 'Disha', '34', 'female', 'disha@gmail.com', '8089186044', '', 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', '12345678888', '4321'),
(5, 'static/Media/images_4fa6Zmj.jpg', 'Meenu ', '25', 'female', 'meenu@gmail.com', '9567818280', '', 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', '12345677889997', '1234'),
(6, 'static/Media/EliasSuelaine_image_ZEFrQWFY_PEIAGGy.jpg', 'Priya ', '23', 'female', 'priya@gmail.com', '8848956474', '', 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', '12345678233333', '11223'),
(7, 'static/Media/Screenshot%20(38).png', 'Ammu', '22', 'female', 'ammu@gmail.com', '', '', 'sdafhah', '56666663744', '1111'),
(8, 'static/Media/legal.jpg', 'abi', '45', 'male', 'abi@gmail.com', '9999999999', '236589652145', 'fghj', '223659874525256', '2365');
