create_database = """CREATE DATABASE sol_nascente"""

create_estado_table = """CREATE TABLE estado(
                         id INT NOT NULL AUTO_INCREMENT,
                         uf VARCHAR(2),
                         PRIMARY KEY (id));"""

create_cidade_table = """CREATE TABLE cidade(
                         id INT NOT NULL AUTO_INCREMENT,
                         estado_id INT,
                         nome VARCHAR(30),
                         PRIMARY KEY (id),
                         CONSTRAINT fk_cidade_estado FOREIGN KEY (estado_id) REFERENCES estado(id));"""
create_telefone_cel_table = """CREATE TABLE telefone_cel(
                               id INT NOT NULL AUTO_INCREMENT,
                               telefone_cel VARCHAR(14) UNIQUE);"""

create_horario_table = """CREATE TABLE horario(
                          id INT NOT NULL AUTO_INCREMENT,
                          periodo VARCHAR (5));"""

create_funcao_table = """CREATE TABLE funcao(
                         id INT NOT NULL AUTO_INCREMENT,
                         cargo VARCHAR (8));"""

create_turno_table = """CREATE TABLE turno(
                        id INT NOT NULL AUTO_INCREMENT,
                        periodo VARCHAR(8));"""

create_salao_table = """CREATE TABLE salao(
                        id INT NOT NULL AUTO_INCREMENT,
                        salao VARCHAR(30));"""

create_condominio_table = """CREATE TABLE condominio(
                             id INT NOT NULL AUTO_INCREMENT,
                             nome VARCHAR(60),
                             CNPJ VARCHAR(18),
                             cidade_id VARCHAR(45),
                             bairro VARCHAR(30),
                             rua VARCHAR(80),
                             numero INT,
                             referencia VARCHAR(100),
                             PRIMARY KEY (id),
                             CONSTRAINT fk_condominio_cidade FOREIGN KEY (cidade_id) REFERENCES cidade(id));"""

create_moradores_table = """CREATE TABLE moradores(
                            id INT NOT NULL AUTO_INCREMENT,
                            id_condominio INT,
                            nome VARCHAR (80),
                            cpf VARCHAR (14),
                            email VARCHAR(100),
                            telefone_cel_id INT, 
                            telefone_fixo VARCHAR (13),
                            num_bloco INT,
                            num_apt INT);"""


