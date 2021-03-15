-- AUTOR --

INSERT INTO autor (id, apellidos, nombres, fechanacimiento) VALUES (NULL, 'Vallejo Mendoza', 'César Abraham', '1892-03-16');
INSERT INTO autor (id, apellidos, nombres, fechanacimiento) VALUES (NULL, 'Vargas Llosa', 'Jorge Mario Pedro', '1936-03-28');
INSERT INTO autor (id, apellidos, nombres, fechanacimiento) VALUES (NULL, 'Alegría Bazán', 'Ciro', '1909-11-04');
INSERT INTO autor (id, apellidos, nombres, fechanacimiento) VALUES (NULL, 'García Márquez', 'Gabriel José de la Concordia', '1927-03-06');

-- LIBRO --

INSERT INTO libro (isbn, titulo, autor_id, anoedicion, precio) VALUES ('978318472263', 'Los heraldos negros', 1, 1919, 48);
INSERT INTO libro (isbn, titulo, autor_id, anoedicion, precio) VALUES ('892014771852', 'Poemas humanos', 1, 1939, 120);
INSERT INTO libro (isbn, titulo, autor_id, anoedicion, precio) VALUES ('591338770183', 'Paco Yunque', 1, 1951, 55);

INSERT INTO libro (isbn, titulo, autor_id, anoedicion, precio) VALUES ('480129403571', 'La ciudad y los perros', 2, 1963, 81);
INSERT INTO libro (isbn, titulo, autor_id, anoedicion, precio) VALUES ('238874100138', 'Conversación en La Catedral', 2, 1951, 70);
INSERT INTO libro (isbn, titulo, autor_id, anoedicion, precio) VALUES ('981402938251', 'La casa verde', 2, 1966, 105);
INSERT INTO libro (isbn, titulo, autor_id, anoedicion, precio) VALUES ('890366138239', 'La fiesta del Chivo', 2, 2000, 30);

INSERT INTO libro (isbn, titulo, autor_id, anoedicion, precio) VALUES ('383370912281', 'El mundo es ancho y ajeno', 3, 1941, 65);
INSERT INTO libro (isbn, titulo, autor_id, anoedicion, precio) VALUES ('589120131047', 'Los perros hambrientos', 3, 1939, 31);
INSERT INTO libro (isbn, titulo, autor_id, anoedicion, precio) VALUES ('483240184226', 'La serpiente de oro', 3, 1935, 85);

INSERT INTO libro (isbn, titulo, autor_id, anoedicion, precio) VALUES ('762841019387', 'Cien años de soledad', 4, 1967, 75);
INSERT INTO libro (isbn, titulo, autor_id, anoedicion, precio) VALUES ('930281938211', 'El amor en los tiempos del cólera', 4, 1985, 38);
INSERT INTO libro (isbn, titulo, autor_id, anoedicion, precio) VALUES ('683425019133', 'El coronel no tiene quien le escriba', 4, 1961, 42);
INSERT INTO libro (isbn, titulo, autor_id, anoedicion, precio) VALUES ('661984010128', 'El general en su laberinto', 4, 1989, 110);

-- CONSTRAINT --

ALTER TABLE usuario
	ADD CONSTRAINT FK_usuario_tipousuario
    FOREIGN KEY (tipousuario_id) REFERENCES tipousuario(id);

ALTER TABLE libro 
	ADD CONSTRAINT FK_libro_autor
	FOREIGN KEY (autor_id) REFERENCES autor(id);

ALTER TABLE compra
	ADD CONSTRAINT FK_compra_libro
    FOREIGN KEY (libro_isbn) REFERENCES libro(isbn);
    
ALTER TABLE compra
	ADD CONSTRAINT FK_compra_usuario
    FOREIGN KEY (usuario_id) REFERENCES usuario(id);

-- CONSULTAS --

SELECT COM.libro_isbn, LIB.titulo, LIB.precio, 
    COUNT(COM.libro_isbn) AS unidades_vendidas
	FROM compra COM JOIN libro LIB ON COM.libro_isbn = LIB.isbn
	GROUP BY COM.libro_isbn ORDER BY 4 DESC, 2 ASC