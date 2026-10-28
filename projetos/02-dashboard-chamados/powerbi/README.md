# Power BI · Projeto 02

Salvar o arquivo aqui como `dashboard_chamados.pbix`. Fonte: `../dados/chamados_limpos.csv`.

## Páginas

1. **Visão geral** — cartões (total de chamados, % dentro do SLA, tempo médio de solução) + linha de volume por semana.
2. **Gargalos** — barras de % fora do SLA por categoria; matriz prioridade × categoria.
3. **Quando chega** — mapa de calor dia da semana × hora.

## Medidas DAX planejadas

| Medida | Fórmula (ponto de partida) |
|---|---|
| Total de chamados | `Total Chamados = COUNTROWS(chamados)` |
| % dentro do SLA | `% SLA = DIVIDE(SUM(chamados[dentro_sla]), [Total Chamados])` |
| Tempo médio (h) | `Tempo Medio = AVERAGE(chamados[tempo_solucao_h])` |

> Confirmar os nomes de coluna depois da limpeza e ajustar as fórmulas.
