DROP TABLE IF EXISTS aluno;

CREATE TABLE aluno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    rga TEXT,
    curso TEXT,
    situacao TEXT,
    registrado_em TEXT
);
