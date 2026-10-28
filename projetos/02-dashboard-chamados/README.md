# 02 · Dashboard de chamados de suporte

> **Status:** 🔜 a começar · Mês 2 (semanas 5–8: 30/11 a 27/12/2026)
> Roteiro de estudo: [ROTEIRO.md](ROTEIRO.md) · Posts do LinkedIn: [LINKEDIN.md](LINKEDIN.md)

## Problema de negócio

A gestão de TI quer acompanhar **volume, tempo de atendimento e cumprimento de SLA** dos chamados, e descobrir onde estão os gargalos.

## Ferramentas

| Ferramenta | Para quê |
|---|---|
| Python + Jupyter | ambiente de análise |
| pandas | limpeza, datas, `groupby`, `merge` |
| matplotlib / seaborn | gráficos da análise exploratória |
| Power BI Desktop | dashboard final (medidas DAX) |
| git + GitHub | versionar e publicar |

## Dados

Fonte, licença e dicionário de dados em [dados/README.md](dados/README.md).

## Perguntas e onde estão as respostas

| # | Pergunta | Onde |
|---|---|---|
| 1 | Quantos chamados por dia, semana e categoria? | [notebooks/02_analise_exploratoria.ipynb](notebooks/02_analise_exploratoria.ipynb) |
| 2 | Tempo médio e mediano de solução por prioridade? | idem |
| 3 | Qual o percentual de chamados dentro do SLA? | idem + [powerbi/](powerbi/) |
| 4 | Que categorias mais estouram o SLA? | idem |
| 5 | Em que dia e horário o volume é maior? | idem |

## Resultados

> Preencher na semana 8.

🖼️ `imagens/dashboard.png` — print do dashboard.

| Achado | Número | O que a gestão pode fazer |
|---|---|---|
| `<TODO>` | `<TODO>` | `<TODO>` |
| `<TODO>` | `<TODO>` | `<TODO>` |
| `<TODO>` | `<TODO>` | `<TODO>` |

## O que aprendi

`<TODO>`

## Como rodar

```bash
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook projetos/02-dashboard-chamados/notebooks
```

O dashboard: abrir `powerbi/dashboard_chamados.pbix` no Power BI Desktop.
