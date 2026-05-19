#!/usr/bin/env python3
"""One-shot patcher that rewrites broken setup/import cells.

Each entry describes a notebook + a predicate to locate the cell to replace +
the new source. We use substring matches against the original cell source so
the patcher is idempotent (running twice does nothing).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]
NB_ROOT = ROOT / "notebooks"


# ---------- New setup/import bodies ----------

SCIPY_STATS_1_2 = """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm, t as t_dist, ttest_ind, chi2_contingency
t_ppf = t_dist.ppf
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-darkgrid')

# Simulacao: populacao vs amostra
np.random.seed(42)

# Populacao: altura em uma cidade (distribuicao normal)
population = np.random.normal(loc=170, scale=10, size=100000)
print(f'POPULACAO: mu = {population.mean():.2f} cm, sigma = {population.std():.2f} cm')

# Tomamos varias amostras
num_samples = 100
sample_size = 30
sample_means = []

for i in range(num_samples):
    sample = np.random.choice(population, size=sample_size, replace=False)
    sample_means.append(sample.mean())

sample_means = np.array(sample_means)
print(f'\\nMEDIA das medias amostrais: {sample_means.mean():.2f} cm')
print(f'DESVIO PADRAO das medias amostrais (EP teorico): {sample_means.std():.2f} cm')
print(f'EP teorico (sigma/sqrt(n)): {population.std()/np.sqrt(sample_size):.2f} cm')
"""

SCIPY_STATS_1_3 = """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import binom, norm, beta
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-darkgrid')

print('=== FREQUENTISTA vs BAYESIANO ===')
print('\\nFREQUENTISTA:')
print('  - Parametros sao fixos (desconhecidos, mas constantes)')
print('  - Dados sao aleatorios')
print('  - Probabilidade = frequencia em infinitas repeticoes')
print('  - Intervalo de confianca: se repetissemos 100 vezes, 95 conteriam o parametro')

print('\\nBAYESIANO:')
print('  - Parametros tem distribuicao de probabilidade (incerteza)')
print('  - Dados sao fixos (observados)')
print('  - Probabilidade = grau de crenca')
print('  - Intervalo de credibilidade: 95% de probabilidade do parametro estar nele')
"""

SKLEARN_REG_1_4 = """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-darkgrid')

print('=== REGRESSAO LINEAR ===')
print('\\nModelo: y = beta_0 + beta_1*x_1 + beta_2*x_2 + ... + beta_p*x_p + eps')
print('Objetivo: Minimizar Sum((y_i - y_hat_i)^2) (soma de erros ao quadrado)')
print('Solucao fechada: beta = (X^T X)^-1 X^T y')
"""

STATS_1_5 = """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm, t
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.power import tt_ind_solve_power
import warnings
warnings.filterwarnings('ignore')
plt.style.use('seaborn-v0_8-darkgrid')

print('=== DESIGN DE EXPERIMENTOS ===')
print('\\nPrincipios:')
print('  1. Randomizacao: evita vies de selecao')
print('  2. Replicacao: reduz variancia')
print('  3. Controle: mede efeito de uma variavel isolada')
print('  4. Bloqueamento: controla variaveis de confusao')
"""

# Module 03: replace the heavy from-scratch implementations with real sklearn.
SKLEARN_FULL_SETUP = """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')

from itertools import product
from copy import deepcopy

# Datasets
from sklearn.datasets import (
    load_iris, load_breast_cancer, load_diabetes, load_digits,
    fetch_california_housing, make_blobs, make_classification,
    make_regression, make_moons, make_circles,
)

# Pre-processing
from sklearn.preprocessing import (
    StandardScaler, MinMaxScaler, RobustScaler,
    LabelEncoder, OneHotEncoder, PolynomialFeatures,
)

# Model selection
from sklearn.model_selection import (
    train_test_split, cross_val_score, cross_validate,
    GridSearchCV, RandomizedSearchCV, KFold, StratifiedKFold,
    learning_curve, validation_curve,
)

# Linear models
from sklearn.linear_model import (
    LogisticRegression, LinearRegression, Ridge, Lasso, ElasticNet,
)

# Trees and ensembles
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestClassifier, RandomForestRegressor,
    GradientBoostingClassifier, GradientBoostingRegressor,
    BaggingClassifier, BaggingRegressor,
    AdaBoostClassifier, AdaBoostRegressor,
    VotingClassifier, StackingClassifier,
)

# Other classifiers
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.svm import SVC, SVR, LinearSVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis

# Clustering
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture

# Dimensionality reduction
from sklearn.decomposition import PCA, KernelPCA, TruncatedSVD, NMF
from sklearn.manifold import TSNE, Isomap

# Metrics
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix, roc_auc_score, roc_curve,
    mean_squared_error, mean_absolute_error, r2_score,
    silhouette_score, calinski_harabasz_score, davies_bouldin_score,
)

# Pipeline
from sklearn.pipeline import Pipeline, make_pipeline

print('Setup OK - sklearn:', __import__('sklearn').__version__)
"""

# Module 04 cell 3 just needs pandas added on top of existing content.
DL_4_2_PD_PATCH = """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
np.random.seed(42)

def make_blobs(n_samples=100, centers=2, n_features=2, random_state=None):
    if random_state is not None:
        np.random.seed(random_state)
    X = np.random.randn(n_samples, n_features)
    y = np.zeros(n_samples, dtype=int)
    center_size = n_samples // centers
    for c in range(centers):
        start = c * center_size
        end = start + center_size if c < centers - 1 else n_samples
        offset = np.random.randn(n_features) * 2
        X[start:end] += offset
        y[start:end] = c
    return X, y
"""

# 4_2 cell 14 needs pd; the cell itself uses pd.DataFrame for a comparison table.
# We patch the SETUP cell to import pandas (above). No need to touch cell 14.

# ---------- Patch instructions ----------

PATCHES = [
    # (notebook_relative_path, finder_substring, new_source)

    # 01-estatistica
    (
        "01-estatistica/1_2_estatistica_inferencial.ipynb",
        "# norm, t as t_dist",
        SCIPY_STATS_1_2,
    ),
    (
        "01-estatistica/1_3_estatistica_bayesiana.ipynb",
        "# binom, norm, beta",
        SCIPY_STATS_1_3,
    ),
    (
        "01-estatistica/1_4_regressao_estatistica.ipynb",
        "##linear_model import LinearRegression",
        SKLEARN_REG_1_4,
    ),
    (
        "01-estatistica/1_5_design_experimentos.ipynb",
        "# norm, t\n",
        STATS_1_5,
    ),

    # 03-machine-learning: replace the bulky from-scratch setup
    (
        "03-machine-learning/3_1_classificacao_completa.ipynb",
        "# ===== CLASSIFICATION MODELS =====",
        SKLEARN_FULL_SETUP,
    ),
    (
        "03-machine-learning/3_2_regressao_modelos.ipynb",
        "# ===== CLASSIFICATION MODELS =====",
        SKLEARN_FULL_SETUP,
    ),
    (
        "03-machine-learning/3_3_arvores_ensemble.ipynb",
        "# ===== CLASSIFICATION MODELS =====",
        SKLEARN_FULL_SETUP,
    ),
    (
        "03-machine-learning/3_4_svm_kernel.ipynb",
        "# ===== CLASSIFICATION MODELS =====",
        SKLEARN_FULL_SETUP,
    ),
    (
        "03-machine-learning/3_5_clustering.ipynb",
        "# ===== CLASSIFICATION MODELS =====",
        SKLEARN_FULL_SETUP,
    ),
    (
        "03-machine-learning/3_6_reducao_dimensionalidade.ipynb",
        "# ===== CLASSIFICATION MODELS =====",
        SKLEARN_FULL_SETUP,
    ),

    # 04-deep-learning
    (
        "04-deep-learning/4_2_arquiteturas_deep.ipynb",
        "def make_blobs(n_samples=100, centers=2",
        DL_4_2_PD_PATCH,
    ),
]


def patch_one(nb_rel: str, needle: str, new_src: str) -> str:
    path = NB_ROOT / nb_rel
    nb = nbformat.read(path, as_version=4)
    modified = False
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        src = cell.source
        if isinstance(src, list):
            src = "".join(src)
        if needle in src and src.strip() != new_src.strip():
            # Refuse to overwrite a restored exercise scaffold. The
            # exercise/solution contract is owned by restore_exercises.py;
            # rewriting an `exercise`-tagged cell here would re-collapse
            # scaffold + solution into the same cell.
            tags = (cell.metadata or {}).get("tags") or []
            if "exercise" in tags and "solution" not in tags:
                return "skipped-exercise-scaffold"
            cell.source = new_src
            cell.outputs = []
            cell.execution_count = None
            modified = True
            break
    if modified:
        nbformat.write(nb, path)
        return "patched"
    return "no-match-or-already-patched"


def main() -> int:
    for nb_rel, needle, new_src in PATCHES:
        status = patch_one(nb_rel, needle, new_src)
        print(f"{status:30s}  {nb_rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
