DROP database IF EXISTS yelp;


CREATE SCHEMA IF NOT EXISTS `yelp` DEFAULT CHARACTER SET utf8 ;
USE `yelp` ;

-- -----------------------------------------------------
-- Table `mydb`.`Usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `yelp`.`Usuarios` (
  `idUsuarios` INT NOT NULL,
  PRIMARY KEY (`idUsuarios`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Business`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `yelp`.`Business` (
  `idBusiness` INT NOT NULL,
  `categoria` VARCHAR(45) NULL,
  `latitude` DOUBLE NULL,
  `longitude` DOUBLE NULL,
  `media_review` FLOAT NULL,
  `desv_pad` FLOAT NULL,
  PRIMARY KEY (`idBusiness`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Usuarios_Business`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `yelp`.`Usuarios_Business` (
  `Usuarios_idUsuarios` INT NOT NULL,
  `Business_idBusiness` INT NOT NULL,
  PRIMARY KEY (`Usuarios_idUsuarios`, `Business_idBusiness`),
  FOREIGN KEY(`Usuarios_idUsuarios`) REFERENCES Usuarios(`idUsuarios`))