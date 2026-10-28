# Plano de estudo — Analista de Dados com ML

**Meta:** em 4 meses (nov/2026 a fev/2027) ter 4 projetos no GitHub, 16 posts no LinkedIn e começar a se candidatar a vagas de **analista de dados júnior / pleno com ML**.

**Ritmo sugerido:** 1h por dia útil + 3h no fim de semana (~8h/semana). Marque `[x]` ao concluir.

**Regra de ouro:** cada mês termina com **um projeto publicado** e **um post de entrega**. Estudar sem publicar não conta para o portfólio.

**Detalhe de cada mês:** o `ROTEIRO.md` de cada projeto tem as tarefas da semana, os comandos de git e a versão de fechamento; o `LINKEDIN.md` tem os 4 posts.

| Projeto | Fecha com a versão | Tag no GitHub |
|---|---|---|
| 01 · SQL | 0.3.0 | `p01-concluido` |
| 02 · Power BI | 0.4.0 | `p02-concluido` |
| 03 · ML | 0.5.0 | `p03-concluido` |
| 04 · Previsão | 1.0.0 | `p04-concluido` + `v1.0.0` |

---

## Mês 1 — SQL + estatística → [Projeto 01](projetos/01-sql-analise-rh/)

- [ ] **Semana 1** — SQL básico: `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, `COUNT/SUM/AVG`. Praticar no SQLite (DB Browser for SQLite).
- [ ] **Semana 2** — `JOIN`s (inner, left), subconsultas, `CASE WHEN`, `HAVING`.
- [ ] **Semana 3** — funções de janela (`ROW_NUMBER`, `RANK`, `LAG`, média móvel) e CTEs (`WITH`).
- [ ] **Semana 4** — estatística descritiva: média, mediana, desvio padrão, percentis, correlação. Fechar e publicar o Projeto 01.

## Mês 2 — Python + pandas + Power BI → [Projeto 02](projetos/02-dashboard-chamados/)

- [ ] **Semana 5** — Python essencial (listas, dicionários, funções) e Jupyter. Criar o `.venv` e instalar o `requirements.txt`.
- [ ] **Semana 6** — pandas: ler CSV/Excel, limpar dados, `groupby`, `merge`, datas.
- [ ] **Semana 7** — gráficos (matplotlib/seaborn) e análise exploratória (EDA).
- [ ] **Semana 8** — Power BI: modelagem, medidas DAX básicas, dashboard. Publicar o Projeto 02.

## Mês 3 — Machine learning clássico → [Projeto 03](projetos/03-ml-previsao-rotatividade/)

- [ ] **Semana 9** — conceitos: treino/teste, overfitting, regressão linear e logística (scikit-learn).
- [ ] **Semana 10** — árvores de decisão, Random Forest, gradient boosting.
- [ ] **Semana 11** — métricas: matriz de confusão, precisão, recall, F1, AUC; dados desbalanceados.
- [ ] **Semana 12** — validação cruzada, ajuste de hiperparâmetros, explicar o modelo (importância de variáveis). Publicar o Projeto 03.

## Mês 4 — ML aplicado ao negócio → [Projeto 04](projetos/04-previsao-demanda-chamados/)

- [ ] **Semana 13** — séries temporais: tendência, sazonalidade, médias móveis, baseline ingênuo.
- [ ] **Semana 14** — modelos de previsão (regressão com variáveis de calendário; Prophet ou statsmodels) e como avaliar (MAE, MAPE).
- [ ] **Semana 15** — clustering (K-Means) para agrupar tipos de chamado.
- [ ] **Semana 16** — publicar o Projeto 04, revisar o README principal e o perfil do LinkedIn, e começar as candidaturas.

---

## Em paralelo (o tempo todo)

- [ ] **LinkedIn:** 1 post por semana ([rascunhos](linkedin/POSTS.md)).
- [ ] **Perfil:** título "Analista de Suporte em transição para Dados | SQL · Python · Power BI · Machine Learning", com o link do GitHub.
- [ ] **Prática:** 2 exercícios de SQL por semana (HackerRank, LeetCode SQL ou StrataScratch).
- [ ] **Vagas:** a partir do mês 3, salvar 5 vagas por semana e anotar as ferramentas que mais aparecem.

## Fontes de estudo (gratuitas)

| Tema | Onde |
|---|---|
| SQL | SQLBolt · Mode SQL Tutorial |
| Python e pandas | Kaggle Learn (Python, Pandas, Data Visualization) |
| Estatística | Khan Academy — Estatística e probabilidade |
| Machine learning | Kaggle Learn (Intro + Intermediate ML) · documentação do scikit-learn |
| Power BI | Microsoft Learn — trilha PL-300 |
| Séries temporais | Kaggle Learn — Time Series |
