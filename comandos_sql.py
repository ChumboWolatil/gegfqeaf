create_condominio_table = """CREATE TABLE condominio(
                             id INT NOT NULL AUTO_INCREMENT,
                             nome VARCHAR(60),
                             CNPJ VARCHAR(18),
                             cidade VARCHAR(45),
                             uf_id VARCHAR(2),
                             bairro VARCHAR(30),
                             rua VARCHAR(50),
                             numero INT,
                             referencia VARCHAR(100),
                             PRIMARY KEY (id));"""