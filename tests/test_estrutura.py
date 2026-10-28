import json
from pathlib import Path

import pytest

PROJETOS = Path(__file__).resolve().parent.parent / "projetos"
OBRIGATORIOS = ["README.md", "ROTEIRO.md", "LINKEDIN.md", "dados/README.md", "imagens/.gitkeep"]


@pytest.mark.parametrize("projeto", sorted(p.name for p in PROJETOS.iterdir() if p.is_dir()))
def test_projeto_tem_esqueleto_completo(projeto):
    faltando = [f for f in OBRIGATORIOS if not (PROJETOS / projeto / f).exists()]
    assert not faltando, f"{projeto} sem: {faltando}"


def test_existem_os_4_projetos():
    assert len([p for p in PROJETOS.iterdir() if p.is_dir()]) == 4


@pytest.mark.parametrize("notebook", sorted(PROJETOS.glob("*/notebooks/*.ipynb")), ids=str)
def test_notebook_e_json_valido(notebook):
    conteudo = json.loads(notebook.read_text(encoding="utf-8"))
    assert conteudo["nbformat"] == 4 and conteudo["cells"]
