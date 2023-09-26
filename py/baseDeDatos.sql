-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`usuarios`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`usuarios` ;

CREATE TABLE IF NOT EXISTS `mydb`.`usuarios` (
  `idusuarios` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(20) NOT NULL,
  `apellido` VARCHAR(30) NOT NULL,
  `email` VARCHAR(65) NOT NULL,
  `clave` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idusuarios`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`publicaciones`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`publicaciones` ;

CREATE TABLE IF NOT EXISTS `mydb`.`publicaciones` (
  `id_publicaciones` INT NOT NULL AUTO_INCREMENT,
  `contenido` VARCHAR(50) NOT NULL,
  `pieDeFoto` VARCHAR(45) NOT NULL,
  `recuentoDeLikes` INT NOT NULL,
  PRIMARY KEY (`id_publicaciones`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`usuarios_has_publicaciones`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`usuarios_has_publicaciones` ;

CREATE TABLE IF NOT EXISTS `mydb`.`usuarios_has_publicaciones` (
  `usuarios_idusuarios` INT NOT NULL,
  `publicaciones_id_publicaciones` INT NOT NULL,
  PRIMARY KEY (`usuarios_idusuarios`, `publicaciones_id_publicaciones`),
  CONSTRAINT `fk_usuarios_has_publicaciones_usuarios`
    FOREIGN KEY (`usuarios_idusuarios`)
    REFERENCES `mydb`.`usuarios` (`idusuarios`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_publicaciones_publicaciones1`
    FOREIGN KEY (`publicaciones_id_publicaciones`)
    REFERENCES `mydb`.`publicaciones` (`id_publicaciones`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`comentarios|`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`comentarios|` ;

CREATE TABLE IF NOT EXISTS `mydb`.`comentarios|` (
  `idcomentarios|` INT NOT NULL AUTO_INCREMENT,
  `comentario` VARCHAR(45) NOT NULL,
  `publicaciones_id_publicaciones` INT NULL,
  PRIMARY KEY (`idcomentarios|`, `publicaciones_id_publicaciones`),
  CONSTRAINT `fk_comentarios|_publicaciones1`
    FOREIGN KEY (`publicaciones_id_publicaciones`)
    REFERENCES `mydb`.`publicaciones` (`id_publicaciones`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
