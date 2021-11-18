create_database = """CREATE DATABASE sol_nascente;"""

create_estado_table = """CREATE TABLE estado(
                         id INT NOT NULL AUTO_INCREMENT,
                         uf VARCHAR(2),
                         PRIMARY KEY(id));"""

create_cidade_table = """CREATE TABLE cidade(
                         id INT NOT NULL AUTO_INCREMENT,
                         estado_id INT,
                         nome VARCHAR(30),
                         PRIMARY KEY (id),
                         CONSTRAINT fk_cidade_estado FOREIGN KEY (estado_id) REFERENCES estado(id));"""

create_telefone_cel_table = """CREATE TABLE telefone_cel(
                               id INT NOT NULL AUTO_INCREMENT,
                               telefone_cel VARCHAR(14) UNIQUE,
                               PRIMARY KEY (id));"""

create_horario_table = """CREATE TABLE horario(
                          id INT NOT NULL AUTO_INCREMENT,
                          periodo VARCHAR (5),
                          PRIMARY KEY (id));"""

create_funcao_table = """CREATE TABLE funcao(
                         id INT NOT NULL AUTO_INCREMENT,
                         cargo VARCHAR (8),
                         PRIMARY KEY (id));"""

create_turno_table = """CREATE TABLE turno(
                        id INT NOT NULL AUTO_INCREMENT,
                        periodo VARCHAR(8),
                        PRIMARY KEY (id));"""

create_salao_table = """CREATE TABLE salao(
                        id INT NOT NULL AUTO_INCREMENT,
                        nome VARCHAR(30),
                        PRIMARY KEY (id));"""

create_categoria_table = """CREATE TABLE categoria(
                            id INT NOT NULL AUTO_INCREMENT,
                            nome VARCHAR(30),
                            PRIMARY KEY (id));"""

create_condominio_table = """CREATE TABLE condominio(
                             id INT NOT NULL AUTO_INCREMENT,
                             nome VARCHAR(60),
                             cnpj VARCHAR(18),
                             id_cidade INT,
                             bairro VARCHAR(30),
                             rua VARCHAR(80),
                             numero INT,
                             referencia VARCHAR(100),
                             CONSTRAINT fk_condominio_cidade FOREIGN KEY (id_cidade) REFERENCES cidade(id),
                             PRIMARY KEY (id));"""

create_morador_table = """CREATE TABLE morador(
                            id INT NOT NULL AUTO_INCREMENT,
                            id_condominio INT,
                            nome VARCHAR (80),
                            cpf VARCHAR (14),
                            email VARCHAR(100),
                            telefone_cel_id INT, 
                            telefone_fixo VARCHAR (13),
                            num_bloco INT,
                            num_apt INT,
                            status INT,
                            CONSTRAINT fk_morador_condomio FOREIGN KEY (id_condominio) REFERENCES condominio(id),
                            CONSTRAINT fk_morador_telefone_cel FOREIGN KEY (telefone_cel_id) REFERENCES telefone_cel(id),
                            PRIMARY KEY (id));"""

create_ocorrencia_table = """CREATE TABLE ocorrencia(
                             id INT NOT NULL AUTO_INCREMENT,
                             condominio_id INT,
                             morador_id INT,
                             categoria_id INT,
                             descricao VARCHAR (100),
                             CONSTRAINT fk_ocorrencia_condominio FOREIGN KEY(condominio_id) REFERENCES condominio(id),
                             CONSTRAINT fk_ocorrencia_morador FOREIGN KEY (morador_id) REFERENCES morador(id),
                             CONSTRAINT fk_ocorrencia_categoria FOREIGN KEY (categoria_id) REFERENCES categoria(id),
                             PRIMARY KEY (id));"""

create_reserva_table = """CREATE TABLE reserva(
                          id INT NOT NULL AUTO_INCREMENT,
                          condominio_id INT,
                          morador_id INT,
                          salao_id INT,
                          data DATE, 
                          horario_id INT,
                          CONSTRAINT fk_reserva_condominio FOREIGN KEY (condominio_id) REFERENCES condominio(id),
                          CONSTRAINT fk_reserva_morador FOREIGN KEY (morador_id) REFERENCES morador(id),
                          CONSTRAINT fk_reserva_salao FOREIGN KEY(salao_id) REFERENCES salao(id),
                          CONSTRAINT fk_reserva_horario FOREIGN KEY (horario_id) REFERENCES horario(id),
                          PRIMARY KEY (id));"""

create_funcionario_table = """CREATE TABLE funcionario(
                            id INT NOT NULL AUTO_INCREMENT,
                            id_condominio INT,
                            nome VARCHAR (80),
                            cpf VARCHAR (14),
                            turno_id INT,
                            funcao_id INT,
                            salario FLOAT,
                            cidade_id INT,
                            bairro VARCHAR(30),
                            rua VARCHAR(80),
                            numero INT,
                            referencia VARCHAR(100),
                            CONSTRAINT fk_funcionario_cidade FOREIGN KEY (cidade_id) REFERENCES cidade(id),
                            CONSTRAINT fk_funcionatio_condomio FOREIGN KEY (id_condominio) REFERENCES condominio(id),
                            CONSTRAINT fk_funcionario_turno FOREIGN KEY (turno_id) REFERENCES turno(id),
                            CONSTRAINT fk_funcionario_funcao FOREIGN KEY (funcao_id) REFERENCES funcao(id),
                            PRIMARY KEY (id));"""

create_achados_perdidos_table = """CREATE TABLE achados_perdidos(
                                   condominio_id INT, 
                                   funcionario_id INT, 
                                   descricao VARCHAR (200),
                                   CONSTRAINT fk_ap_condominio FOREIGN KEY (condominio_id) REFERENCES condominio(id),
                                   CONSTRAINT fk_ap_funcionario FOREIGN KEY (funcionario_id) REFERENCES funcionario(id),
                                   PRIMARY KEY (condominio_id, funcionario_id));"""

createTodos = create_achados_perdidos_table

