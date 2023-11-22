PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE usuarios(
    name text primary key,
    password text not null
);
INSERT INTO usuarios VALUES('usuario1','password1');
INSERT INTO usuarios VALUES('user','pass');
INSERT INTO usuarios VALUES('admin','admin');
INSERT INTO usuarios VALUES('usuario','numero');
INSERT INTO usuarios VALUES('nombre','nombre');
CREATE TABLE entradas(
    id integer primary key autoincrement,
    name text not null,
    entrada text not null,
    publica boolean not null default false,

    FOREIGN KEY (name) REFERENCES usuarios (name)
);
INSERT INTO entradas VALUES(1,'user','Entrada de user: abcde',0);
INSERT INTO entradas VALUES(2,'admin','Entrada de admin 1: fghij',0);
INSERT INTO entradas VALUES(3,'admin','Entrada de admin 2: klmnÃ±',0);
INSERT INTO entradas VALUES(4,'usuario1','Entrada de usuario1: opqrs',0);
INSERT INTO entradas VALUES(5,'user','Entrada privada',0);
INSERT INTO entradas VALUES(6,'user','Entrada publica',1);
INSERT INTO entradas VALUES(7,'usuario','Entrada 2',0);
INSERT INTO entradas VALUES(8,'usuario','Entrada 1',1);
INSERT INTO entradas VALUES(9,'usuario','Entrada 2',1);
INSERT INTO entradas VALUES(10,'user','Nueva publica',1);
INSERT INTO entradas VALUES(11,'usuario1','Publica de usuario1',1);
INSERT INTO entradas VALUES(12,'usuario1','Nueva publica de usuario1',1);
INSERT INTO entradas VALUES(13,'nombre','Nueva entrada',0);
INSERT INTO entradas VALUES(14,'admin','Entrada de admin',1);
INSERT INTO entradas VALUES(15,'usuario','Entrada 1',0);
INSERT INTO entradas VALUES(16,'usuario','Entrada 3',1);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('entradas',16);
COMMIT;
