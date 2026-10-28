import re
import tomllib
from pathlib import Path

import versao

RAIZ = Path(__file__).resolve().parent.parent


def test_versao_bate_com_changelog_e_pyproject():
    changelog = (RAIZ / "CHANGELOG.md").read_text(encoding="utf-8")
    topo = re.search(r"^## \[(\d+\.\d+\.\d+)\]", changelog, re.MULTILINE)
    assert topo, "CHANGELOG.md sem entrada '## [x.y.z]'"
    pyproject = tomllib.loads((RAIZ / "pyproject.toml").read_text(encoding="utf-8"))
    assert versao.__version__ == topo.group(1) == pyproject["project"]["version"]
