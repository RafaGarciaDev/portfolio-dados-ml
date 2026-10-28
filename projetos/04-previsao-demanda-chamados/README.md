# 04 · Previsão de demanda de chamados (séries temporais + clustering)

> **Status:** 🔜 a começar · Mês 4 (semanas 13–16: 25/01 a 21/02/2027)
> Roteiro de estudo: [ROTEIRO.md](ROTEIRO.md) · Posts do LinkedIn: [LINKEDIN.md](LINKEDIN.md)

## Problema de negócio

Prever **quantos chamados vão chegar nas próximas semanas**, para dimensionar a equipe de suporte, e **agrupar os chamados por perfil** para criar ações por grupo.

## Ferramentas

| Ferramenta | Para quê |
|---|---|
| pandas | agregar a série diária, variáveis de calendário |
| statsmodels | decomposição (tendência e sazonalidade) e modelo de previsão |
| scikit-learn | regressão com variáveis de calendário, K-Means, métricas (MAE) |
| matplotlib | gráfico real x previsto |
| git + GitHub | versionar e publicar |

## Dados

Reaproveitar `../02-dashboard-chamados/dados/chamados_limpos.csv` ou outro dataset público — ver [dados/README.md](dados/README.md).

## Método e onde está cada etapa

| Etapa | Notebook |
|---|---|
| Série diária, tendência e sazonalidade | [notebooks/01_serie_temporal.ipynb](notebooks/01_serie_temporal.ipynb) |
| Baseline x modelo de previsão | [notebooks/02_previsao.ipynb](notebooks/02_previsao.ipynb) |
| Agrupamento de chamados (K-Means) | [notebooks/03_clusters.ipynb](notebooks/03_clusters.ipynb) |

## Resultados

> Preencher na semana 16.

| Modelo | MAE (chamados/dia) | MAPE |
|---|---|---|
| Baseline ingênuo (mesmo dia da semana anterior) | `<TODO>` | `<TODO>` |
| `<modelo escolhido>` | `<TODO>` | `<TODO>` |

🖼️ `imagens/real_x_previsto.png`

**Recomendação de escala:** `<TODO — ex.: reforçar a equipe às segundas>`

**Grupos de chamados encontrados:** `<TODO — nome e perfil de cada cluster>`

## O que aprendi

`<TODO>`

## Como rodar

```bash
.venv\Scripts\activate
jupyter notebook projetos/04-previsao-demanda-chamados/notebooks
```
