# Portfólio · Análise de Dados com Machine Learning

Jornada pública de 4 meses do suporte de TI para a análise de dados com ML. Cada projeto resolve um **problema real de RH ou de suporte de TI**, com dados públicos, código aberto e as conclusões escritas em linguagem de negócio.

**Stack:** SQL · Python · pandas · scikit-learn · Power BI · Jupyter

## Projetos

| # | Projeto | Pergunta de negócio | Ferramentas | Período | Status |
|---|---|---|---|---|---|
| 01 | [Análise de RH com SQL](projetos/01-sql-analise-rh/) | Onde se concentram rotatividade e faltas? | SQLite, SQL (CTE, janelas), Excel | nov/2026 | 🔜 |
| 02 | [Dashboard de chamados](projetos/02-dashboard-chamados/) | O suporte cumpre o SLA? Onde está o gargalo? | Python, pandas, seaborn, Power BI | dez/2026 | 🔜 |
| 03 | [Previsão de rotatividade](projetos/03-ml-previsao-rotatividade/) | Quem tem mais risco de sair? | scikit-learn (logística, Random Forest, boosting) | jan/2027 | 🔜 |
| 04 | [Previsão de demanda de chamados](projetos/04-previsao-demanda-chamados/) | Quantos chamados vêm na próxima semana? | statsmodels, scikit-learn (K-Means) | fev/2027 | 🔜 |

Cada projeto tem a mesma estrutura:

```
projetos/NN-nome/
├── README.md      ← problema, ferramentas, resultados (vitrine)
├── ROTEIRO.md     ← o que estudar e fazer em cada semana + comandos de git
├── LINKEDIN.md    ← os 4 posts do projeto
├── dados/         ← fonte, licença e dicionário de dados
├── sql/ ou notebooks/  (+ powerbi/ no 02)
└── imagens/       ← prints e gráficos
```

## Plano

O roteiro geral está em [PLANO_DE_ESTUDO.md](PLANO_DE_ESTUDO.md) e o calendário de posts em [linkedin/POSTS.md](linkedin/POSTS.md).

## Como rodar

```bash
git clone https://github.com/RafaGarciaDev/portfolio-dados-ml.git
cd portfolio-dados-ml
python -m venv .venv
.venv\Scripts\activate          # Windows (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt -r requirements-dev.txt
python -m pytest -q
```

## Contato

Acompanhe a jornada no LinkedIn · GitHub: [@RafaGarciaDev](https://github.com/RafaGarciaDev)

---

Versão atual: ver [CHANGELOG.md](CHANGELOG.md) · Documentação: [técnica](docs/TECNICO.md) · [manual](docs/MANUAL.md)
