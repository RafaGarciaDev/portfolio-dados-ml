# Portfólio · Análise de Dados com Machine Learning

Jornada pública de 4 meses do suporte de TI para a análise de dados com ML. Cada projeto resolve um **problema real de RH ou de suporte de TI**, com dados públicos, código aberto e as conclusões escritas em linguagem de negócio.

**Stack:** SQL · Python · pandas · scikit-learn · Power BI · Jupyter

## Projetos

| # | Projeto | Pergunta de negócio | Técnicas | Status |
|---|---|---|---|---|
| 01 | [Análise de RH com SQL](projetos/01-sql-analise-rh/) | Onde se concentram rotatividade e faltas? | SQL, CTE, funções de janela, estatística | 🔜 |
| 02 | [Dashboard de chamados](projetos/02-dashboard-chamados/) | O suporte cumpre o SLA? Onde está o gargalo? | pandas, EDA, Power BI | 🔜 |
| 03 | [Previsão de rotatividade](projetos/03-ml-previsao-rotatividade/) | Quem tem mais risco de sair? | Classificação, Random Forest, boosting | 🔜 |
| 04 | [Previsão de demanda de chamados](projetos/04-previsao-demanda-chamados/) | Quantos chamados vêm na próxima semana? | Séries temporais, K-Means | 🔜 |

## Plano

O roteiro semana a semana está em [PLANO_DE_ESTUDO.md](PLANO_DE_ESTUDO.md).

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
