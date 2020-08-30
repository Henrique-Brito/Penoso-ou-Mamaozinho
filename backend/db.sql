

CREATE DATABASE teste;




CREATE TABLE users (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) ,
email VARCHAR(255) ,
username VARCHAR(255),
password  VARCHAR(255)
);

CREATE TABLE  disciplinas(
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255) ,
body VARCHAR(255) ,
author VARCHAR(255),
penoso  INT UNSIGNED,
mamao  INT UNSIGNED
);

CREATE TABLE avaliado (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
id_user INT(6) UNSIGNED ,
id_disciplinas INT(6) UNSIGNED   ,
FOREIGN KEY (id_user) REFERENCES users(id),
FOREIGN KEY (id_disciplinas) REFERENCES disciplinas(id)
);

CREATE TABLE comentario (
id INT(6)  UNSIGNED AUTO_INCREMENT PRIMARY KEY,
id_user INT(6)  UNSIGNED ,
id_disciplinas INT(6)  UNSIGNED  ,
texto VARCHAR(255) NOT NULL,
FOREIGN KEY(id_user) REFERENCES users(id),
FOREIGN KEY (id_disciplinas) REFERENCES disciplinas(id)
);


