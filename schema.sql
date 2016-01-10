CREATE DATABASE  IF NOT EXISTS `movie_guess` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `movie_guess`;

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
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `synopsis` text NOT NULL,
  `poster` varchar(512) NOT NULL,
  `rating` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES (1,'Djävulen bär Prada (2006)','Andrea Sachs har just fått ett jobb som många unga kvinnor skulle döda för. Hon har fått anställning som assistent till den legendariska och oerhört krävande modedrottningen Miranda Priestly på en av New Yorks största tidningar. Andy har egentligen siktet inställt på att bli journalist, men bestämmer sig för att först ta sig an modevärldens utmaningar.','prada.jpg',7),(2,'Natt på museet (2006)','Larry Daley har svårt att binda sig vid ett jobb. När han så tar ett jobb som nattvakt på ett museum har han ingen aning vilken överraskning som väntar honom - allt i museet väcks till liv på natten.','museet.jpg',6),(3,'Fight Club (1999)','Vår berättare lever ett vanligt liv och hatar det. En dag träffar han Tyler Durden som anser att det bara är genom smärtan och kampen som en man kan känna att han lever. Tillsammans startar de en hemlig klubb där unga män får utlopp för sina frustrationer genom slagsmål.','fightclub.jpg',9),(4,'Teenage Mutant Ninja Turtles (2014)','Mörkret har lagt sig över New York City. Shredder och hans ondskefulla Foot Clan har tagit ett järngrepp om allt från poliser till politiker. Framtiden ser hopplös och dyster ut tills en kvartett muterade reptilkrigare reser sig ur kloakerna för att agera i rättfärdighetens namn. Sköldpaddorna måste arbeta tillsammans med den tappra journalisten April O\'Neill och hennes kameraman Vern Fenwick för att rädda staden och avslöja Shredders diaboliska planer.','tmnt.jpg',6),(5,'Star Wars: Episod I - Det mörka hotet (1999)','En handelsfederation ledd av Nute Gunray planerar att ta över den fredliga planeten Naboo. Jedikrigarna Qui-Gon Jinn och Obi-Wan Kenobi skickas för att konfrontera ledarna, men allt går inte som planerat. Jediriddarna lyckas rymma, och tillsammans med sin nyfunna vän Jar Jar Binks beger de sig till Naboo för att varna drottning Amidala. Droider har dock redan börjat inta planeten och eftersom drottningen inte längre är säker där bestämmer de sig för att fly. Efter problem med skeppet tvingas de landa på ökenplaneten Tatooine för reparationer, där de möter en nioårig slavpojke vid namn Anakin Skywalker.','starwars.png',7),(6,'Jack and Jill (2011)','Jack Sadelstein är en framgångsrik reklamchef i Los Angeles som har en vacker fru, fina barn och en sak som han fasar för varje år: att få besök av sin tvillingsyster Jill. Jills bekräftelsebehov och passiva aggressivitet gör Jack vansinnig och vänder upp och ned på hans vanligtvis stillsamma liv. Saker och ting glider Jack ännu mer ur händerna när Jill bestämmer sig för att stanna längre och han börjar tro att hon aldrig tänker åka hem.','jackjill.jpg',3),(7,'Twilight (2008)','Isabella Swan flyttar till Forks, en liten regnig sovstad i Washington, Hon förväntar sig att hennes nya liv ska bli lika långtråkigt som staden själv. Men när hon träffar den gåtfulla och förföriska Edward Cullen tar hennes liv en oväntad och farlig vändning. Edward har länge lyckats hålla sin identitet som vampyr hemlig, men nu går ingen säker, minst av allt Bella, som är den person Edward älskar mer än någon annan. Edward och Bellas förhållande balanserar på knivseggen mellan begär och livsfara. Twilight är baserad på Stephenie Meyers succéroman Om jag kunde drömma.','twilight.jpg',5),(8,'Frozen (2013)','Kungariket Arendelles prinsessor Elsa och Anna har länge levt i isolering för att Elsa som barn inte kunde kontrollera sin ismagi. När deras föräldrar dör och Elsa kröns till drottning förlorar hon kontrollen igen och råkar frysa hela kungariket. Hon flyr mot bergen efter att ha sett folkets reaktion och Anna måste hitta henne och övertyga henne om att låta sommaren komma tillbaka. Till sin hjälp har hon Kristoff, hans ren Sven och snögubben Olaf.','frozen.jpg',8),(9,'American Pie (1999)','Det är sista terminen i stadens lilla high school och vårbalen är i antågande. Detta i sig är nog en befrielse, om det inte vore för att hälften av eleverna mot sin vilja fortfarande är oskulder. Fyra killar sluter en pakt: svendomen ska väck innan balen med alla medel som står till buds.','americanpie.jpg',7),(10,'50 Shades of Grey (2015)','Litteraturstudenten Anastasia Steele går med på att intervjua miljardären Christian Grey för att göra sin rumskompis en tjänst. Intervjuoffret visar sig vara en man som är både vacker och intelligent, men också en aning överlägsen. Den naiva Ana och den reserverade Christian dras ohjälpligt till varandra. Hon kan inte motstå honom och han vill ha henne, men på sina egna villkor. Ana tvekar när hon under den framgångsrike Christians yta anar en man som har ett kontrollbehov på gränsen till besatthet. Men ju närmare de kommer varandra, desto mer upptäcker Ana inte bara av Christians hemligheter, utan även sidor hon själv inte visste att hon hade.','50shades.jpg',4);
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guesses`
--

DROP TABLE IF EXISTS `guesses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `guesses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `guess` varchar(45) NOT NULL,
  `user_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `diff` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `no_duplicates` (`movie_id`,`user_id`),
  KEY `user_id_idx` (`user_id`),
  KEY `movie_id_idx` (`movie_id`),
  CONSTRAINT `movie_id` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK TABLES `guesses` WRITE;
/*!40000 ALTER TABLE `guesses` DISABLE KEYS */;
/*!40000 ALTER TABLE `guesses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `score` decimal(10,0) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;