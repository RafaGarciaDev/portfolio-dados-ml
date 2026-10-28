# Roteiro · Projeto 02 — Python, pandas e Power BI

Marque `[x]` ao concluir. Cada semana termina com **commit + post**.

## Antes de começar

- [ ] Instalar as bibliotecas: `.venv\Scripts\pip install -r requirements.txt`.
- [ ] Instalar o **Power BI Desktop** (Microsoft Store).
- [ ] Escolher o dataset e preencher [dados/README.md](dados/README.md) (fonte + licença).

## Semana 5 (30/11) — Python essencial e Jupyter

- [ ] Estudar: variáveis, listas, dicionários, funções, `for` (Kaggle Learn — Python).
- [ ] Abrir [notebooks/01_limpeza.ipynb](notebooks/01_limpeza.ipynb) e carregar o CSV.
- [ ] Post 5 — do Excel para o Python.
- [ ] Git: `P02 semana 5: carga dos dados`

## Semana 6 (07/12) — pandas: limpeza e datas

- [ ] Estudar: `read_csv`, `dropna`, `astype`, `to_datetime`, `groupby`, `merge` (Kaggle Learn — Pandas).
- [ ] Terminar o `01_limpeza.ipynb` e salvar `dados/chamados_limpos.csv`.
- [ ] Post 6 — 3 problemas que encontrei limpando os dados.
- [ ] Git: `P02 semana 6: limpeza e coluna de SLA`

## Semana 7 (14/12) — análise exploratória e gráficos

- [ ] Estudar: matplotlib/seaborn (Kaggle Learn — Data Visualization).
- [ ] Responder as 5 perguntas em [notebooks/02_analise_exploratoria.ipynb](notebooks/02_analise_exploratoria.ipynb).
- [ ] Post 7 — um gráfico e o que ele revela.
- [ ] Git: `P02 semana 7: análise exploratória`

## Semana 8 (21/12) — Power BI e entrega

- [ ] Estudar: importar CSV, modelagem, medidas DAX (Microsoft Learn — PL-300, módulos iniciais).
- [ ] Montar o dashboard seguindo [powerbi/README.md](powerbi/README.md); salvar o print em `imagens/dashboard.png`.
- [ ] Preencher **Resultados** e **O que aprendi** no [README.md](README.md); status ✅.
- [ ] Post 8 — entrega do projeto.
- [ ] Git de fechamento → versão **0.4.0**.

---

## Git — toda semana

```bash
cd "C:\Users\Suporte\Documents\Portfolio Analista de Dados com ML 2026-10-28"
git add projetos/02-dashboard-chamados
git commit -m "P02 semana N: <o que fez>"
git push
```

> 💡 Antes do commit de um notebook, use **Kernel → Restart & Run All** para ele subir com as saídas em ordem.

## Git — fechamento do projeto

1. `CHANGELOG.md`: `## [0.4.0] — <data>` com "Adicionado: Projeto 02 concluído — <principal achado>".
2. Mesma versão em `versao.py` e `pyproject.toml`; status ✅ no `README.md` da raiz.
3. Subir:

```bash
.venv\Scripts\python -m pytest -q
git add -A
git commit -m "0.4.0 - Projeto 02 concluído: dashboard de chamados"
git tag p02-concluido
git push --follow-tags
```

## Pronto quando

- [ ] Notebooks rodam do início ao fim sem erro.
- [ ] Dashboard com print no README.
- [ ] 4 posts publicados.
- [ ] Tag `p02-concluido` no GitHub.
