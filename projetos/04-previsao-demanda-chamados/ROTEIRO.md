# Roteiro · Projeto 04 — Séries temporais e clustering

Marque `[x]` ao concluir. Cada semana termina com **commit + post**.

## Antes de começar

- [ ] Decidir a base (reaproveitar a do Projeto 02 ou outra) e preencher [dados/README.md](dados/README.md).
- [ ] Conferir o statsmodels: `.venv\Scripts\python -c "import statsmodels; print(statsmodels.__version__)"`.

## Semana 13 (25/01) — série temporal

- [ ] Estudar: tendência, sazonalidade, médias móveis (Kaggle Learn — Time Series).
- [ ] Fazer o [notebooks/01_serie_temporal.ipynb](notebooks/01_serie_temporal.ipynb): agregar por dia e decompor.
- [ ] Post 13 — a segunda-feira do suporte em um gráfico.
- [ ] Git: `P04 semana 13: série diária e sazonalidade`

## Semana 14 (01/02) — previsão

- [ ] Estudar: baseline ingênuo, separação temporal treino/teste, MAE e MAPE.
- [ ] Fazer o [notebooks/02_previsao.ipynb](notebooks/02_previsao.ipynb): baseline x modelo.
- [ ] Post 14 — por que comecei pelo modelo mais burro possível.
- [ ] Git: `P04 semana 14: previsão e comparação com baseline`

## Semana 15 (08/02) — clustering

- [ ] Estudar: K-Means, padronização (`StandardScaler`), método do cotovelo.
- [ ] Fazer o [notebooks/03_clusters.ipynb](notebooks/03_clusters.ipynb) e dar nome a cada grupo.
- [ ] Post 15 — os tipos de chamado que os dados encontraram sozinhos.
- [ ] Git: `P04 semana 15: clusters de chamados`

## Semana 16 (15/02) — entrega e fechamento da jornada

- [ ] Preencher **Resultados** e **O que aprendi** no [README.md](README.md); status ✅.
- [ ] Revisar o README principal e o perfil do LinkedIn (título, sobre, destaques).
- [ ] Post 16 — fechamento dos 4 meses.
- [ ] Git de fechamento → versão **1.0.0** (portfólio completo).
- [ ] Começar as candidaturas.

---

## Git — toda semana

```bash
cd "C:\Users\Suporte\Documents\Portfolio Analista de Dados com ML 2026-10-28"
git add projetos/04-previsao-demanda-chamados
git commit -m "P04 semana N: <o que fez>"
git push
```

> ⚠️ Em série temporal, nunca embaralhar os dados na divisão treino/teste: o teste é sempre o período mais recente.

## Git — fechamento do projeto e da jornada

1. `CHANGELOG.md`: `## [1.0.0] — <data>` com "Adicionado: Projeto 04 concluído; portfólio completo com 4 projetos".
2. Mesma versão em `versao.py` e `pyproject.toml`; status ✅ no `README.md` da raiz.
3. Subir:

```bash
.venv\Scripts\python -m pytest -q
git add -A
git commit -m "1.0.0 - Projeto 04 concluído: portfólio completo"
git tag p04-concluido
git tag v1.0.0
git push --follow-tags
```

## Pronto quando

- [ ] Modelo bate o baseline (MAE menor) e o gráfico real x previsto está no README.
- [ ] Clusters com nome e ação sugerida.
- [ ] 4 posts publicados.
- [ ] Tags `p04-concluido` e `v1.0.0` no GitHub.
