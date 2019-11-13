-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
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
  INDEX `fk_table1_Business1_idx` (`Business_idBusiness` ASC) VISIBLE,
  CONSTRAINT `fk_table1_Usuarios`
    FOREIGN KEY (`Usuarios_idUsuarios`)
    REFERENCES `yelp`.`Usuarios` (`idUsuarios`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_table1_Business1`
    FOREIGN KEY (`Business_idBusiness`)
    REFERENCES `yelp`.`Business` (`idBusiness`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

