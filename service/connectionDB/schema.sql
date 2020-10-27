DROP TABLE IF EXISTS aluno;

CREATE TABLE aluno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    rga TEXT,
    curso TEXT,
    situacao TEXT,
    registrado_em TEXT
);

INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES ('Kaio', '2018.1907.125-5', 'SI', 'ativo', '25/12/2019');
INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES ('Diego', '2018.1907.125-5', 'SI', 'ativo', '25/12/2019');
INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES ('Vini', '2018.1907.125-5', 'SI', 'ativo', '25/12/2019');
INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES ('Valentina', '2018.1907.125-5', 'SI', 'ativo', '25/12/2019');
INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES ('tiago', '2018.1907.125-5', 'SI', 'ativo', '25/12/2019');
INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES ('Mariana', '2018.1907.125-5', 'SI', 'ativo', '25/12/2019');
INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES ('claudia', '2018.1907.125-5', 'SI', 'ativo', '25/12/2019');
