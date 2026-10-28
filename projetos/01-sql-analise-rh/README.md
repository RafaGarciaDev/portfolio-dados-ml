# 01 · Análise de RH com SQL

> **Status:** 🔜 a começar · Mês 1 (semanas 1–4: 02/11 a 29/11/2026)
> Roteiro de estudo: [ROTEIRO.md](ROTEIRO.md) · Posts do LinkedIn: [LINKEDIN.md](LINKEDIN.md)

## Problema de negócio

O RH quer entender **onde está a rotatividade e o absenteísmo**: quais áreas, cargos e faixas de tempo de casa concentram mais desligamentos e faltas?

## Ferramentas

| Ferramenta | Para quê |
|---|---|
| SQLite + DB Browser for SQLite | banco local e editor de consultas |
| SQL (JOIN, CTE, funções de janela) | responder as perguntas |
| Excel ou Google Sheets | estatística descritiva e gráfico rápido para o post |
| git + GitHub | versionar e publicar |

## Dados

Fonte, licença e dicionário de dados em [dados/README.md](dados/README.md).

## Perguntas e onde estão as respostas

| # | Pergunta | Arquivo |
|---|---|---|
| 1 | Qual a taxa de desligamento por área e por cargo? | [sql/02_perguntas_basicas.sql](sql/02_perguntas_basicas.sql) |
| 2 | Quem sai mais: quem tem menos de 1 ano de casa ou mais de 5? | [sql/02_perguntas_basicas.sql](sql/02_perguntas_basicas.sql) |
| 3 | Existe relação entre horas extras, salário e desligamento? | [sql/03_joins.sql](sql/03_joins.sql) |
| 4 | Qual mês concentra mais faltas? | [sql/04_janelas_e_ctes.sql](sql/04_janelas_e_ctes.sql) |
| 5 | Quais 3 áreas merecem atenção primeiro, e por quê? | [sql/04_janelas_e_ctes.sql](sql/04_janelas_e_ctes.sql) |

## Resultados

> Preencher na semana 4.

| Achado | Número | O que o RH pode fazer |
|---|---|---|
| `<ex.: Área X tem o dobro da média de desligamentos>` | `<x%>` | `<ação>` |
| `<TODO>` | `<TODO>` | `<TODO>` |
| `<TODO>` | `<TODO>` | `<TODO>` |

🖼️ `imagens/` — prints das consultas e o gráfico principal.

## O que aprendi

`<TODO — 3 linhas: o que foi difícil, o que eu faria diferente>`

## Como rodar

1. Baixe o dataset indicado em `dados/README.md` e salve em `dados/`.
2. Abra o DB Browser for SQLite → **Novo banco** → `dados/rh.db`.
3. Rode os arquivos de `sql/` na ordem: `01` → `02` → `03` → `04`.
