#!/usr/bin/env python3
"""Restore exercise scaffolds (TAREFA DO ALUNO) and add separate solution cells.

PR #4 review (P1) flagged that exercise cells were converted into "solucao
preenchida" in the same cell, breaking the didactic separation. This script
restores the original scaffold (the cell tagged `exercise` keeps the student
prompts with TAREFA DO ALUNO) and inserts a new cell tagged `solution`
immediately after each one with the working code.

Idempotent: skips cells where the solution cell is already present.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]


# ---------- Patch definitions ----------

EXERCISE_SVD_0_3 = """# EXERCICIO 3: Decomposicao em Autovalores
# TAREFA DO ALUNO: Implemente SVD truncado para reduzir dimensionalidade de uma matriz aleatoria

import numpy as np

# Crie matriz aleatoria 10x8
A = np.random.randn(10, 8)

# TAREFA DO ALUNO: Calcule SVD completo
U, s, Vt = None  # TAREFA DO ALUNO: use np.linalg.svd(A)

# TAREFA DO ALUNO: Mantenha apenas os 3 maiores valores singulares
k = 3
U_k = None  # TAREFA DO ALUNO
s_k = None  # TAREFA DO ALUNO
Vt_k = None  # TAREFA DO ALUNO

# TAREFA DO ALUNO: Reconstrua matriz aproximada
A_approx = None  # TAREFA DO ALUNO: A_k = U_k @ np.diag(s_k) @ Vt_k

# TAREFA DO ALUNO: Calcule erro de reconstrucao
erro_frobenius = None  # TAREFA DO ALUNO: use np.linalg.norm(A - A_approx)

print(f"Forma original: {A.shape}")
print(f"Valores singulares: {s}")
print(f"Erro de reconstrucao (rank-{k}): {erro_frobenius:.6f}")
print(f"Razao de compressao: {8*10 / (10*3 + 3 + 3*8):.2f}x")
"""

SOLUTION_SVD_0_3 = """# SOLUCAO - Exercicio 3 (SVD truncado)
import numpy as np

A = np.random.randn(10, 8)

U, s, Vt = np.linalg.svd(A, full_matrices=False)

k = 3
U_k = U[:, :k]
s_k = s[:k]
Vt_k = Vt[:k, :]

A_approx = U_k @ np.diag(s_k) @ Vt_k

erro_frobenius = np.linalg.norm(A - A_approx)

print(f"Forma original: {A.shape}")
print(f"Valores singulares: {s}")
print(f"Erro de reconstrucao (rank-{k}): {erro_frobenius:.6f}")
print(f"Razao de compressao: {8*10 / (10*3 + 3 + 3*8):.2f}x")
"""

EXERCISE_NORM_2_1 = """# TAREFA DO ALUNO: Exercicio 1 - NumPy vs Loop
import time

n = 1_000_000
vec = np.random.randn(n)

# (a) Loop Python puro - calcule norma L2: sqrt(sum(x_i^2))
start = time.time()
norma_loop = None  # TAREFA DO ALUNO: implementar com loop
tempo_loop = time.time() - start

# (b) NumPy vetorizado
start = time.time()
norma_numpy = None  # TAREFA DO ALUNO: implementar com np.sqrt e np.sum (ou np.linalg.norm)
tempo_numpy = time.time() - start

print(f"Loop: {norma_loop:.4f} em {tempo_loop:.4f}s")
print(f"NumPy: {norma_numpy:.4f} em {tempo_numpy:.4f}s")
print(f"Speedup: {tempo_loop/tempo_numpy:.1f}x")

# (c) Distancia euclidiana entre dois vetores
vec_a = np.random.randn(n)
vec_b = np.random.randn(n)
distancia = None  # TAREFA DO ALUNO: np.linalg.norm(vec_a - vec_b)
print(f"Distancia euclidiana: {distancia:.4f}")
"""

SOLUTION_NORM_2_1 = """# SOLUCAO - Exercicio 1 (NumPy vs Loop)
import time

n = 1_000_000
vec = np.random.randn(n)

# (a) Loop Python puro
start = time.time()
total = 0.0
for x in vec:
    total += float(x) ** 2
norma_loop = total ** 0.5
tempo_loop = time.time() - start

# (b) NumPy vetorizado
start = time.time()
norma_numpy = float(np.linalg.norm(vec))
tempo_numpy = time.time() - start

print(f"Loop:  {norma_loop:.4f} em {tempo_loop:.4f}s")
print(f"NumPy: {norma_numpy:.4f} em {tempo_numpy:.4f}s")
print(f"Speedup: {tempo_loop / max(tempo_numpy, 1e-12):.1f}x")

# (c) Distancia euclidiana
vec_a = np.random.randn(n)
vec_b = np.random.randn(n)
distancia = float(np.linalg.norm(vec_a - vec_b))
print(f"Distancia euclidiana: {distancia:.4f}")
"""

EXERCISE_CLEAN_2_1 = """# TAREFA DO ALUNO: Exercicio 2 - Limpeza de Dados
df_original = pd.DataFrame({
    'customer_id': ['C001', 'C002', 'C001', 'C003', None, 'C004'],
    'product': ['Notebook', 'Mouse', 'Notebook', 'Teclado', 'Monitor', 'Mouse'],
    'price': [3500, 45, 3500, 80, 1200, None],
    'purchase_date': ['2024-01-15', '2024-01-16', '2024-01-15', '2024-02-01', '2024-02-10', '2024-02-15'],
    'rating': [4.5, None, 4.5, 3.8, 4.2, 4.0]
})

print("Dataset original:")
print(df_original)
print(f"\\nNulos por coluna:\\n{df_original.isnull().sum()}")

# TAREFA DO ALUNO: 1. Remover duplicatas
df_clean = None  # TAREFA DO ALUNO

# TAREFA DO ALUNO: 2. Tratar nulos (customer_id: dropar, price: mediana, rating: media)
# TAREFA DO ALUNO

# TAREFA DO ALUNO: 3. Converter purchase_date para datetime
# TAREFA DO ALUNO

# TAREFA DO ALUNO: 4. Validar
print(f"\\nNulos restantes: {df_clean.isnull().sum().sum()}")
print(f"Duplicatas restantes: {df_clean.duplicated().sum()}")
"""

SOLUTION_CLEAN_2_1 = """# SOLUCAO - Exercicio 2 (Limpeza de Dados)
df_original = pd.DataFrame({
    'customer_id': ['C001', 'C002', 'C001', 'C003', None, 'C004'],
    'product': ['Notebook', 'Mouse', 'Notebook', 'Teclado', 'Monitor', 'Mouse'],
    'price': [3500, 45, 3500, 80, 1200, None],
    'purchase_date': ['2024-01-15', '2024-01-16', '2024-01-15', '2024-02-01', '2024-02-10', '2024-02-15'],
    'rating': [4.5, None, 4.5, 3.8, 4.2, 4.0],
})

# 1. Remover duplicatas
df_clean = df_original.drop_duplicates()

# 2. Tratar nulos
df_clean = df_clean.dropna(subset=['customer_id'])
df_clean['price'] = df_clean['price'].fillna(df_clean['price'].median())
df_clean['rating'] = df_clean['rating'].fillna(df_clean['rating'].mean())

# 3. Converter purchase_date para datetime
df_clean['purchase_date'] = pd.to_datetime(df_clean['purchase_date'])

# 4. Validar
print('Dataset limpo:')
print(df_clean)
print(f"\\nNulos restantes: {df_clean.isnull().sum().sum()}")
print(f"Duplicatas restantes: {df_clean.duplicated().sum()}")
"""

EXERCISE_BAYES_1_5 = """# TAREFA DO ALUNO: Exercicio 2 - A/B Test Bayesiano
conv_a, trials_a = 1200, 15000
conv_b, trials_b = 1350, 15000

# 1. Prior: Beta(1, 1)
prior_alpha, prior_beta = 1, 1

# 2. Posterior parameters
alpha_post_a = None  # TAREFA DO ALUNO: prior_alpha + conv_a
beta_post_a = None   # TAREFA DO ALUNO: prior_beta + (trials_a - conv_a)
alpha_post_b = None  # TAREFA DO ALUNO
beta_post_b = None   # TAREFA DO ALUNO

# 3. Monte Carlo: sample 50000 from each posterior
n_mc = 50000
# samples_a = None  # TAREFA DO ALUNO: np.random.beta(...)
# samples_b = None  # TAREFA DO ALUNO
# prob_b_better = None  # TAREFA DO ALUNO: (samples_b > samples_a).mean()

# 4. Lift
# lift = None  # TAREFA DO ALUNO: (samples_b / samples_a - 1) * 100

print(f"P(B > A): {prob_b_better}")
print(f"Lift medio: {lift.mean():.2f}%")
"""

SOLUTION_BAYES_1_5 = """# SOLUCAO - Exercicio 2 (A/B Test Bayesiano)
conv_a, trials_a = 1200, 15000
conv_b, trials_b = 1350, 15000

# 1. Prior: Beta(1, 1) (uniforme)
prior_alpha, prior_beta = 1, 1

# 2. Posterior parameters
alpha_post_a = prior_alpha + conv_a
beta_post_a  = prior_beta  + (trials_a - conv_a)
alpha_post_b = prior_alpha + conv_b
beta_post_b  = prior_beta  + (trials_b - conv_b)

# 3. Monte Carlo
np.random.seed(42)
n_mc = 50000
samples_a = np.random.beta(alpha_post_a, beta_post_a, n_mc)
samples_b = np.random.beta(alpha_post_b, beta_post_b, n_mc)
prob_b_better = float((samples_b > samples_a).mean())

# 4. Lift
lift = (samples_b / samples_a - 1) * 100

print(f"P(B > A): {prob_b_better:.4f}")
print(f"Lift medio: {lift.mean():.2f}%")
"""


PATCHES = [
    # (notebook_relative_path, finder_substring_to_locate_cell, original_exercise_src, solution_src)
    (
        "notebooks/00-matematica/0_3_algebra_linear_matrizes.ipynb",
        "Implemente SVD truncado",
        EXERCISE_SVD_0_3,
        SOLUTION_SVD_0_3,
    ),
    (
        "notebooks/02-data-science/2_1_python_data_science.ipynb",
        "Exercicio 1 - NumPy vs Loop",
        EXERCISE_NORM_2_1,
        SOLUTION_NORM_2_1,
    ),
    (
        "notebooks/02-data-science/2_1_python_data_science.ipynb",
        "Exercicio 2 - Limpeza de Dados",
        EXERCISE_CLEAN_2_1,
        SOLUTION_CLEAN_2_1,
    ),
    (
        "notebooks/01-estatistica/1_5_design_experimentos.ipynb",
        "Exercicio 2 - A/B Test Bayesiano",
        EXERCISE_BAYES_1_5,
        SOLUTION_BAYES_1_5,
    ),
]


def patch_one(nb_rel: str, needle: str, exercise_src: str, solution_src: str) -> str:
    path = ROOT / nb_rel
    nb = nbformat.read(path, as_version=4)
    target_idx = None
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        src = cell.source if isinstance(cell.source, str) else "".join(cell.source)
        if needle in src:
            target_idx = i
            break

    if target_idx is None:
        return "needle-not-found"

    # Restore the exercise scaffold (preserve tag list, ensure 'exercise' is present)
    cell = nb.cells[target_idx]
    cell.source = exercise_src
    tags = list((cell.metadata or {}).get("tags") or [])
    if "exercise" not in tags:
        tags.append("exercise")
    # Strip 'solution' if it was wrongly merged onto this scaffold
    tags = [t for t in tags if t != "solution"]
    cell.metadata["tags"] = tags
    cell.outputs = []
    cell.execution_count = None

    # Check if next cell is already the solution we're about to insert
    next_idx = target_idx + 1
    if next_idx < len(nb.cells):
        nxt = nb.cells[next_idx]
        if nxt.cell_type == "code":
            nxt_src = nxt.source if isinstance(nxt.source, str) else "".join(nxt.source)
            nxt_tags = (nxt.metadata or {}).get("tags") or []
            if "solution" in nxt_tags and nxt_src.strip() == solution_src.strip():
                return "already-has-solution"
            if "solution" in nxt_tags:
                # Update existing solution cell rather than insert a duplicate
                nxt.source = solution_src
                nxt.outputs = []
                nxt.execution_count = None
                nbformat.write(nb, path)
                return "updated-existing-solution"

    # Insert new solution cell
    new_cell = nbformat.v4.new_code_cell(source=solution_src)
    new_cell.metadata = {"tags": ["solution"]}
    nb.cells.insert(next_idx, new_cell)
    nbformat.write(nb, path)
    return "inserted"


def main() -> int:
    for nb_rel, needle, ex_src, sol_src in PATCHES:
        status = patch_one(nb_rel, needle, ex_src, sol_src)
        print(f"{status:30s}  {nb_rel}  ({needle[:40]!r})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
