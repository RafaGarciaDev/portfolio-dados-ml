# LinkedIn · Projeto 03 — Machine learning clássico

Regra: imagem em todo post; link do GitHub **no primeiro comentário**. Depois de publicar, marque ✅ e cole o link do post.

| # | Semana | Tema | Status | Link do post |
|---|---|---|---|---|
| 9 | 9 (28/12) | O que é machine learning, explicado com RH | rascunho | |
| 10 | 10 (04/01) | Por que acurácia de 85% pode ser um modelo ruim | rascunho | |
| 11 | 11 (11/01) | Matriz de confusão sem jargão | rascunho | |
| 12 | 12 (18/01) | Entrega do Projeto 03 | modelo | |

---

## Post 9 — O que é machine learning, explicado com RH

> Imagem: esquema simples "dados do passado → modelo → risco de cada pessoa".

Mês 3 da jornada: machine learning.

A explicação mais simples que encontrei:

Se o RH tem o histórico de quem saiu e de quem ficou, um modelo aprende os **padrões** de quem saiu (tempo de casa, horas extras, salário…) e aponta quem hoje tem um perfil parecido.

Não é bola de cristal. É uma lista de prioridade para o RH conversar primeiro.

O que mais me surpreendeu essa semana: `<anotar>`.

#MachineLearning #PeopleAnalytics #AprendendoEmPublico

---

## Post 10 — Por que acurácia de 85% pode ser um modelo ruim

> Imagem: os números de acurácia x recall do seu modelo.

Treinei meu primeiro modelo e ele acertou 85%. Fiquei feliz por 5 minutos.

Aí percebi: se só `<x>%` das pessoas saem da empresa, um modelo que responde "ninguém vai sair" já acerta `<100 − x>%`.

Acurácia alta, utilidade zero.

Por isso a métrica que importa aqui é o **recall**: de quem realmente saiu, quantos o modelo encontrou?

Meu recall: `<antes>` → `<depois de ajustar>`.

#MachineLearning #DataScience #Metricas

---

## Post 11 — Matriz de confusão sem jargão

> Imagem: a matriz de confusão do seu modelo, com os 4 quadrantes legendados em português.

4 quadrados que explicam qualquer modelo de classificação:

✅ Disse que ia sair e saiu → acerto que importa
✅ Disse que ia ficar e ficou → acerto
⚠️ Disse que ia sair e ficou → uma conversa a mais (custo baixo)
❌ Disse que ia ficar e saiu → a pessoa que perdemos (custo alto)

No meu modelo: `<números>`.

Escolhi aceitar mais ⚠️ para reduzir os ❌.

#MachineLearning #DataScience #RH

---

## Post 12 — Entrega do Projeto 03 (modelo)

> Imagem: gráfico de importância das variáveis.

✅ Projeto 3 de 4 concluído: **modelo que prevê risco de desligamento**.

📊 Comparei 3 modelos: regressão logística, Random Forest e gradient boosting.
🏆 Melhor: `<modelo>`, com recall de `<x%>`.

Os 3 fatores que mais pesam:
1️⃣ `<fator>` → ação sugerida: `<ação>`
2️⃣ `<fator>` → `<ação>`
3️⃣ `<fator>` → `<ação>`

O mais importante que aprendi: um modelo só vale se alguém consegue agir com ele.

Último mês: previsão de demanda de chamados de suporte.

#MachineLearning #PeopleAnalytics #ScikitLearn #Portfolio

> 1º comentário: "Notebooks: https://github.com/RafaGarciaDev/portfolio-dados-ml/tree/main/projetos/03-ml-previsao-rotatividade"
