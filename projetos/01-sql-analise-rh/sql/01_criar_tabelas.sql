-- Projeto 01 · Criar as tabelas
-- Ajustar as colunas ao dataset escolhido (ver dados/README.md).
-- No DB Browser for SQLite: Arquivo → Importar → Tabela de arquivo CSV também funciona.

CREATE TABLE IF NOT EXISTS areas (
    id_area   INTEGER PRIMARY KEY,
    nome_area TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS funcionarios (
    id_funcionario INTEGER PRIMARY KEY,
    id_area        INTEGER REFERENCES areas (id_area),
    cargo          TEXT,
    data_admissao  DATE,
    salario        REAL,
    horas_extras   REAL,
    desligado      INTEGER  -- 1 = saiu, 0 = ativo
);

CREATE TABLE IF NOT EXISTS faltas (
    id_falta       INTEGER PRIMARY KEY,
    id_funcionario INTEGER REFERENCES funcionarios (id_funcionario),
    data_falta     DATE
);

-- Conferência: quantas linhas cada tabela tem?
SELECT 'areas' AS tabela, COUNT(*) AS linhas FROM areas
UNION ALL SELECT 'funcionarios', COUNT(*) FROM funcionarios
UNION ALL SELECT 'faltas', COUNT(*) FROM faltas;
