-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: localhost    Database: prototipo
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `fluxo_caixa`
--

DROP TABLE IF EXISTS `fluxo_caixa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fluxo_caixa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `transação` text NOT NULL,
  `data` date NOT NULL,
  `valor` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fluxo_caixa`
--

LOCK TABLES `fluxo_caixa` WRITE;
/*!40000 ALTER TABLE `fluxo_caixa` DISABLE KEYS */;
INSERT INTO `fluxo_caixa` VALUES (1,'investimento inicial','2021-12-01',1000000);
/*!40000 ALTER TABLE `fluxo_caixa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fornecedores`
--

DROP TABLE IF EXISTS `fornecedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fornecedores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(70) NOT NULL,
  `endereço` varchar(70) NOT NULL,
  `cnpj` varchar(14) NOT NULL,
  `email` varchar(70) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fornecedores`
--

LOCK TABLES `fornecedores` WRITE;
/*!40000 ALTER TABLE `fornecedores` DISABLE KEYS */;
INSERT INTO `fornecedores` VALUES (1,'Fornecedor 1','Rua 1 n 111 Bairro 1','12345','vinicius.gabriel@usp.br'),(2,'Fornecedor 2','Rua 2 n 222 Bairro 2','54321','vinicius.gabriel@usp.br'),(3,'Fornecedor 3','Rua 3 n 333 Bairro 3','33333','bru020@usp.br'),(4,'Fornecedor 4','Rua 4 n 444 Bairro 4','44444','kaua.machado@usp.br'),(5,'Fornecedor 5','Rua 5 n 555 Bairro 5 ','55555','vinicius.gabriel@usp.br'),(6,'Fornecedor 6','Rua 6 n 666 Bairro 6','66666','vinicius.gabriel@usp.br');
/*!40000 ALTER TABLE `fornecedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionarios`
--

DROP TABLE IF EXISTS `funcionarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(70) NOT NULL,
  `cargo` varchar(30) NOT NULL,
  `salario` float(9,2) NOT NULL,
  `cpf` bigint NOT NULL,
  `telefone` varchar(13) NOT NULL,
  `email` varchar(70) NOT NULL,
  `admissao` date DEFAULT NULL,
  `hist_pagamento` text,
  `senha` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionarios`
--

LOCK TABLES `funcionarios` WRITE;
/*!40000 ALTER TABLE `funcionarios` DISABLE KEYS */;
INSERT INTO `funcionarios` VALUES (1,'inicial','Gerente',0.00,0,'-','-','2021-12-01','-','senha'),(2,'Bruno','Caixa',2300.00,20505286555,'84515596','bruno@gmail.com','2021-12-01',NULL,'senha'),(3,'Luana','Contadora',2700.00,95623585447,'99652517','luana@gmail.com','2021-12-01',NULL,'senha'),(4,'Vinicius','Gerente',137890.00,3960863224,'93964158','vinicius@gmail.com','2021-12-01',NULL,'senha'),(5,'Kauã','Analista',3100.00,84512697751,'62553247','kaua@gmail.com','2021-12-01',NULL,'senha'),(6,'Gustavo','Segurança',3400.00,75596325874,'55632479','gustavo@gmail.com','2021-12-01',NULL,'senha');
/*!40000 ALTER TABLE `funcionarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `horario_compra`
--

DROP TABLE IF EXISTS `horario_compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `horario_compra` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data` date DEFAULT NULL,
  `dia` varchar(9) DEFAULT NULL,
  `horário` time DEFAULT NULL,
  `valor` float(9,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horario_compra`
--

LOCK TABLES `horario_compra` WRITE;
/*!40000 ALTER TABLE `horario_compra` DISABLE KEYS */;
INSERT INTO `horario_compra` VALUES (1,'2021-11-01','Monday','04:10:00',104.12),(2,'2021-11-01','Monday','04:10:00',71.79),(3,'2021-11-19','Friday','18:17:00',18.85);
/*!40000 ALTER TABLE `horario_compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos`
--

DROP TABLE IF EXISTS `pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pedido` text,
  `data_emissão` date NOT NULL,
  `data_entregue` date DEFAULT NULL,
  `valor` float(9,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos`
--

LOCK TABLES `pedidos` WRITE;
/*!40000 ALTER TABLE `pedidos` DISABLE KEYS */;
INSERT INTO `pedidos` VALUES (1,'[[\'cerveja\', 1.8, 30], [\'farofa\', 3.75, 30], [\'bolacha\', 2.2, 40], [\'lata de ervilha\', 1.5, 20]]','2021-10-26','2021-10-29',284.50),(2,'[[\'suco de uva\', 3.25, 20], [\'carvao\', 12.3, 30]]','2021-10-26','2021-10-29',434.00),(3,'[[\'caixa de leite\', 1.8, 20], [\'pao de forma\', 3.3, 20], [\'carvao\', 12.3, 15]]','2021-10-27','2021-10-29',286.50),(4,'[[\'suco de uva\', 3.25, 20], [\'pao de forma\', 3.3, 15], [\'carvao\', 12.3, 20]]','2021-10-28','2021-10-29',360.50),(5,'[[\'caixa de leite\', 1.8, 20], [\'bombom\', 0.5, 20], [\'lasanha\', 8.0, 15]]','2021-10-29','2021-10-29',166.00),(6,'[[\'saco de lixo\', 2.0, 30]]','2021-10-29','2021-10-29',60.00),(7,'[[\'lata de ervilha\', 1.5, 30], [\'carvao\', 12.3, 20]]','2021-10-30','2021-10-30',291.00),(8,'[[\'farofa\', 3.75, 100], [\'suco de uva\', 3.25, 30], [\'pao de forma\', 3.3, 40]]','2021-11-01','2021-11-01',604.50),(9,'[[\'caixa de leite\', 1.8, 10], [\'suco de uva\', 3.25, 10], [\'pao de forma\', 3.3, 30]]','2021-11-03','2021-11-28',149.50),(10,'[[\'lata de ervilha\', 1.5, 15], [\'farofa\', 3.75, 15], [\'esponja\', 0.45, 35], [\'vassoura\', 7.49, 28], [\'caderno\', 3.19, 20], [\'caixa de ovos\', 8.99, 40]]','2021-11-26','2021-11-28',727.62),(11,'[[\'caixa de ovos\', 8.99, 17], [\'vassoura\', 7.49, 23]]','2021-11-26','2021-11-28',325.10),(12,'[[\'vassoura\', 7.49, 21], [\'esponja\', 0.45, 19]]','2021-11-26','2021-11-28',165.84),(13,'[[\'lata de ervilha\', 1.5, 16], [\'bolacha\', 2.2, 12]]','2021-11-26','2021-11-28',50.40),(14,'[[\'suco de uva\', 3.25, 1]]','2021-11-26',NULL,3.25),(15,'[[\'pao de forma\', 3.3, 2]]','2021-11-26',NULL,6.60),(16,'[[\'caixa de ovos\', 8.99, 31], [\'esponja\', 0.45, 24], [\'farofa\', 3.75, 13]]','2021-11-26','2021-11-28',338.24),(17,'[[\'farofa\', 3.75, 12], [\'carvao\', 12.3, 25], [\'caderno\', 3.19, 30], [\'vassoura\', 7.49, 20]]','2021-11-26','2021-11-28',598.00);
/*!40000 ALTER TABLE `pedidos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produto`
--

DROP TABLE IF EXISTS `produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produto` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `codigo` int DEFAULT NULL,
  `custo` float(9,2) NOT NULL,
  `preço` float(9,2) NOT NULL,
  `lucro` float(9,2) NOT NULL,
  `estoque` bigint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produto`
--

LOCK TABLES `produto` WRITE;
/*!40000 ALTER TABLE `produto` DISABLE KEYS */;
INSERT INTO `produto` VALUES (1,'bolacha',100,2.20,3.00,0.80,70),(2,'bombom',101,0.50,1.00,0.50,23),(3,'lata de ervilha',102,1.50,2.35,0.85,87),(4,'suco de uva',103,3.25,5.00,1.75,153),(5,'pao de forma',104,3.30,5.50,2.20,335),(6,'lasanha',105,8.00,11.75,3.75,16),(7,'cerveja',106,1.80,2.69,0.89,64),(8,'saco de lixo',107,2.00,5.60,3.60,34),(9,'caixa de leite',108,1.80,3.49,1.69,121),(10,'farofa',109,3.75,6.00,2.25,193),(11,'carvao',110,12.30,19.75,7.45,109),(12,'esponja',111,0.45,0.90,0.45,75),(13,'vassoura',112,7.49,11.35,3.86,115),(14,'caderno',113,3.19,6.89,3.70,50),(15,'caixa de ovos',114,8.99,11.35,2.36,101);
/*!40000 ALTER TABLE `produto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-01 22:14:23
