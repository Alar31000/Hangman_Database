CREATE TABLE WORDS (
words_id INT NOT NULL AUTO_INCREMENT,
mot VARCHAR(20)NOT NULL UNIQUE,
dico VARCHAR(255),
difficulte ENUM('F','M','D'),
PRIMARY KEY ( words_id )
);

CREATE TABLE sessions (
sessions_id INT NOT NULL AUTO_INCREMENT,
nombre_parties INT NOT NULL UNIQUE,
nombre_victoires INT,
nombre_defaites INT,
PRIMARY KEY ( sessions_id )
);

CREATE TABLE partie (
partie_id INT NOT NULL AUTO_INCREMENT,
username VARCHAR (20) NOT NULL,
mot INT NOT NULL UNIQUE,
nombre_essais INT NOT NULL,
nombre_essais_restants INT NOT NULL,
date_partie DATE NOT NULL,
PRIMARY KEY ( partie_id ),
FOREIGN KEY ( mot ) REFERENCES words(words_id) 
);


ALTER TABLE sessions
ADD partie INT NOT NULL UNIQUE,
ADD date_sessions DATE NOT NULL,
ADD FOREIGN KEY ( partie ) REFERENCES partie( partie_id );