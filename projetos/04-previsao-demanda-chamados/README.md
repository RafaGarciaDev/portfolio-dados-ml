# 04 · Previsão de demanda de chamados (séries temporais + clustering)

> **Status:** 🔜 a começar · Mês 4

## Problema de negócio

Prever **quantos chamados vão chegar nas próximas semanas**, para dimensionar a equipe de suporte, e **agrupar os chamados por perfil** para criar ações por grupo.

## Dados

- Reaproveitar a base do [Projeto 02](../02-dashboard-chamados/) (agregada por dia), ou outro dataset público de tickets.

## Método

1. Série diária: tendência, sazonalidade semanal e feriados.
2. Baseline ingênuo (mesmo dia da semana anterior) para comparar.
3. Modelo de previsão (regressão com variáveis de calendário; Prophet ou statsmodels).
4. Avaliar com MAE e MAPE em um período de teste.
5. K-Means para agrupar chamados por categoria, tempo de solução e prioridade.

## Ferramentas

Python · pandas · scikit-learn · statsmodels ou Prophet

## Entregáveis

- [ ] Notebook com previsão e gráfico de real x previsto
- [ ] Recomendação de escala da equipe com base na previsão
- [ ] Post no LinkedIn de fechamento da jornada de 4 meses
