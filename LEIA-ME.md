# 3 Notebooks Educacionais de ML em Português (pt-BR)

## Criados com Sucesso! ✅

### Arquivos Gerados

1. **`0_6_probabilidade_fundamentos.ipynb`** (38 células)
   - Título: Probabilidade I: Fundamentos para ML
   - Tempo: 10-12 horas
   - Pré-requisitos: 0.1, 0.5
   - Próximo: 0.7

2. **`0_7_probabilidade_avancada.ipynb`** (32 células)
   - Título: Probabilidade II: Tópicos Avançados para ML
   - Tempo: 10-12 horas
   - Pré-requisitos: 0.3, 0.6
   - Próximo: 0.8

3. **`0_8_otimizacao_ml.ipynb`** (32 células)
   - Título: Otimização para Machine Learning
   - Tempo: 12-14 horas
   - Pré-requisitos: 0.3, 0.4
   - Próximo: 1.1 (Estatística)

---

## 📋 Características Principais

### Markdown em Português (pt-BR)
✅ Todos os textos explicativos, títulos, índices estão em português\
✅ Nomes de seções, conceitos em português\
✅ Exemplos contextualizados para audiência brasileira

### Código Python
✅ Variáveis em inglês (boas práticas)\
✅ Comentários em inglês\
✅ Sem docstrings (aspas triplas) - apenas comentários #\
✅ Uso do helper: `md()`, `code()`, `save_nb()`

### Conteúdo Educacional
✅ 35-45 células por notebook\
✅ Aplicações reais de ML\
✅ Visualizações ricas com matplotlib\
✅ Exercícios no final de cada notebook

---

## 📊 Conteúdo por Notebook

### Notebook 1: Probabilidade I - Fundamentos (38 células)

**Seções:**
1. Introdução: Probabilidade como linguagem da incerteza
2. Espaço amostral, eventos, axiomas de Kolmogorov
3. Regras de probabilidade (União, complemento)
4. Probabilidade condicional (spam vs não-spam)
5. Regra de Bayes (diagnóstico médico)
6. Independência de eventos (Naive Bayes)
7. Variáveis aleatórias discretas
8. Distribuição Bernoulli
9. Distribuição Binomial
10. Distribuição Poisson
11. Variáveis aleatórias contínuas
12. Distribuição Normal (68-95-99.7)
13. Distribuição Exponencial
14. Esperança e Variância
15. Lei dos Grandes Números
16. Exercícios: Diagnóstico, Simulação, Estimação

**Aplicações ML:**
- Naive Bayes
- Bayesian Neural Networks
- VAE (Variational Autoencoders)

---

### Notebook 2: Probabilidade II - Avançada (32 células)

**Seções:**
1. Distribuições conjuntas e marginais
2. Covariância e correlação de Pearson
3. Correlação ≠ Causalidade (confundidores)
4. Distribuições condicionais
5. Lei dos Grandes Números (prova intuitiva)
6. Teorema Central do Limite (surpreendente!)
7. Estimação de parâmetros
8. Máxima Verossimilhança (MLE)
9. Conexão MLE ↔ Cross-Entropy
10. Inferência Bayesiana (Prior × Likelihood = Posterior)
11. Regularização como Prior Gaussiano
12. Distribuição Normal Multivariada
13. Mistura de Gaussianas (GMM)
14. Exercícios integradores

**Aplicações ML:**
- PCA, ICA
- GMM (Clustering)
- Modelos generativos

---

### Notebook 3: Otimização para ML (32 células)

**Seções:**
1. ML como problema de otimização
2. Funções de custo comuns (MSE, MAE, Huber, Cross-Entropy)
3. Convexidade e otimalidade
4. Gradient Descent (GD)
5. Learning Rate (crítico!)
6. Batch GD vs SGD vs Mini-batch
7. SGD com Momentum
8. AdaGrad
9. RMSprop
10. Adam (padrão)
11. Regularização L2/L1
12. Vanishing/Exploding Gradients
13. Aplicação: Regressão Linear do zero
14. Aplicação: Regressão Logística do zero
15. Exercícios: Implementação, Comparação

**Otimizadores:**
- Gradient Descent
- SGD + Momentum
- AdaGrad
- RMSprop
- Adam

---

## 🔧 Requisitos

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, optimize
import seaborn as sns
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_classification
```

---

## 📖 Como Usar

1. **Baixe os notebooks:**
   ```bash
   # Estão em:
   /sessions/kind-ecstatic-archimedes/mnt/notebooks-math&statistics/
   ```

2. **Abra no Jupyter:**
   ```bash
   jupyter notebook 0_6_probabilidade_fundamentos.ipynb
   ```

3. **Siga o fluxo:**
   - Leia as seções markdown
   - Execute as células code sequencialmente
   - Faça os exercícios finais
   - Vá para o próximo notebook

---

## ✨ Características Especiais

### Notebook 1 (Probabilidade I)
- Axiomas fundamentais com verificação numérica
- Distribuições discretas vs contínuas
- Aplicação prática: teste COVID e diagnóstico médico
- Lei dos Grandes Números demonstrada empiricamente

### Notebook 2 (Probabilidade II)
- **Teorema Central do Limite:** Demonstração visual com 5 distribuições diferentes
- **Confundidores:** Porque correlação ≠ causalidade
- **Inferência Bayesiana:** Atualização de crenças em tempo real
- **MLE vs Cross-Entropy:** Conexão fundamental em ML

### Notebook 3 (Otimização)
- **Comparação de otimizadores:** GD, SGD, Momentum, Adam
- **Learning rate:** Efeito crítico (divergência vs convergência)
- **Do zero:** Regressão linear e logística implementadas do zero
- **Problemas reais:** Vanishing gradients em redes profundas

---

## 📈 Progressão de Dificuldade

```
Iniciante → Intermediário → Avançado
    ↓            ↓              ↓
 0.6        0.7           0.8
Fundamentos Avançado    Otimização
```

**Total estimado:** 32-38 horas de aprendizado

---

## 🎯 Objetivos de Aprendizado

### Ao terminar Notebook 1:
- [ ] Entender axiomas de probabilidade
- [ ] Diferenciar distribuições discretas e contínuas
- [ ] Aplicar regra de Bayes em problemas reais
- [ ] Conhecer distribuições importantes (Normal, Poisson, etc)

### Ao terminar Notebook 2:
- [ ] Trabalhar com distribuições multivariadas
- [ ] Entender MLE e inferência Bayesiana
- [ ] Conhecer conexão com ML (Cross-Entropy, regularização)
- [ ] Aplicar TCL em análise de dados

### Ao terminar Notebook 3:
- [ ] Implementar otimizadores do zero
- [ ] Escolher learning rate adequado
- [ ] Debugar convergência
- [ ] Entender trade-offs (batch vs SGD)

---

## 📚 Referências Internas

- Variáveis aleatórias → Distribuições
- Distribuições → Estimação → Otimização
- MLE → Cross-Entropy → Gradient Descent

---

## ✅ Checklist de Criação

- [x] 3 notebooks criados
- [x] 32-38 células cada
- [x] Markdown em português (pt-BR)
- [x] Código Python em inglês
- [x] Sem docstrings (apenas # comentários)
- [x] Aplicações reais de ML
- [x] Visualizações com matplotlib
- [x] Exercícios finais
- [x] Usando helper: md(), code(), save_nb()
- [x] Salvo em `/sessions/kind-ecstatic-archimedes/mnt/notebooks-math&statistics/`

---

## 🔗 Estrutura de Arquivos

```
notebooks-math&statistics/
├── 0_6_probabilidade_fundamentos.ipynb      (38 células)
├── 0_7_probabilidade_avancada.ipynb         (32 células)
├── 0_8_otimizacao_ml.ipynb                  (32 células)
└── LEIA-ME.md (este arquivo)
```

---

**Criados em:** 2026-03-08\
**Formato:** Jupyter Notebook (.ipynb)\
**Linguagem:** Português (pt-BR) + Python 3.x\
**Status:** ✅ Completo e pronto para uso

Bom aprendizado! 🚀
