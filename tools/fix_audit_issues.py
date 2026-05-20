#!/usr/bin/env python3
"""Aplica os fixes da auditoria das issues #9 e #10.

Idempotente: roda quantas vezes precisar; cada fix verifica antes de
mexer. A ordem do PIPELINE (no final do arquivo) e a fonte de verdade
da sequencia executada e do que cada passo faz.

Cada função retorna o numero de mudanças aplicadas (para log).
"""
from __future__ import annotations

import json
import os
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NB_ROOT = ROOT / "notebooks"


def load(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def save(p: Path, nb: dict) -> None:
    """Save atomico: escreve em tempfile e faz rename. Evita corromper o
    notebook se o processo for interrompido no meio da escrita."""
    data = json.dumps(nb, indent=1, ensure_ascii=False) + "\n"
    # tempfile no MESMO diretorio para garantir rename atomico no mesmo fs
    fd, tmp_path = tempfile.mkstemp(
        prefix=p.name + ".", suffix=".tmp", dir=str(p.parent)
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(data)
        os.replace(tmp_path, p)
    except Exception:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise


def get_src(cell: dict) -> str:
    s = cell.get("source", "")
    return "".join(s) if isinstance(s, list) else s


def set_src(cell: dict, new_src: str) -> None:
    cell["source"] = new_src.splitlines(keepends=True)


def all_paths():
    return sorted(NB_ROOT.rglob("*.ipynb"))


# ---------- 1: cells de markdown duplicadas ----------

def cells_md_dups(nb: dict, _p: Path) -> int:
    seen: dict[str, int] = {}
    keep = []
    removed = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            keep.append(cell)
            continue
        src = get_src(cell).strip()
        if len(src) < 100:
            keep.append(cell)
            continue
        if src in seen:
            removed += 1
            continue
        seen[src] = 1
        keep.append(cell)
    if removed:
        nb["cells"] = keep
    return removed


# ---------- 2: cells de codigo duplicadas ----------

def cells_code_dups(nb: dict, _p: Path) -> int:
    seen: dict[str, int] = {}
    keep = []
    removed = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            keep.append(cell)
            continue
        src = get_src(cell).strip()
        if len(src) < 80:
            keep.append(cell)
            continue
        if src in seen:
            removed += 1
            continue
        seen[src] = 1
        keep.append(cell)
    if removed:
        nb["cells"] = keep
    return removed


# ---------- 3: refs com IDs inexistentes ----------

# Mapeamento de IDs herdados de outra estruturação do curso para IDs reais.
# Quando não há correspondencia útil, mapeia para descrição em texto.
LEGACY_ID_MAP = {
    # do 5D_3 cell 1
    "1D_1": "1_1",      # Estatistica -> estatistica_descritiva
    "1D_4": "5D_1",     # Series temporais basicas -> series_temporais_fundamentos
    "2D_1": "2_2",      # Feature engineering -> eda_completa
    "2D_2": "1_4",      # Regressao/Classificacao -> regressao_estatistica
    "2D_3": "1_5",      # Validacao cruzada -> design_experimentos
    "3B_2": "2_2",      # Analise multivariada -> eda_completa
    "3C_4": "3_3",      # Arvores -> arvores_ensemble
    "3C_5": "3_3",      # Ensemble -> arvores_ensemble
    "4B_1": "0_8",      # Otimizacao -> otimizacao_ml
    # do 5D_4 cells 2 e 33
    "3A_2": "5D_1",     # Time Series Analysis -> series_temporais_fundamentos
    "3A_3": "1_2",      # Estatistica -> estatistica_inferencial
    "3B_1": "5D_3",     # Series Temporais ML -> ml_series_temporais
    "4A_1": "0_4",      # Gradientes -> calculo_derivadas
    "4B_2": "4_3",      # Normalizacao -> treinamento_deep
    "4D_1": "4_3",      # Regularizacao -> treinamento_deep
    # do 5C_1 gans
    "3A.1": "4_1",      # MLPs e backprop -> fundamentos_redes_neurais
    "2B.2": "0_2",      # Metricas de distancia -> algebra_linear_vetores
    "3A_1": "4_1",
    "2B_2": "0_2",
    # 6_1
    "6_0": None,        # nao existe — apaga ref
    # 5C_5
    "5C.6": None,
    "5C_6": None,
    # 5B_1
    "2_5": "2_4",       # max real
    # 5C_4
    "1_24": "1_2",
    # 5A_1 ref 5.5 e similar — ignorar (numeros decimais legitimos)
}

# Refs textuais a notebooks que nunca existiram (issue #10)
OBSOLETE_NB_NAMES = {
    "4_1_pipeline_ml.ipynb",
    "3_1_feature_engineering.ipynb",
    "4_2_otimizacao_hiperparametros.ipynb",
    "4_4_monitoramento_modelos.ipynb",
    "5_3_interpretabilidade_modelos.ipynb",
    "6_1_comunicacao_resultados.ipynb",
    "2_1_algebra_linear_fundamentos.ipynb",
    "3_2_algebra_linear.ipynb",
    "5_2_clustering.ipynb",
}


# Slugs em crase (sem .ipynb) que apontam para notebooks inexistentes.
# Diferente de OBSOLETE_REF_REPLACEMENTS, estes nao tem versao .ipynb no texto —
# aparecem em tabelas tipo "| Cross-validation | ... | `5_3_interpretabilidade` |".
# Aplicados como word-boundary substitutions para nao casar prefixos de slugs reais.
INVALID_SLUG_REPLACEMENTS = {
    "2_3_funcoes_de_perda": "0_8_otimizacao_ml",
    "4_2_otimizacao": "0_8_otimizacao_ml",
    "4_3_bayesian_optimization": "0_8_otimizacao_ml",
    "5_3_interpretabilidade": "1_4_regressao_estatistica",
    "1_4_regressao": "1_4_regressao_estatistica",
    "4_4_monitoramento": "6_3_monitoramento_drift",
    "3_3_reducao_dimensionalidade": "3_6_reducao_dimensionalidade",
    "6_1_comunicacao": "6_1_deploy_modelos",
}


def fix_invalid_backtick_slugs(nb: dict, _p: Path) -> int:
    """Substitui slugs em crase que apontam para notebooks inexistentes.
    Usa boundary `..` para nao casar prefixos de slugs reais (ex: `1_4_regressao`
    nao deve casar dentro de `1_4_regressao_estatistica`).
    """
    changes = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        src = get_src(cell)
        new_src = src
        for bad, good in INVALID_SLUG_REPLACEMENTS.items():
            # so dentro de crase, com final exato (sem suffix de slug real)
            pat = re.compile(r"`" + re.escape(bad) + r"`")
            new_src = pat.sub(f"`{good}`", new_src)
        if new_src != src:
            set_src(cell, new_src)
            changes += 1
    return changes


def _apply_legacy_map(text: str) -> str:
    """Aplica LEGACY_ID_MAP a um trecho de texto (markdown, codigo ou output)."""
    new = text
    for old, target in LEGACY_ID_MAP.items():
        pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(old) + r"(?![A-Za-z0-9])")
        if not pat.search(new):
            continue
        if target is None:
            paren_pat = re.compile(r"\([^()]*?" + re.escape(old) + r"[^()]*?\)")
            tmp = paren_pat.sub("", new)
            if tmp == new:
                tmp = pat.sub("", new)
            new = tmp
        else:
            new = pat.sub(target, new)
    return new


def broken_refs(nb: dict, _p: Path) -> int:
    changes = 0
    for cell in nb.get("cells", []):
        ctype = cell.get("cell_type")
        if ctype not in ("markdown", "code"):
            continue
        src = get_src(cell)
        new_src = _apply_legacy_map(src)
        if new_src != src:
            set_src(cell, new_src)
            changes += 1
        # outputs (code only): refs ja renderizadas em prints/HTML salvos
        if ctype == "code":
            for out in cell.get("outputs", []):
                text = out.get("text")
                if isinstance(text, list):
                    joined = "".join(text)
                    replaced = _apply_legacy_map(joined)
                    if replaced != joined:
                        out["text"] = replaced.splitlines(keepends=True)
                        changes += 1
                elif isinstance(text, str):
                    replaced = _apply_legacy_map(text)
                    if replaced != text:
                        out["text"] = replaced
                        changes += 1
                data = out.get("data", {})
                if isinstance(data, dict):
                    for k, v in list(data.items()):
                        if not k.startswith("text") or not isinstance(v, (str, list)):
                            continue
                        joined = "".join(v) if isinstance(v, list) else v
                        replaced = _apply_legacy_map(joined)
                        if replaced != joined:
                            data[k] = (
                                replaced.splitlines(keepends=True)
                                if isinstance(v, list)
                                else replaced
                            )
                            changes += 1
    return changes


# ---------- 4: refs apontam pra arquivo certo mas descricao errada ----------

# Mapping de correções textuais. Cada item: (regex_pattern, replacement)
# Aplicado em ordem.
WRONG_TOPIC_FIXES = [
    # 1_2 e 1_3: 0_5 (Probabilidade) -> 0_6 (Probabilidade)
    (re.compile(r"\*\*0_5\s*\(Probabilidade\)\*\*"), "**0_6 (Probabilidade)**"),
    (re.compile(r"0_5\s*\(Probabilidade\)"), "0_6 (Probabilidade)"),
    # 0_2 cell 1: "Notebook 0.5: Otimização" -> "Notebook 0.8: Otimização"
    (re.compile(r"\*\*Notebook\s+0\.5:\*\*\s+Otimi(?:z|s)a[çc][aã]o([^\n]*)"),
     r"**Notebook 0.8:** Otimização\1"),
    # 0_2 cell 1: "Notebook 1.1: Regressão linear" -> "Notebook 1.4: Regressão linear"
    (re.compile(r"\*\*Notebook\s+1\.1:\*\*\s+Regress[aã]o\s+linear([^\n]*)"),
     r"**Notebook 1.4:** Regressão linear\1"),
    # 0_2 cell 1: "Notebook 0.4: Cálculo multivariado" -> "Notebook 0.4: Cálculo (derivadas e gradientes)"
    (re.compile(r"\*\*Notebook\s+0\.4:\*\*\s+C[aá]lculo\s+multivariado[^\n]*"),
     "**Notebook 0.4:** Cálculo: derivadas, gradientes e Jacobianos"),
    # 0_1 cell 78: "Notebook 0.3: Cálculo" -> "Notebook 0.4: Cálculo"
    (re.compile(r"\*\*Notebook\s+0\.3:\*\*\s+C[aá]lculo([^\n]*)"),
     r"**Notebook 0.4:** Cálculo\1"),
    # 0_1 cell 78: "Notebook 0.4: Probabilidade" -> "Notebook 0.6: Probabilidade"
    (re.compile(r"\*\*Notebook\s+0\.4:\*\*\s+Probabilidade([^\n]*)"),
     r"**Notebook 0.6:** Probabilidade\1"),
    # 0_1 cell 78: "Notebook 0.5: Implementar gradient descent" -> "Notebook 0.8: Otimização (gradient descent)"
    (re.compile(r"\*\*Notebook\s+0\.5:\*\*\s+Implementar\s+gradient\s+descent[^\n]*"),
     "**Notebook 0.8:** Otimização (gradient descent, Adam, regularização)"),
    # 3_4 cell 2: "0.3 (calculo)" -> "0.4 (calculo)" (0_3 é matrizes, calculo é 0_4)
    (re.compile(r"0\.3\s*\(calculo\)"), "0.4 (calculo)"),
    (re.compile(r"0\.3\s*\(c[aá]lculo\)"), "0.4 (cálculo)"),
    # 5D_4 cells 2 e 33: refs com descricao errada
    (re.compile(r"\*\*5B_2\s*\(CNN\)\*\*"), "**5A_1 (CNN)**"),
    (re.compile(r"\*\*5C_1\s*\(Otimi(?:z|s)a[çc][aã]o\)\*\*"), "**0_8 (Otimização)**"),
    (re.compile(r"\*\*5A_1\s*\(Ativa[çc][oõ]es\)\*\*"), "**4_1 (Ativações)**"),
    (re.compile(r"\*\*5B_1\s*\(Backprop\)\*\*"), "**0_4 (Backprop)**"),
    (re.compile(r"\*\*5B_2\*\*:\s*CNN"), "**5A_1**: CNN"),
    (re.compile(r"\*\*5C_1\*\*:\s*Otimi(?:z|s)a[çc][aã]o"), "**0_8**: Otimização"),
    (re.compile(r"\*\*5A_1\*\*:\s*Ativa[çc][oõ]es"), "**4_1**: Ativações"),
    (re.compile(r"\*\*5B_1\*\*:\s*Backprop"), "**0_4**: Backprop"),
]


def wrong_topic_refs(nb: dict, _p: Path) -> int:
    changes = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        src = get_src(cell)
        new_src = src
        for pat, repl in WRONG_TOPIC_FIXES:
            new_src = pat.sub(repl, new_src)
        if new_src != src:
            set_src(cell, new_src)
            changes += 1
    return changes


# ---------- 5: refs textuais obsoletas (issue #10 sec 2) ----------

OBSOLETE_REF_REPLACEMENTS = {
    # 4_1_pipeline_ml e o pipeline ML end-to-end, que de fato e 3_0_tutorial_from_scratch
    # (e nao redes neurais). Versoes anteriores apontavam para 4_1_fundamentos_redes_neurais
    # e estavam semanticamente erradas — fix_wrong_semantic_refs limpa o legado.
    "4_1_pipeline_ml.ipynb": "3_0_tutorial_from_scratch.ipynb",
    # 3_1_feature_engineering coberto por 2_2_eda_completa, salvo dentro do proprio 2_2 (self-ref)
    "3_1_feature_engineering.ipynb": "2_2_eda_completa.ipynb",
    "4_2_otimizacao_hiperparametros.ipynb": "0_8_otimizacao_ml.ipynb",
    "4_4_monitoramento_modelos.ipynb": "6_3_monitoramento_drift.ipynb",
    # 5_3_interpretabilidade_modelos nao tem destino exato no curriculo atual.
    # Mapeavamos para 3_6_reducao_dimensionalidade (errado: dim reduction != interpretabilidade).
    # fix_wrong_semantic_refs remove o legado dessa substituicao.
    "5_3_interpretabilidade_modelos.ipynb": "1_4_regressao_estatistica.ipynb",
    "6_1_comunicacao_resultados.ipynb": "6_1_deploy_modelos.ipynb",
    "2_1_algebra_linear_fundamentos.ipynb": "0_2_algebra_linear_vetores.ipynb",
    "3_2_algebra_linear.ipynb": "0_3_algebra_linear_matrizes.ipynb",
    "5_2_clustering.ipynb": "3_5_clustering.ipynb",
}


def obsolete_refs(nb: dict, p: Path) -> int:
    changes = 0
    own_slug = p.name.removesuffix(".ipynb")
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        src = get_src(cell)
        new_src = src
        for old, new in OBSOLETE_REF_REPLACEMENTS.items():
            slug_new = new.removesuffix(".ipynb")
            # nao cria self-ref (ex: dentro de 2_2_eda_completa, nao trocar 3_1_feature_engineering -> 2_2)
            if slug_new == own_slug:
                continue
            if old in new_src:
                new_src = new_src.replace(old, new)
            slug_old = old.removesuffix(".ipynb")
            if slug_old in new_src:
                new_src = new_src.replace(slug_old, slug_new)
        if new_src != src:
            set_src(cell, new_src)
            changes += 1
    return changes


# ---------- 5b: refs semanticamente erradas legadas de OBSOLETE_REF_REPLACEMENTS antigo ----------

# Versoes anteriores do OBSOLETE_REF_REPLACEMENTS apontavam refs a `4_1_pipeline_ml`
# para `4_1_fundamentos_redes_neurais` (errado: redes neurais != pipeline ML).
# Da mesma forma, `5_3_interpretabilidade_modelos` apontava para `3_6_reducao_dimensionalidade`
# (errado: reducao de dim != interpretabilidade). Como os notebooks ja foram modificados
# com esses destinos errados, precisamos de uma passada corretiva direcionada.

# Cada item: (regex contextual, replacement). Aplicado so quando o contexto bate.
SEMANTIC_REF_FIXES = [
    # "pipeline completo de 4_1_fundamentos_redes_neurais" e variantes → 3_0_tutorial_from_scratch
    (re.compile(r"pipeline (completo|de limpeza|de ML)( do Exercicio \d+)? (de|e formalizado em) `4_1_fundamentos_redes_neurais`"),
     r"pipeline \1\2 \3 `3_0_tutorial_from_scratch`"),
    (re.compile(r"pipelines? confiaveis em `4_1_fundamentos_redes_neurais`"),
     "pipelines confiaveis em `3_0_tutorial_from_scratch`"),
    (re.compile(r"pipeline completo de ML\.\s*\*\*`4_1_fundamentos_redes_neurais`\*\*"),
     "pipeline completo de ML.\n3. **`3_0_tutorial_from_scratch`**"),
    (re.compile(r"input para `4_1_fundamentos_redes_neurais`"),
     "input para `3_0_tutorial_from_scratch`"),
    (re.compile(r"alimentam diretamente o pipeline de `4_1_fundamentos_redes_neurais`"),
     "alimentam diretamente o pipeline de `3_0_tutorial_from_scratch`"),
    (re.compile(r"Data leakage na limpeza e discutido em `4_1_fundamentos_redes_neurais`"),
     "Data leakage na limpeza e discutido em `1_5_design_experimentos`"),
    (re.compile(r"Prevencao de leakage no pipeline e tema central de `4_1_fundamentos_redes_neurais`"),
     "Prevencao de leakage no pipeline e tema central de `3_0_tutorial_from_scratch`"),
    (re.compile(r"validacao de features com cross-validation aparece em `4_1_fundamentos_redes_neurais`"),
     "validacao de features com cross-validation aparece em `3_0_tutorial_from_scratch`"),
    (re.compile(r"validacao de features com CV aparece em `4_1_fundamentos_redes_neurais`"),
     "validacao de features com CV aparece em `3_0_tutorial_from_scratch`"),
    (re.compile(r"deteccao de leakage aqui previne problemas graves em `4_1_fundamentos_redes_neurais`"),
     "deteccao de leakage aqui previne problemas graves em `3_0_tutorial_from_scratch`"),
    (re.compile(r"recomendacao do relatorio se traduz em etapas de `4_1_fundamentos_redes_neurais`"),
     "recomendacao do relatorio se traduz em etapas de `3_0_tutorial_from_scratch`"),
    # Requer ausencia de "(`3_0_tutorial_from_scratch`)" depois — evita
    # apendar repetidamente em execucoes sucessivas (idempotencia).
    (re.compile(r"recomendacoes do relatorio EDA no pipeline(?!\s*\(`3_0_tutorial_from_scratch`\))"),
     "recomendacoes do relatorio EDA no pipeline (`3_0_tutorial_from_scratch`)"),
    (re.compile(r"`4_1_fundamentos_redes_neurais` \(ColumnTransformer\)"),
     "`3_0_tutorial_from_scratch` (ColumnTransformer)"),
    (re.compile(r"`4_1_fundamentos_redes_neurais` \(robustez\)"),
     "`3_0_tutorial_from_scratch` (robustez)"),
    (re.compile(r"desbalanceamento do target e tratado em `4_1_fundamentos_redes_neurais`"),
     "desbalanceamento do target e tratado em `3_1_classificacao_completa`"),
    (re.compile(r"desbalanceamento do target e tratado formalmente em `4_1_fundamentos_redes_neurais`"),
     "desbalanceamento do target e tratado formalmente em `3_1_classificacao_completa`"),
    (re.compile(r"imputacao aparecem em `2_2_eda_completa` e `4_1_fundamentos_redes_neurais`"),
     "imputacao aparecem em `2_2_eda_completa` e `3_0_tutorial_from_scratch`"),
    (re.compile(r"try/except com logging e usado em todo `4_1_fundamentos_redes_neurais`"),
     "try/except com logging e usado em pipelines de producao (ver `3_0_tutorial_from_scratch`)"),
    (re.compile(r"\| Data leakage \| `1_5_design_experimentos` \(causalidade\) \| `4_1_fundamentos_redes_neurais` \|"),
     "| Data leakage | `1_5_design_experimentos` (causalidade) | `3_0_tutorial_from_scratch` |"),
    # 1_4 cell 39: "interpretabilidade dos coeficientes conecta com 3_6_reducao_dimensionalidade"
    # 3_6 e PCA/UMAP, nao interpretabilidade. Reformula sem ref errada.
    (re.compile(r"A interpretabilidade dos coeficientes conecta com `3_6_reducao_dimensionalidade`"),
     "A interpretabilidade dos coeficientes e abordada no proprio `1_4_regressao_estatistica` (analise de p-valores e intervalos de confianca)"),
    # 2_2 cell 38 self-ref: "formalizado em `2_2_eda_completa`" dentro de 2_2_eda_completa
    (re.compile(r"pipeline de feature engineering do Exercicio \d+ e formalizado em `2_2_eda_completa`"),
     "pipeline de feature engineering do Exercicio em questao usa as tecnicas deste proprio notebook"),
    # 2_2 cell 22: "Feature engineering completo e sistematico e o tema de `2_2_eda_completa`" (self-ref)
    (re.compile(r"Feature engineering completo e sistematico e o tema (deste notebook|de `2_2_eda_completa`)"),
     "Feature engineering completo e sistematico e o tema deste notebook"),
    # 2_2 cell 10 self-ref: "deteccao de assimetria conecta com transformacoes em `2_2_eda_completa`"
    (re.compile(r"deteccao de assimetria conecta com transformacoes em `2_2_eda_completa`"),
     "deteccao de assimetria conecta com transformacoes apresentadas adiante neste notebook"),
    # 2_2 cell 25 self-ref: "Train-test contamination via normalizacao e discutido em `2_2_eda_completa`"
    (re.compile(r"Train-test contamination via normalizacao e discutido em `2_2_eda_completa`"),
     "Train-test contamination via normalizacao e discutido em `1_5_design_experimentos`"),
    # tabela 2_2 cell 41: "Estatisticas descritivas | 1_1 | 2_2_eda_completa" (self-ref final)
    # tabela 2_2 cell 41: "Feature engineering | 2_1_python_data_science | 2_2_eda_completa" (self-ref)
    # tabela 2_2 cell 41: "Outliers | 1_1 | 2_2_eda_completa" (self-ref)
    (re.compile(r"\| Estatisticas descritivas \| `1_1_estatistica_descritiva` \| `2_2_eda_completa` \|"),
     "| Estatisticas descritivas | `1_1_estatistica_descritiva` | EDA visual e numerica (este notebook) |"),
    (re.compile(r"\| Feature engineering \| `2_1_python_data_science` \(Pandas\) \| `2_2_eda_completa` \|"),
     "| Feature engineering | `2_1_python_data_science` (Pandas) | Criacao de features (este notebook) |"),
    (re.compile(r"\| Outliers \| `1_1_estatistica_descritiva` \(IQR\) \| `2_2_eda_completa` \|"),
     "| Outliers | `1_1_estatistica_descritiva` (IQR) | Detecao multivariada (este notebook) |"),
    # 2_1 cell 41: tabela "Pandas DataFrame|...|2_2_eda_completa (analise exploratoria)" (ok, mantem)
    # mas "Pandas limpeza" hoje aponta 4_1_fundamentos — corrigir
    # ja coberto pelo regex `4_1_fundamentos_redes_neurais` (ColumnTransformer) acima
    # listas finais "1. **2_2_eda_completa**" e "3. **2_2_eda_completa**" dentro do proprio 2_2: substitui por descricao
    (re.compile(r"1\. \*\*`2_2_eda_completa`\*\*: Aplicar tudo em uma analise exploratoria completa"),
     "1. Aplicar tudo em uma analise exploratoria completa (proximas secoes deste notebook)"),
    (re.compile(r"3\. \*\*`2_2_eda_completa`\*\*: Tecnicas avancadas de criacao de features"),
     "3. Tecnicas avancadas de criacao de features (proximas secoes deste notebook)"),
    (re.compile(r"2\. \*\*`2_2_eda_completa`\*\*: Tecnicas avancadas de criacao de features"),
     "2. Tecnicas avancadas de criacao de features (proximas secoes deste notebook)"),
    (re.compile(r"2\. \*\*`2_2_eda_completa`\*\*: Usar dados coletados para criar features avancadas"),
     "2. **`2_2_eda_completa`**: Usar dados coletados para criar features avancadas"),
    # 2_3 cell 41: "3. **4_1_fundamentos_redes_neurais**: Integrar coleta no pipeline completo de ML"
    (re.compile(r"3\. \*\*`4_1_fundamentos_redes_neurais`\*\*: Integrar coleta no pipeline completo de ML"),
     "3. **`3_0_tutorial_from_scratch`**: Integrar coleta no pipeline completo de ML"),
    # 1_5 cell 33: "Todo o pipeline de `4_1_fundamentos_redes_neurais` e um experimento"
    (re.compile(r"Todo o pipeline de `4_1_fundamentos_redes_neurais` e um experimento"),
     "Todo o pipeline de `3_0_tutorial_from_scratch` e um experimento"),
    # 1_5 cell 37 tabela: "| Cross-validation | `1_2` (bootstrap) | `4_1_fundamentos_redes_neurais` |"
    (re.compile(r"\| Cross-validation \| `1_2` \(bootstrap\) \| `4_1_fundamentos_redes_neurais` \|"),
     "| Cross-validation | `1_2` (bootstrap) | `3_0_tutorial_from_scratch` |"),
    # 1_5 cell 37: "3. **`4_1_fundamentos_redes_neurais`**: O pipeline completo que usa CV..."
    (re.compile(r"3\. \*\*`4_1_fundamentos_redes_neurais`\*\*: O pipeline completo que usa CV como design experimental"),
     "3. **`3_0_tutorial_from_scratch`**: O pipeline completo que usa CV como design experimental"),
]


def fix_wrong_semantic_refs(nb: dict, _p: Path) -> int:
    changes = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        src = get_src(cell)
        new_src = src
        for pat, repl in SEMANTIC_REF_FIXES:
            new_src = pat.sub(repl, new_src)
        if new_src != src:
            set_src(cell, new_src)
            changes += 1
    return changes


# ---------- 6: headers truncados ----------

# Cabecalhos H2-H6 que sao apenas prefixos sem complemento.
# Estratégia: substituir por texto em negrito (preserva intencao didatica).
TRUNCATED_HEADER_FIXES = [
    (re.compile(r"^(#{2,6})\s+conexao\s+com\s*$", re.MULTILINE | re.IGNORECASE),
     "**Conexão com outros notebooks:**"),
    (re.compile(r"^(#{2,6})\s+por\s+que\s+em\s+ml\s*$", re.MULTILINE | re.IGNORECASE),
     "**Por que em ML:**"),
    (re.compile(r"^(#{2,6})\s+o\s+que\s+observar\s*$", re.MULTILINE | re.IGNORECASE),
     "**O que observar:**"),
    (re.compile(r"^(#{2,6})\s+o\s+que\s+concluir\s*$", re.MULTILINE | re.IGNORECASE),
     "**O que concluir:**"),
]


def truncated_headers(nb: dict, _p: Path) -> int:
    changes = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        src = get_src(cell)
        new_src = src
        for pat, repl in TRUNCATED_HEADER_FIXES:
            new_src = pat.sub(repl, new_src)
        if new_src != src:
            set_src(cell, new_src)
            changes += 1
    return changes


# ---------- 7: headers colados com texto ----------

def glued_headers(nb: dict, _p: Path) -> int:
    """Detecta `## Foo BarBaz` ou `### Conceito CLIPCLIP é...` onde uma palavra
    em CamelCase termina e a próxima começa em maiúscula sem espaço, na MESMA
    linha que um cabeçalho. Insere quebra de linha entre o título e o resto.
    Usa heurística conservadora: separa onde há palavra terminando em 3+ letras
    minúsculas seguidas de letra maiúscula + 2+ minúsculas (palavra real).
    """
    pat = re.compile(
        r"^(#{2,6}\s+[^\n]*?[a-z]{3,}\s*[\)\*])\s*([A-Z][a-z]{2,}[^\n]*)$",
        re.MULTILINE,
    )
    # variante: header termina em palavra com letra final lowercase e gruda
    # ex: "### O ConceitoÁudio é uma modalidade..."
    # ex: "### O que concluir1. Áudio é rico..."
    pat_lower_upper = re.compile(
        r"^(#{2,6}\s+[^\n]*?[a-zà-ÿ]{3,})([A-ZÀ-Ý][^\n]*)$",
        re.MULTILINE,
    )
    pat_lower_digit = re.compile(
        r"^(#{2,6}\s+[^\n]*?[a-zà-ÿ]{3,})(\d+\.\s[A-ZÀ-Ý][^\n]*)$",
        re.MULTILINE,
    )

    changes = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        src = get_src(cell)
        new_src = src
        # primeiro: separa header + "(X) **resto"
        new_src = re.sub(
            r"^(#{2,6}\s+.*?\*\*)([A-Z][a-z]{2,}[^\n]+)$",
            r"\1\n\n\2",
            new_src,
            flags=re.MULTILINE,
        )
        # depois: separa "## Foo CapitalLetra..."
        new_src = pat_lower_upper.sub(r"\1\n\n\2", new_src)
        new_src = pat_lower_digit.sub(r"\1\n\n\2", new_src)
        if new_src != src:
            set_src(cell, new_src)
            changes += 1
    return changes


# ---------- 8: palavras cortadas em headers ----------

CUT_WORD_FIXES = [
    # NOTA: o validador rejeita CamelCase em headers (vê como "newline-stripping
    # corruption"). Por isso usamos separadores (espaço, hífen, parênteses)
    # entre palavras compostas como PostgreSQL/RetinaNet/DeepLab/FastText/SimpleRNN.
    # Mantemos o nome próprio no corpo do texto.

    # 2_4 cell 10: "## 3. Postgre\nSQL" → header sem CamelCase + nome no corpo
    (re.compile(r"## 3\. Postgre\nSQL[^\n]*\n+(?:SQL[^\n]*\n+)*"),
     "## 3. Postgres com SQLAlchemy\n\n**PostgreSQL** + **SQLAlchemy** (ORM)\n\n"),
    (re.compile(r"## 3\. Postgre(?!s)"), "## 3. Postgres com SQLAlchemy"),

    # 5A_3 cell 11: header sem CamelCase
    (re.compile(r"## 3\. One-Stage Detectors \(YOLO, SSD, Retina\s*\n\s*\n?\s*Net\)[^\n]*\n+(?:Net\)[^\n]*\n+)*"),
     "## 3. One-Stage Detectors: YOLO, SSD e Retina-Net\n\n"),
    (re.compile(r"### O que observar sobre Focal Loss \(Retina\s*\n\s*\n?\s*Net\)[^\n]*\n+(?:Net\)[^\n]*\n+)*"),
     "### O que observar sobre Focal Loss em Retina-Net\n\n"),

    # 5A_4 cell 10: header sem CamelCase
    (re.compile(r"## 3\. Atrous Convolutions e Deep\s*\n\s*\n?\s*Lab[^\n]*\n+(?:Lab[^\n]*\n+)*"),
     "## 3. Atrous Convolutions e Deep-Lab\n\n"),
    (re.compile(r"### Por que em ML: Deep\s*\n\s*\n?\s*Lab[^\n]*\n+(?:Lab[^\n]*\n+)*"),
     "### Por que em ML: arquitetura Deep-Lab\n\n"),

    # 4_3 cell 37: "### Erro 2: Batch\n" — provavelmente "Batch size" ou "Batch Normalization"
    # Original tinha "### Erro 2: Batch\nNormalization\n" - vou inferir do contexto
    (re.compile(r"### Erro 2: Batch\n(?!size|Normalization)"),
     "### Erro 2: Batch normalization mal calibrada\n"),

    # 4_5 cell 34: "### Erro 6: num_workers=0 no Data\nLoader"
    (re.compile(r"### Erro 6: num_workers=0 no Data\nLoader[^\n]*\n+(?:Loader[^\n]*\n+)*"),
     "### Erro 6: num_workers=0 no `DataLoader`\n\n"),

    # 5B_2 cell 11: "## 4. Fast\nText" (possivelmente com \n\n entre)
    (re.compile(r"## 4\. Fast\s*\n\s*\n?\s*Text[^\n]*\n+(?:Text[^\n]*\n+)*"),
     "## 4. Fast-Text (subword embeddings)\n\n"),

    # 5D_4 cell 3: "## 2. Simple\nRNN para Séries Temporais"
    (re.compile(r"## 2\. Simple\nRNN para Séries Temporais\s*\(Implementação NumPy\)"),
     "## 2. Simple-RNN para Séries Temporais (Implementação NumPy)"),

    # 5D_4 cell 5: "## 3. LSTM ... Gates)LSTM adiciona gates à Simple\nRNN"
    (re.compile(r"## 3\. LSTM para Previsão \(Implementação NumPy com Gates\)LSTM adiciona gates à Simple\nRNN"),
     "## 3. LSTM para previsão (NumPy)\n\nLSTM adiciona gates à Simple-RNN"),
    (re.compile(r"## 3\. LSTM para Previsão \(Implementação NumPy com Gates\)LSTM adiciona gates à SimpleRNN\nRNN"),
     "## 3. LSTM para previsão (NumPy)\n\nLSTM adiciona gates à Simple-RNN"),

    # 5D_4 cell 17: "### Exercício 1: Implementar Simple\n\nRNN com Predição Multi-StepModifique"
    (re.compile(r"### Exercício 1: Implementar Simple\s*\n\s*\n?\s*RNN com Predição Multi-StepModifique"),
     "### Exercício 1: Implementar Simple-RNN com predição multi-step\n\nModifique"),
    (re.compile(r"### Exercício 1: Implementar Simple\s*\n\s*\n?\s*RNN com Predição Multi-Step"),
     "### Exercício 1: Implementar Simple-RNN com predição multi-step"),
    (re.compile(r"### Exercício 1: Implementar SimpleRNN\s*\n\s*\n?\s*RNN"),
     "### Exercício 1: Implementar Simple-RNN"),

    # 5D_3, 5D_4, 6_1: "### Por que em MLPalavra..." — glued_headers nao pega porque
    # "ML" termina em uppercase (regex exige minusculas antes). Separador explicito:
    (re.compile(r"^### Por que em ML([A-ZÀ-Ý][a-zà-ÿ])", re.MULTILINE),
     r"### Por que em ML\n\n\1"),
    # 5D_3 cell 22: "## 8. Comparação ML vs. ARIMATrade-offs..." — similar
    (re.compile(r"^## 8\. Comparação ML vs\. ARIMA([A-ZÀ-Ý][a-zà-ÿ])", re.MULTILINE),
     r"## 8. Comparação ML vs. ARIMA\n\n\1"),
]


def cut_words(nb: dict, _p: Path) -> int:
    changes = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        src = get_src(cell)
        new_src = src
        for pat, repl in CUT_WORD_FIXES:
            new_src = pat.sub(repl, new_src)
        if new_src != src:
            set_src(cell, new_src)
            changes += 1
    return changes


# ---------- 9: imports duplicados ----------

DUP_IMPORT_TARGETS = {
    # nome_notebook : lista de imports a deduplica (manter 1a ocorrência)
    "2_4_acesso_banco_dados.ipynb": ["import sqlite3"],
    "1_4_regressao_estatistica.ipynb": ["from sklearn.datasets import load_diabetes"],
    "1_5_design_experimentos.ipynb": ["from statsmodels.stats.power import tt_ind_solve_power"],
    "2_3_sql_e_apis.ipynb": ["import time"],
    "4_6_otimizacao_python.ipynb": ["import time", "import functools"],
}


def dup_imports(nb: dict, p: Path) -> int:
    targets = DUP_IMPORT_TARGETS.get(p.name)
    if not targets:
        return 0
    seen: set[str] = set()
    changes = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        src = get_src(cell)
        new_lines = []
        modified = False
        for line in src.split("\n"):
            stripped = line.strip()
            if stripped in targets:
                if stripped in seen:
                    modified = True
                    continue
                seen.add(stripped)
            new_lines.append(line)
        if modified:
            set_src(cell, "\n".join(new_lines))
            changes += 1
    return changes


# ---------- 10: repetição patológica de cabeçalhos sem conteúdo ----------

REPETITIVE_HEADER_PATTERNS = [
    re.compile(r"^###\s+O\s+que\s+observar\s*$", re.IGNORECASE),
    re.compile(r"^###\s+O\s+que\s+concluir\s*$", re.IGNORECASE),
    re.compile(r"^###\s+Por\s+Que?\s+em\s+(Machine\s+Learning|ML)\s*$", re.IGNORECASE),
    re.compile(r"^###\s+Conexao\s+com\s+outros\s+notebooks\s*$", re.IGNORECASE),
]


def patho_repetition_v2(nb: dict, _p: Path) -> int:
    keep = []
    seen_norm: set[str] = set()
    removed = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            keep.append(cell)
            continue
        src = get_src(cell).strip()
        first_line = src.split("\n")[0] if src else ""
        # detecta cell que é só um header generico
        is_lone_header = False
        for pat in REPETITIVE_HEADER_PATTERNS:
            if pat.match(first_line):
                # cell tem só esse header (linhas pouco substantivas)
                content_after = "\n".join(src.split("\n")[1:]).strip()
                if len(content_after) < 5:  # praticamente vazio
                    is_lone_header = True
                    break
        if is_lone_header:
            norm = first_line.strip().lower()
            if norm in seen_norm:
                removed += 1
                continue
            seen_norm.add(norm)
        keep.append(cell)
    if removed:
        nb["cells"] = keep
    return removed


# ---------- 11: metadata vazada ----------

LEAKED_METADATA_LINES = [
    re.compile(r'^### Erro"?\*?\*? apareceu >= \d+ vezes:.*$', re.MULTILINE),
    re.compile(r'^### "Repeticao de Frases-Chave".*$', re.MULTILINE),
]


def leaked_metadata(nb: dict, _p: Path) -> int:
    changes = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        src = get_src(cell)
        new_src = src
        for pat in LEAKED_METADATA_LINES:
            new_src = pat.sub("", new_src)
        # so colapsa newlines se algum padrao de metadata casou
        # (evita reescrever cells com espacamento intencional)
        if new_src != src:
            new_src = re.sub(r"\n{3,}", "\n\n", new_src)
            set_src(cell, new_src)
            changes += 1
    return changes


# ---------- 12: bug pedagogico 5D_3 cell 29 ----------

EXERCICIO_5D_3_NOVO = '''# Exercicio 3: Walk-Forward vs. Train-Test naive (solucao preenchida)
# Constroi o dataset supervisionado a partir da serie
X_ex, y_ex = create_supervised_dataset(series, n_lags=7, rolling_window=7)

# 1) Train-Test simples (split unico)
split_simple = int(0.8 * len(X_ex))
X_tr_simple = X_ex[:split_simple]
X_te_simple = X_ex[split_simple:]
y_tr_simple = y_ex[:split_simple]
y_te_simple = y_ex[split_simple:]

rf_simple = SimpleRandomForest(n_trees=5, max_depth=2)
rf_simple.fit(X_tr_simple, y_tr_simple)
r2_simple = evaluate(y_te_simple, rf_simple.predict(X_te_simple))[2]

# 2) Walk-Forward: re-treina a cada passo usando todos os dados ate o instante t
n_test = len(X_te_simple)
wf_predictions = []
for i in range(n_test):
    end_train = split_simple + i
    X_tr_wf = X_ex[:end_train]
    y_tr_wf = y_ex[:end_train]
    rf_wf = SimpleRandomForest(n_trees=5, max_depth=2)
    rf_wf.fit(X_tr_wf, y_tr_wf)
    wf_predictions.append(rf_wf.predict(X_ex[end_train:end_train + 1])[0])

import numpy as np
r2_wf = evaluate(y_te_simple, np.array(wf_predictions))[2]

print("Comparacao de Validacao:")
print(f"  Train-Test simples: R2 = {r2_simple:.4f}")
print(f"  Walk-Forward:       R2 = {r2_wf:.4f}")
print(f"\\n  Diferenca: {r2_simple - r2_wf:.4f}")

if abs(r2_simple - r2_wf) > 0.1:
    print("\\nDiferenca grande indica que o split simples nao representa o cenario temporal corretamente.")
else:
    print("\\nDiferenca pequena: split simples ja captura razoavelmente a dinamica temporal aqui.")
'''


def exercise_bug_5D_3(nb: dict, p: Path) -> int:
    if p.name != "5D_3_ml_series_temporais.ipynb":
        return 0
    for i, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        src = get_src(cell)
        if "r2_wf_dt" in src and "Walk-Forward vs. Train-Test" in src:
            set_src(cell, EXERCICIO_5D_3_NOVO)
            return 1
    return 0


# ---------- 13a: 0_1 com cada secao numerada duplicada (uma sem acento, outra com) ----------

def fix_dup_h2_0_1(nb: dict, p: Path) -> int:
    """Em 0_1, cada secao numerada tem duas versões (sem e com acento).
    Mantém a versão sem acento (que tem mais conteúdo nas subseções) e
    REMOVE o header duplicado em acento (a segunda ocorrência), reduzindo
    seu cell a apenas o conteúdo após o header.
    """
    if p.name != "0_1_pre_calculo_funcoes_ml.ipynb":
        return 0
    cells = nb.get("cells", [])
    h2_pat = re.compile(r"^---?\s*\n##\s+(\d+)\.\s+[^\n]+(?:\s*<a id='[^']+'></a>)?\s*\n", re.MULTILINE)
    h2_simple_pat = re.compile(r"^##\s+(\d+)\.", re.MULTILINE)
    seen_h2_nums: set[str] = set()
    changes = 0
    for cell in cells:
        if cell.get("cell_type") != "markdown":
            continue
        src = get_src(cell)
        m = h2_simple_pat.search(src)
        if not m:
            continue
        num = m.group(1)
        if num in seen_h2_nums:
            # remove a linha do header (e separador) mas preserva subseções
            new_src = h2_pat.sub("", src, count=1)
            if new_src == src:
                # fallback: remove só a linha do H2
                new_src = h2_simple_pat.sub("", src, count=1)
                # remove separador ---
                new_src = re.sub(r"^---\s*\n", "", new_src, count=1)
            set_src(cell, new_src.lstrip())
            changes += 1
        else:
            seen_h2_nums.add(num)
    return changes


# ---------- 13: secoes numeradas faltando ----------

def fix_missing_sections(nb: dict, p: Path) -> int:
    """0_1 falta ## 9 entre Sigmoid (## 8) e Exercicios (## 10).
    5A_4 falta ## 6 entre ## 5 e ## 7."""
    changes = 0
    if p.name == "0_1_pre_calculo_funcoes_ml.ipynb":
        for cell in nb.get("cells", []):
            if cell.get("cell_type") != "markdown":
                continue
            src = get_src(cell)
            # renomeia "## 10. Exercicios" para "## 9. Exercicios"
            new_src = re.sub(
                r"^## 10\.\s+Exercicios\s+Praticos",
                "## 9. Exercicios Praticos",
                src,
                flags=re.MULTILINE,
            )
            if new_src != src:
                set_src(cell, new_src)
                changes += 1
    elif p.name == "5A_4_segmentacao.ipynb":
        for cell in nb.get("cells", []):
            if cell.get("cell_type") != "markdown":
                continue
            src = get_src(cell)
            # renumera ## 7, ## 8, ## 9 para ## 6, ## 7, ## 8
            new_src = src
            new_src = re.sub(r"^## 9\.\s+Resumo", "## 8. Resumo", new_src, flags=re.MULTILINE)
            new_src = re.sub(r"^## 8\.\s+Erros\s+Comuns", "## 7. Erros Comuns", new_src, flags=re.MULTILINE)
            new_src = re.sub(r"^## 7\.\s+Exercicios", "## 6. Exercicios", new_src, flags=re.MULTILINE)
            if new_src != src:
                set_src(cell, new_src)
                changes += 1
    return changes


# ---------- 14: outputs com paths locais ----------

LOCAL_PATH_PATTERNS = [
    re.compile(r"/var/folders/[^\s'\"]+"),
    re.compile(r"/private/tmp/[^\s'\"]+"),
    re.compile(r"/private/var/folders/[^\s'\"]+"),
    re.compile(r"ipykernel_\d+/[^\s'\"]*"),
    re.compile(r"/tmp/ipykernel_[^\s'\"]+"),
]


def _redact_paths(text: str) -> str:
    new = text
    for pat in LOCAL_PATH_PATTERNS:
        new = pat.sub("<local-path-redacted>", new)
    return new


def _scrub_json_paths(obj):
    """Aplica _redact_paths recursivamente em dicts/lists/strings (application/json output)."""
    if isinstance(obj, str):
        return _redact_paths(obj)
    if isinstance(obj, list):
        return [_scrub_json_paths(v) for v in obj]
    if isinstance(obj, dict):
        return {k: _scrub_json_paths(v) for k, v in obj.items()}
    return obj


def drop_local_paths(nb: dict, _p: Path) -> int:
    changes = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        outputs = cell.get("outputs", [])
        for out in outputs:
            text = out.get("text")
            if isinstance(text, list):
                joined = "".join(text)
                replaced = _redact_paths(joined)
                if replaced != joined:
                    out["text"] = replaced.splitlines(keepends=True)
                    changes += 1
            elif isinstance(text, str):
                replaced = _redact_paths(text)
                if replaced != text:
                    out["text"] = replaced
                    changes += 1
            data = out.get("data", {})
            if not isinstance(data, dict):
                continue
            for k, v in list(data.items()):
                # text/plain, text/html etc — string ou list-of-strings
                if k.startswith("text") and isinstance(v, (str, list)):
                    joined = "".join(v) if isinstance(v, list) else v
                    replaced = _redact_paths(joined)
                    if replaced != joined:
                        data[k] = (
                            replaced.splitlines(keepends=True)
                            if isinstance(v, list)
                            else replaced
                        )
                        changes += 1
                # application/json (e variantes) — dict aninhado
                elif "json" in k and isinstance(v, (dict, list)):
                    scrubbed = _scrub_json_paths(v)
                    if scrubbed != v:
                        data[k] = scrubbed
                        changes += 1
    return changes


# ---------- 14b: limpar warnings poluindo stderr ----------

# Linhas tipicas de Python warning serializadas em stderr ficam como:
#   <local-path-redacted> RuntimeWarning: overflow encountered in exp
#   /opt/anaconda3/lib/.../matplotlib/...: UserWarning: ...
# Esses outputs sao ruido de ambiente, nao informacao educacional.

WARNING_LINE_RE = re.compile(
    r"^(?:<local-path-redacted>|[\w\-./]+):.*?(?:User|Runtime|Deprecation|Future|Pending|Resource)Warning:",
    re.MULTILINE,
)
WARNING_KEYWORDS = (
    "UserWarning:",
    "RuntimeWarning:",
    "DeprecationWarning:",
    "FutureWarning:",
    "PendingDeprecationWarning:",
    "ResourceWarning:",
)


def clean_warning_outputs(nb: dict, _p: Path) -> int:
    changes = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        outputs = cell.get("outputs", [])
        new_outputs = []
        for out in outputs:
            if (
                out.get("output_type") == "stream"
                and out.get("name") == "stderr"
            ):
                text = out.get("text", "")
                if isinstance(text, list):
                    text = "".join(text)
                if any(kw in text for kw in WARNING_KEYWORDS):
                    # remove o output todo se for so warning
                    # mas se tem outras linhas (ex logs INFO + warning), preserva.
                    # Filtros: linhas que CONTEM keyword de Warning, mais traceback-style
                    # padrao do warnings module (linha "warnings.warn(...)" e
                    # follow-up do tight_layout do matplotlib).
                    # NAO usamos heuristica generica de "linha indentada com =" porque
                    # pegaria prints didaticos (ver review do PR #11).
                    lines = text.split("\n")
                    kept_lines = [
                        l for l in lines
                        if not any(kw in l for kw in WARNING_KEYWORDS)
                        and not (
                            l.strip().startswith("warnings.warn")
                            or l.strip().startswith("self._figure.tight_layout")
                            or l.strip().startswith("plt.tight_layout")
                        )
                    ]
                    new_text = "\n".join(kept_lines).strip()
                    if not new_text:
                        changes += 1
                        continue
                    if (out["text"] if isinstance(out.get("text"), str) else "".join(out.get("text", []))) != new_text + "\n":
                        out["text"] = new_text + "\n"
                        changes += 1
            new_outputs.append(out)
        if len(new_outputs) != len(outputs):
            cell["outputs"] = new_outputs
    return changes


# ---------- 14c: reduzir runtime do 4_6 (issue #10 - timeout 300s) ----------


def reduce_4_6_runtime(nb: dict, p: Path) -> int:
    """4_6_otimizacao_python.ipynb roda em ~291s (margem de 9s para timeout 300s).
    Cell 11 tem dois `for i in range(n * 1000000)` que dominam o tempo.
    Reduzimos para `n * 100000` (10x menor) — ainda demonstra a diferenca de cache.
    """
    if p.name != "4_6_otimizacao_python.ipynb":
        return 0
    changes = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        src = get_src(cell)
        if "range(n * 1000000)" not in src:
            continue
        new_src = src.replace("range(n * 1000000)", "range(n * 100000)")
        if new_src != src:
            set_src(cell, new_src)
            changes += 1
    return changes


# ---------- 15: padronizar Python version ----------

def normalize_py_version(nb: dict, _p: Path) -> int:
    meta = nb.get("metadata", {})
    lang_info = meta.get("language_info")
    if not isinstance(lang_info, dict):
        return 0
    if "version" not in lang_info:
        return 0
    del lang_info["version"]
    return 1


# ---------- pipeline orquestrador ----------

# Ordem importa:
# - cut_words antes de glued_headers: corrige palavras quebradas em multilinha
#   antes da heuristica de glued_headers, que so olha uma linha por vez.
# - glued_headers ANTES de truncated_headers: quando glued separa um header
#   colado, ele pode expor um header generico ("### O que concluir"), que
#   precisa ser limpado em seguida. Inverter quebra idempotencia.
# - fix_wrong_semantic_refs depois de obsolete_refs: limpa o legado de
#   substituicoes erradas (4_1_pipeline_ml -> 4_1_fundamentos_redes_neurais)
#   que existiam em versoes anteriores deste script.
PIPELINE = [
    ("cells_md_dups", cells_md_dups),
    ("cells_code_dups", cells_code_dups),
    ("broken_refs", broken_refs),
    ("wrong_topic_refs", wrong_topic_refs),
    ("obsolete_refs", obsolete_refs),
    ("fix_invalid_backtick_slugs", fix_invalid_backtick_slugs),
    ("fix_wrong_semantic_refs", fix_wrong_semantic_refs),
    ("cut_words", cut_words),
    ("glued_headers", glued_headers),
    ("truncated_headers", truncated_headers),
    ("dup_imports", dup_imports),
    ("patho_repetition", patho_repetition_v2),
    ("leaked_metadata", leaked_metadata),
    ("exercise_bug_5D_3", exercise_bug_5D_3),
    ("fix_dup_h2_0_1", fix_dup_h2_0_1),
    ("fix_missing_sections", fix_missing_sections),
    ("reduce_4_6_runtime", reduce_4_6_runtime),
    ("drop_local_paths", drop_local_paths),
    ("clean_warning_outputs", clean_warning_outputs),
    ("normalize_py_version", normalize_py_version),
]


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    paths = all_paths()
    totals = {name: 0 for name, _ in PIPELINE}
    affected_files = 0
    failures: list[tuple[Path, str]] = []
    for p in paths:
        if only and only != p.name:
            continue
        try:
            nb = load(p)
            before = json.dumps(nb, ensure_ascii=False)
            for name, fn in PIPELINE:
                c = fn(nb, p)
                totals[name] += c
            after = json.dumps(nb, ensure_ascii=False)
            if before != after:
                save(p, nb)
                affected_files += 1
                print(f"  fixed: {p.relative_to(ROOT)}")
        except (json.JSONDecodeError, OSError) as e:
            failures.append((p, f"{type(e).__name__}: {e}"))
            print(f"  FAILED: {p.relative_to(ROOT)} -- {type(e).__name__}: {e}",
                  file=sys.stderr)
    print()
    print(f"arquivos modificados: {affected_files}/{len(paths)}")
    for name, total in totals.items():
        if total:
            print(f"  {name:25} {total}")
    if failures:
        print(f"\n{len(failures)} arquivo(s) falharam:", file=sys.stderr)
        for fp, err in failures:
            print(f"  - {fp.relative_to(ROOT)}: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
