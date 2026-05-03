# Índice - Currículo Educacional ML: Módulos 0.3, 0.4, 0.5

## Módulo 0.3: Álgebra Linear II - Matrizes

**Arquivo**: `0_3_algebra_linear_matrizes.ipynb`

**Metadados**:
- Células: 36 (18 markdown + 18 code)
- Tempo: 12-14 horas
- Pré-requisitos: Álgebra Linear I (0.2)
- Próximo: Cálculo I (0.4)

**Conteúdo**:
```
1. Introdução: Y = X @ W em ML
2. Tipos de Matrizes (6 tipos)
3. Operações Básicas (3 operações)
4. Multiplicação de Matrizes (forward pass)
5. Transformações Lineares 2D (6 visualizações)
6. Sistemas de Equações (2 métodos)
7. Determinante (interpretação)
8. Rank de Matriz (dimensionalidade)
9. Inversa e Pseudo-inversa (soluções)
10. Autovalores e Autovetores (Av=λv)
11. PCA do Zero (algoritmo completo)
12. SVD (A = U·Σ·V^T)
13. Compressão de Imagem (rank-k)
14. Sistemas de Recomendação (matrix factorization)
15. Matrizes em ML (5 aplicações)
16. Exercícios Práticos (3 problemas)
```

**Destaques**:
- Transformações geométricas com visualização
- PCA implementado sem sklearn
- SVD com compressão real
- Sistema de recomendação funcional

---

## Módulo 0.4: Cálculo I - Derivadas

**Arquivo**: `0_4_calculo_derivadas.ipynb`

**Metadados**:
- Células: 34 (17 markdown + 17 code)
- Tempo: 10-12 horas
- Pré-requisitos: Álgebra Linear (0.1, 0.2)
- Próximo: Cálculo II (0.5)

**Conteúdo**:
```
1. Introdução: taxa de mudança
2. Limites e Continuidade
3. Derivada: Definição Formal
4. Derivadas Básicas (tabela)
5. Regras de Diferenciação
6. Regra da Cadeia (backprop)
7. Derivadas Numéricas
8. Ativações e Derivadas (3 ativações)
9. Máximos e Mínimos
10. Derivadas Parciais (2D/3D)
11. Gradiente ∇f
12. Gradient Descent (algoritmo)
13. Jacobiano e Hessiano
14. Backpropagation (rede 2 camadas)
15. Exercícios Práticos (3 problemas)
```

**Destaques**:
- Gradient descent com visualização
- Backprop manual implementado
- Todas as ativações com derivadas
- Gradient checking para validação

---

## Módulo 0.5: Cálculo II - Integrais e Séries

**Arquivo**: `0_5_calculo_integrais_series.ipynb`

**Metadados**:
- Células: 32 (16 markdown + 16 code)
- Tempo: 8-10 horas
- Pré-requisitos: Cálculo I (0.4)
- Próximo: Probabilidade (0.6)

**Conteúdo**:
```
1. Introdução: área sob curva
2. Integral Definida
3. Teorema Fundamental do Cálculo
4. Integrais Básicas (tabela)
5. Técnicas de Integração (2 técnicas)
6. Integrais Múltiplas
7. Séries Numéricas
8. Série de Taylor
9. Integrais em Probabilidade
10. Distribuição Normal
11. Métodos Numéricos (4 métodos)
12. AUC-ROC (integração)
13. Integração Monte Carlo
14. Exercícios Práticos (3 problemas)
```

**Destaques**:
- 4 métodos numéricos comparados
- AUC-ROC calculado por integração
- Monte Carlo para estimar π
- Taylor com convergência visualizada

---

## Estatísticas Globais

| Métrica | Valor |
|---------|-------|
| Total Notebooks | 3 |
| Total Células | 102 |
| Markdown | 51 |
| Code | 51 |
| Horas Totais | 30-36h |
| Exercícios | 9 |
| Tamanho | 77 KB |
| Visualizações | ~80+ gráficos |

---

## Tecnologias

**Núcleo**:
- NumPy (operações matriciais)
- SciPy (álgebra linear, integração)
- Matplotlib (visualizações)
- SymPy (simbólico)

**ML**:
- Scikit-learn (datasets, modelos)

---

## Fluxo Recomendado

```
0.3 → 0.4 → 0.5
  ↓      ↓      ↓
Mat   Der    Int
       ↓
    0.6 Probabilidade
       ↓
    1.0 Regressão
       ↓
    2.0 Classificação
       ↓
    3.0 Redes Neurais
```

---

## Como Usar

### Abrir um notebook:
```bash
jupyter notebook 0_3_algebra_linear_matrizes.ipynb
jupyter notebook 0_4_calculo_derivadas.ipynb
jupyter notebook 0_5_calculo_integrais_series.ipynb
```

### Executar todos:
```bash
jupyter nbconvert --to notebook --execute 0_3_*.ipynb
jupyter nbconvert --to notebook --execute 0_4_*.ipynb
jupyter nbconvert --to notebook --execute 0_5_*.ipynb
```

### Verificar estrutura:
```python
import json
with open("0_3_algebra_linear_matrizes.ipynb") as f:
    nb = json.load(f)
    print(f"Células: {len(nb['cells'])}")
```

---

## Checklist de Conteúdo

### Notebook 0.3 (Matrizes)
- [x] 36 células
- [x] Tipos de matrizes
- [x] Operações básicas
- [x] Multiplicação A@B
- [x] Transformações lineares 2D
- [x] Sistemas Ax=b
- [x] Determinante
- [x] Rank
- [x] Inversa/pseudo-inversa
- [x] Autovalores/autovetores
- [x] PCA do zero
- [x] SVD
- [x] Compressão imagem
- [x] Recomendação
- [x] ML aplicações
- [x] 3 exercícios

### Notebook 0.4 (Derivadas)
- [x] 34 células
- [x] Limites
- [x] Definição formal
- [x] Derivadas básicas
- [x] Regras
- [x] Regra da cadeia
- [x] Numérico
- [x] Ativações
- [x] Max/min
- [x] Parciais
- [x] Gradiente
- [x] Gradient descent
- [x] Jacobiano/Hessiano
- [x] Backpropagation
- [x] 3 exercícios

### Notebook 0.5 (Integrais)
- [x] 32 células
- [x] Integral definida
- [x] Teorema fundamental
- [x] Integrais básicas
- [x] Técnicas
- [x] Múltiplas
- [x] Séries
- [x] Taylor
- [x] Probabilidade
- [x] Normal
- [x] Métodos numéricos
- [x] AUC-ROC
- [x] Monte Carlo
- [x] 3 exercícios

---

## Informações

- **Criado**: 2026-03-08
- **Localização**: `/sessions/kind-ecstatic-archimedes/mnt/notebooks-math&statistics/`
- **Formato**: Jupyter Notebook JSON
- **Kernel**: Python 3.10+
- **Status**: Completo e Validado ✅

---

**Última atualização**: 2026-03-08
