# 03 · Previsão de rotatividade de funcionários (ML)

> **Status:** 🔜 a começar · Mês 3 (semanas 9–12: 28/12/2026 a 24/01/2027)
> Roteiro de estudo: [ROTEIRO.md](ROTEIRO.md) · Posts do LinkedIn: [LINKEDIN.md](LINKEDIN.md)

## Problema de negócio

Antecipar **quais funcionários têm maior risco de pedir desligamento**, para o RH agir antes (conversa, plano de carreira, ajuste de jornada).

## Ferramentas

| Ferramenta | Para quê |
|---|---|
| pandas | preparar os dados |
| scikit-learn | modelos, validação cruzada, métricas |
| matplotlib / seaborn | matriz de confusão, curva ROC, importância de variáveis |
| Jupyter | documentar o processo |
| git + GitHub | versionar e publicar |

## Dados

Fonte, licença e dicionário de dados em [dados/README.md](dados/README.md).

## Método e onde está cada etapa

| Etapa | Notebook |
|---|---|
| Análise exploratória e preparação | [notebooks/01_eda_preparacao.ipynb](notebooks/01_eda_preparacao.ipynb) |
| Baseline + comparação de modelos | [notebooks/02_modelos.ipynb](notebooks/02_modelos.ipynb) |
| Explicação do modelo para o RH | [notebooks/03_explicacao.ipynb](notebooks/03_explicacao.ipynb) |

## Resultados

> Preencher na semana 12.

| Modelo | Recall | Precisão | F1 | AUC |
|---|---|---|---|---|
| Regressão logística (baseline) | `<TODO>` | `<TODO>` | `<TODO>` | `<TODO>` |
| Random Forest | `<TODO>` | `<TODO>` | `<TODO>` | `<TODO>` |
| Gradient boosting | `<TODO>` | `<TODO>` | `<TODO>` | `<TODO>` |

**Por que recall:** deixar escapar quem vai sair custa mais caro que conversar com alguém que ficaria.

## O que o RH pode fazer com isso

`<TODO — os 3 fatores que mais pesam e uma ação para cada>`

## O que aprendi

`<TODO>`

## Como rodar

```bash
.venv\Scripts\activate
jupyter notebook projetos/03-ml-previsao-rotatividade/notebooks
```

Rodar os notebooks na ordem `01` → `02` → `03`.
