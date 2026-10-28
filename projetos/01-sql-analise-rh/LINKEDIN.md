# LinkedIn · Projeto 01 — SQL + estatística

Regra: imagem em todo post; link do GitHub **no primeiro comentário**. Depois de publicar, marque ✅ e cole o link do post.

| # | Semana | Tema | Status | Link do post |
|---|---|---|---|---|
| 1 | 1 (02/11) | Anúncio da jornada | ✍️ pronto para publicar | |
| 2 | 2 (09/11) | O que aprendi de SQL em 1 semana | rascunho | |
| 3 | 3 (16/11) | JOIN explicado com um exemplo de RH | rascunho | |
| 4 | 4 (23/11) | Entrega do Projeto 01 | modelo | |

---

## Post 1 — Anúncio da jornada

> Imagem: print do repositório no GitHub ou um quadro com o plano dos 4 meses.

Passei os últimos anos no suporte de TI resolvendo problemas, automatizando planilhas e montando scripts para que as tarefas repetitivas rodassem sozinhas.

Em algum momento percebi que a parte que eu mais gostava não era "consertar". Era olhar os dados e entender **por que** as coisas aconteciam.

Por isso, a partir de hoje começo uma jornada pública de 4 meses rumo à área de **Análise de Dados com Machine Learning**:

📊 Mês 1 — SQL e estatística
🐍 Mês 2 — Python, pandas e Power BI
🤖 Mês 3 — Machine learning (prevendo rotatividade de funcionários)
📈 Mês 4 — Previsão de demanda de chamados de suporte

Os projetos usam temas que conheço de perto: RH e suporte de TI. Tudo com dados públicos e código aberto no GitHub.

Toda semana vou compartilhar aqui o que aprendi, o que deu errado e o que construí.

Se você trabalha com dados, qual conselho daria para quem está começando? 👇

#AnaliseDeDados #MachineLearning #SQL #Python #PowerBI #TransicaoDeCarreira

> 1º comentário: "Repositório com o plano e os projetos: https://github.com/RafaGarciaDev/portfolio-dados-ml"

---

## Post 2 — O que aprendi de SQL em 1 semana

> Imagem: print de uma consulta sua com o resultado.

Uma semana de SQL e já respondi em 10 segundos uma pergunta que no Excel levava `<tempo>`.

A pergunta: **`<ex.: qual área tem mais desligamentos?>`**

3 comandos que mais usei:
🔹 `WHERE` — filtra o que interessa
🔹 `GROUP BY` — agrupa (por área, por cargo, por mês)
🔹 `ORDER BY` — coloca o maior no topo

O que travou: `<anotar durante a semana>`.

Para quem vem do Excel: `GROUP BY` é uma tabela dinâmica escrita em uma linha.

Qual foi o primeiro comando de SQL que fez sentido pra você?

#SQL #AnaliseDeDados #AprendendoEmPublico

---

## Post 3 — JOIN explicado com um exemplo de RH

> Imagem: duas tabelas pequenas (funcionários e áreas) e o resultado do JOIN.

JOIN parece difícil até você ver com dados de verdade.

Tenho duas tabelas: **funcionários** (nome, id_área) e **áreas** (id, nome da área).

🔸 **INNER JOIN** → só quem tem área cadastrada.
🔸 **LEFT JOIN** → todos os funcionários; quem não tem área aparece com área vazia.

O erro que eu cometi: `<ex.: o JOIN duplicou linhas e a contagem de desligamentos dobrou>`.
Como percebi: `<ex.: comparei o COUNT antes e depois do JOIN>`.

Dica: sempre confira quantas linhas você tinha antes e depois do JOIN.

#SQL #DataAnalytics #RH

---

## Post 4 — Entrega do Projeto 01 (modelo)

> Imagem: o gráfico principal + print de uma consulta.

✅ Projeto 1 de 4 concluído: **análise de RH só com SQL**.

A pergunta: onde estão a rotatividade e as faltas?

O que os dados mostraram:
📌 `<achado 1 com número>`
📌 `<achado 2 com número>`
📌 `<achado 3 com número>`

Se eu fosse o RH, começaria por: `<recomendação em uma frase>`.

Técnicas: JOIN, CTE, funções de janela e estatística descritiva.

O que eu faria diferente: `<uma linha>`.

Mês que vem: Python, pandas e Power BI com dados de chamados de suporte.

#SQL #AnaliseDeDados #PeopleAnalytics #Portfolio

> 1º comentário: "Código e consultas: https://github.com/RafaGarciaDev/portfolio-dados-ml/tree/main/projetos/01-sql-analise-rh"
