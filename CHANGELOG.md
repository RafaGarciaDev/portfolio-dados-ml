# Changelog

Todas as mudanças relevantes deste projeto. Formato: [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) · versões: [SemVer](https://semver.org/lang/pt-BR/).

## [0.2.0] — 2026-10-28

### Adicionado
- Esqueleto completo dos 4 projetos: cada um com `README.md` (vitrine com ferramentas e tabela de resultados), `ROTEIRO.md` (tarefas semana a semana com datas, comandos de git e versão de fechamento), `LINKEDIN.md` (os 4 posts do projeto), `dados/README.md` (fonte, licença, dicionário) e `imagens/`.
- Arquivos de trabalho já criados: 4 consultas SQL comentadas no projeto 01, 8 notebooks com o roteiro de cada etapa nos projetos 02 a 04 e o plano do dashboard em `projetos/02-dashboard-chamados/powerbi/`.
- Teste que confere se todo projeto tem o esqueleto completo e se os notebooks são válidos (`tests/test_estrutura.py`).
- `statsmodels` no `requirements.txt` (séries temporais do projeto 04).

### Alterado
- `linkedin/POSTS.md` virou o calendário dos 16 posts; os textos foram para o `LINKEDIN.md` de cada projeto.
- README principal e `PLANO_DE_ESTUDO.md` mostram a estrutura de cada projeto e a versão/tag de fechamento de cada um (0.3.0 → 1.0.0).

## [0.1.0] — 2026-10-28

### Adicionado
- Estrutura inicial do projeto (pasta, changelog duplo com `versao.py`, TECNICO/MANUAL a partir dos modelos oficiais).
- Plano de estudo de 4 meses para vaga de analista de dados com ML (`PLANO_DE_ESTUDO.md`), com checklist por semana.
- Pastas dos 4 projetos de portfólio (`projetos/01` a `04`), cada uma com README de objetivo, perguntas e entregáveis.
- Rascunhos de posts do LinkedIn (`linkedin/POSTS.md`), com o primeiro post pronto para publicar.
- Teste automático que confere se a versão em `versao.py`, `pyproject.toml` e `CHANGELOG.md` é a mesma (`tests/test_versao.py`), e lint com ruff.
