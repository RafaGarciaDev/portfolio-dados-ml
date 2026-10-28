# 02 · Dashboard de chamados de suporte

> **Status:** 🔜 a começar · Mês 2

## Problema de negócio

A gestão de TI quer acompanhar **volume, tempo de atendimento e cumprimento de SLA** dos chamados, e descobrir onde estão os gargalos.

## Dados

- Fonte: `<a definir — dataset público de tickets de service desk. Anotar link e licença.>`
- Alternativa: base sintética gerada em Python (abertura, categoria, prioridade, técnico, tempo de solução).

## Perguntas a responder

1. Quantos chamados por dia, semana e categoria?
2. Qual o tempo médio e mediano de solução por prioridade?
3. Qual o percentual de chamados dentro do SLA?
4. Que categorias mais reabrem ou estouram o SLA?
5. Em que dia da semana e horário o volume é maior?

## Ferramentas

Python · pandas · matplotlib/seaborn · Jupyter · Power BI

## Entregáveis

- [ ] Notebook de limpeza e análise exploratória
- [ ] Dashboard no Power BI (`.pbix`) + print no README
- [ ] Post no LinkedIn com o print do dashboard e 3 insights
