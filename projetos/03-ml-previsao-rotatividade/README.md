# 03 · Previsão de rotatividade de funcionários (ML)

> **Status:** 🔜 a começar · Mês 3

## Problema de negócio

Antecipar **quais funcionários têm maior risco de pedir desligamento**, para o RH agir antes (conversa, plano de carreira, ajuste de jornada).

## Dados

- Fonte: `<a definir — dataset público de attrition de RH. Anotar link e licença.>`

## Método

1. Análise exploratória e tratamento (nulos, variáveis categóricas).
2. Baseline simples (regressão logística).
3. Comparar Random Forest e gradient boosting com validação cruzada.
4. Avaliar com recall, precisão, F1 e AUC (o que importa mais: não deixar escapar quem vai sair).
5. Explicar o modelo: quais fatores mais pesam no risco.

## Ferramentas

Python · pandas · scikit-learn · matplotlib

## Entregáveis

- [ ] Notebook com todo o processo
- [ ] Comparação de modelos em tabela
- [ ] Seção "o que o RH pode fazer com isso" no README
- [ ] Post no LinkedIn explicando o modelo sem jargão
