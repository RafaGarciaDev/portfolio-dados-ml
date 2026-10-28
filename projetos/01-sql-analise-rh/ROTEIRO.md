# Roteiro · Projeto 01 — SQL + estatística

Marque `[x]` ao concluir. Cada semana termina com **commit + post**.

## Antes de começar

- [ ] Instalar o **DB Browser for SQLite** (sqlitebrowser.org).
- [ ] Escolher o dataset e preencher [dados/README.md](dados/README.md) (fonte + licença).
- [ ] Criar `dados/rh.db` e rodar [sql/01_criar_tabelas.sql](sql/01_criar_tabelas.sql).

## Semana 1 (02/11) — SQL básico

- [ ] Estudar: `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `GROUP BY`, `COUNT/SUM/AVG` (SQLBolt, lições 1–6 e 10–12).
- [ ] Responder a pergunta 1 em [sql/02_perguntas_basicas.sql](sql/02_perguntas_basicas.sql).
- [ ] Post 1 — anúncio da jornada ([LINKEDIN.md](LINKEDIN.md)).
- [ ] Git (ver abaixo): `P01 semana 1: tabelas e primeira consulta`

## Semana 2 (09/11) — JOIN, CASE, HAVING

- [ ] Estudar: `INNER/LEFT JOIN`, `CASE WHEN`, `HAVING`, subconsultas.
- [ ] Responder as perguntas 2 e 3 ([02](sql/02_perguntas_basicas.sql) e [03](sql/03_joins.sql)).
- [ ] Post 2 — o que aprendi de SQL em 1 semana.
- [ ] Git: `P01 semana 2: joins e faixas de tempo de casa`

## Semana 3 (16/11) — funções de janela e CTEs

- [ ] Estudar: `WITH`, `ROW_NUMBER`, `RANK`, `LAG`, `SUM() OVER`.
- [ ] Responder as perguntas 4 e 5 em [sql/04_janelas_e_ctes.sql](sql/04_janelas_e_ctes.sql).
- [ ] Post 3 — JOIN explicado com um exemplo de RH.
- [ ] Git: `P01 semana 3: ranking de áreas com funções de janela`

## Semana 4 (23/11) — estatística e entrega

- [ ] Estudar: média x mediana, desvio padrão, percentis, correlação (Khan Academy).
- [ ] Exportar os resultados para o Excel/Sheets, montar 1 gráfico e salvar em `imagens/`.
- [ ] Preencher **Resultados** e **O que aprendi** no [README.md](README.md) e mudar o status para ✅.
- [ ] Post 4 — entrega do projeto.
- [ ] Git de fechamento (abaixo) → versão **0.3.0**.

---

## Git — toda semana

```bash
cd "C:\Users\Suporte\Documents\Portfolio Analista de Dados com ML 2026-10-28"
git add projetos/01-sql-analise-rh
git commit -m "P01 semana N: <o que fez>"
git push
```

## Git — fechamento do projeto

1. No `CHANGELOG.md`, adicionar no topo `## [0.3.0] — <data>` com "Adicionado: Projeto 01 concluído — <principal achado>".
2. Mesma versão e mesmo texto em `versao.py` e em `pyproject.toml`.
3. No `README.md` da raiz, mudar o status do projeto 01 para ✅.
4. Rodar os testes e subir:

```bash
.venv\Scripts\python -m pytest -q
git add -A
git commit -m "0.3.0 - Projeto 01 concluído: análise de RH com SQL"
git tag p01-concluido
git push --follow-tags
```

## Pronto quando

- [ ] As 5 perguntas têm consulta + resposta comentada.
- [ ] README com resultados, gráfico e "o que aprendi".
- [ ] 4 posts publicados.
- [ ] Tag `p01-concluido` no GitHub.
