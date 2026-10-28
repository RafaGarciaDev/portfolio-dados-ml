# Roteiro · Projeto 03 — Machine learning clássico

Marque `[x]` ao concluir. Cada semana termina com **commit + post**.

## Antes de começar

- [ ] Escolher o dataset e preencher [dados/README.md](dados/README.md) (fonte + licença).
- [ ] Conferir que o scikit-learn está instalado: `.venv\Scripts\python -c "import sklearn; print(sklearn.__version__)"`.

## Semana 9 (28/12) — conceitos e baseline

- [ ] Estudar: treino x teste, overfitting, regressão logística (Kaggle Learn — Intro to ML).
- [ ] Fazer o [notebooks/01_eda_preparacao.ipynb](notebooks/01_eda_preparacao.ipynb): nulos, variáveis categóricas, `train_test_split` estratificado.
- [ ] Post 9 — o que é machine learning, explicado com RH.
- [ ] Git: `P03 semana 9: preparação e baseline`

## Semana 10 (04/01) — árvores e ensembles

- [ ] Estudar: árvore de decisão, Random Forest, gradient boosting (Kaggle Learn — Intermediate ML).
- [ ] Treinar os 3 modelos em [notebooks/02_modelos.ipynb](notebooks/02_modelos.ipynb).
- [ ] Post 10 — por que acurácia de 85% pode ser um modelo ruim.
- [ ] Git: `P03 semana 10: comparação de modelos`

## Semana 11 (11/01) — métricas e dados desbalanceados

- [ ] Estudar: matriz de confusão, precisão, recall, F1, AUC; `class_weight="balanced"`.
- [ ] Validação cruzada (`cross_val_score`) e ajuste de hiperparâmetros (`GridSearchCV`).
- [ ] Post 11 — matriz de confusão sem jargão.
- [ ] Git: `P03 semana 11: validação cruzada e ajuste`

## Semana 12 (18/01) — explicar o modelo e entrega

- [ ] Fazer o [notebooks/03_explicacao.ipynb](notebooks/03_explicacao.ipynb): importância de variáveis (`permutation_importance`).
- [ ] Preencher **Resultados**, **O que o RH pode fazer** e **O que aprendi** no [README.md](README.md); status ✅.
- [ ] Post 12 — entrega do projeto.
- [ ] Git de fechamento → versão **0.5.0**.

---

## Git — toda semana

```bash
cd "C:\Users\Suporte\Documents\Portfolio Analista de Dados com ML 2026-10-28"
git add projetos/03-ml-previsao-rotatividade
git commit -m "P03 semana N: <o que fez>"
git push
```

> 💡 Fixe `random_state=42` em tudo, para quem clonar ter os mesmos números.

## Git — fechamento do projeto

1. `CHANGELOG.md`: `## [0.5.0] — <data>` com "Adicionado: Projeto 03 concluído — <melhor modelo e recall>".
2. Mesma versão em `versao.py` e `pyproject.toml`; status ✅ no `README.md` da raiz.
3. Subir:

```bash
.venv\Scripts\python -m pytest -q
git add -A
git commit -m "0.5.0 - Projeto 03 concluído: previsão de rotatividade"
git tag p03-concluido
git push --follow-tags
```

## Pronto quando

- [ ] 3 modelos comparados com validação cruzada.
- [ ] Explicação dos fatores em linguagem de RH no README.
- [ ] 4 posts publicados.
- [ ] Tag `p03-concluido` no GitHub.
