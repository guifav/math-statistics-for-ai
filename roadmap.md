# 📚 Roadmap Completo: Notebooks Educacionais de Machine Learning

> **Versão:** 3.0  
> **Total de Notebooks:** 53  
> **Tempo Total Estimado:** ~530 horas (estudo + prática)  
> **Última Atualização:** Janeiro 2025

---

## Visão Geral do Roadmap

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                    │
│   NÍVEL 0         NÍVEL 1        NÍVEL 2       NÍVEL 3       NÍVEL 4         NÍVEL 5    NÍVEL 6   │
│   MATEMÁTICA      ESTATÍSTICA    FUNDAMENTOS   CORE ML       DEEP LEARNING   DOMÍNIOS   PRODTIC   │
│   ──────────      ───────────    ───────────   ───────       ─────────────   ────────   ──────    │
│   8 notebooks     5 notebooks    4 notebooks   6 notebooks   6 notebooks     16 noteb.  4 noteb.  │
│   ~80 horas       ~50 horas      ~35 horas     ~55 horas     ~70 horas       ~190 horas ~50 horas │
│                                                                                                    │
│   [Pré-Cálculo]   [Descrittic.]  [Python DS]   [Classif.]    [Fund. NN]      [CV x5]    [Deploy]  │
│   [Álg.Lin. I]    [Infertic.]    [EDA]         [Regressão]   [Arquitet.]     [NLP x6]   [MLflow]  │
│   [Álg.Lin. II]   [Bayesiana]    [SQL/APIs]    [Árvores]     [Training]      [GenAI x5] [Drift]   │
│   [Cálc. I]       [Regressão]    [Acesso BD]   [SVM]         [Transfer]      [TS x4]    [Pipeline]│
│   [Cálc. II]      [Experim.]                   [Clustering]  [Aceler.]                            │
│   [Prob. I]                                    [Dim.Reduc.]  [Aceler.]                            │
│   [Prob. II]                                                                                       │
│   [Otimtic.]                                                                                       │
│                                                                                                    │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔢 NÍVEL 0: MATEMÁTICA APLICADA AO MACHINE LEARNING

> **Objetivo:** Construir base matemática sólida para compreensão profunda dos algoritmos.  
> **Notebooks:** 8 | **Tempo:** ~80 horas

---

### 0.1 Pré-Cálculo e Funções para ML

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `0_1_pre_calculo_funcoes_ml.ipynb` |
| **Tempo Estimado** | 6-8 horas |
| **Pré-requisitos** | Matemática básica (ensino médio) |

#### 📋 Conteúdo Detalhado

```
1. Introdução: Matemática como Linguagem do ML
2. Revisão de Álgebra Básica
3. Funções: Conceitos Fundamentais
4. Funções Lineares
   └── Aplicação: Regressão Linear
5. Funções Quadráticas e Polinomiais
   └── Aplicação: Features Polinomiais
6. Funções Exponenciais
   └── Aplicações: Softmax, Decaimento exponencial
7. Funções Logarítmicas
   └── Aplicações: Cross-Entropy, Entropia
8. Função Sigmoid e Ativações
   └── Aplicações: Logistic Regression, Redes Neurais
9. Somatórios e Produtórios
   └── Aplicações: Funções de custo, Verossimilhança
10. Exercícios Práticos
```

---

### 0.2 Álgebra Linear I: Vetores e Operações

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `0_2_algebra_linear_vetores.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebook 0.1 |

#### 📋 Conteúdo Detalhado

```
1. Vetores em Machine Learning
2. Vetores: Definição e Representação
3. Operações Básicas com Vetores
4. Produto Interno (Dot Product)
   └── Aplicações: Similaridade, Neurônios
5. Norma de Vetores (L1, L2, Lp)
   └── Aplicações: Regularização, Distâncias
6. Distância entre Vetores
   └── Aplicações: KNN, K-Means
7. Ângulos e Similaridade de Cosseno
   └── Aplicações: NLP, Recomendação
8. Vetores Unitários e Normalização
9. Espaços Vetoriais (Conceitos)
10. Projeção de Vetores
    └── Aplicação: PCA (intuição)
11. Exercícios Práticos
```

---

### 0.3 Álgebra Linear II: Matrizes e Transformações

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `0_3_algebra_linear_matrizes.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Notebook 0.2 |

#### 📋 Conteúdo Detalhado

```
1. Matrizes: Definição e Tipos Especiais
2. Operações com Matrizes
3. Matrizes como Transformações Lineares
   └── Visualização: Rotação, Escala, Cisalhamento
4. Sistemas de Equações Lineares
5. Matriz Inversa e Pseudo-inversa
   └── Aplicação: Solução fechada de regressão
6. Determinante e Rank
7. Autovalores e Autovetores
   └── Aplicação: PCA
8. Decomposição em Autovalores
9. Decomposição em Valores Singulares (SVD)
   └── Aplicações: Compressão, PCA, Recomendação
10. Matrizes em ML (covariância, kernel, pesos)
11. Exercícios Práticos
```

---

### 0.4 Cálculo I: Derivadas e Diferenciação

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `0_4_calculo_derivadas.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebooks 0.1, 0.2 |

#### 📋 Conteúdo Detalhado

```
1. Derivadas em Machine Learning
2. Limite e Continuidade (Revisão)
3. Derivada: Definição e Interpretação
4. Derivadas de Funções Básicas
5. Regras de Derivação
   └── Regra da Cadeia (CRUCIAL para Backprop)
6. Derivadas Importantes para ML
   └── Sigmoid, Tanh, ReLU, Softmax
7. Derivadas Numéricas (Gradient Checking)
8. Máximos e Mínimos
9. Derivadas Parciais
10. Vetor Gradiente
    └── Aplicação: Gradient Descent
11. Jacobiano e Hessiano (Introdução)
12. Exercícios Práticos
```

---

### 0.5 Cálculo II: Integrais e Séries

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `0_5_calculo_integrais_series.ipynb` |
| **Tempo Estimado** | 8-10 horas |
| **Pré-requisitos** | Notebook 0.4 |

#### 📋 Conteúdo Detalhado

```
1. Integrais em ML
2. Integral Definida (Área sob a curva)
3. Teorema Fundamental do Cálculo
4. Integrais de Funções Básicas
5. Técnicas de Integração (Básico)
6. Integrais Múltiplas (Conceito)
7. Séries Numéricas
8. Série de Taylor
   └── Aplicações: Aproximações de ativações
9. Integrais em Probabilidade
   └── PDF, CDF, Esperança
10. Métodos Numéricos de Integração
11. Exercícios Práticos
```

---

### 0.6 Probabilidade I: Fundamentos

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `0_6_probabilidade_fundamentos.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebooks 0.1, 0.5 |

#### 📋 Conteúdo Detalhado

```
1. Probabilidade em ML
2. Conceitos Fundamentais (Espaço amostral, Eventos)
3. Regras de Probabilidade
4. Probabilidade Condicional
5. Teorema de Bayes
   └── Aplicações: Naive Bayes, Spam Filter
6. Variáveis Aleatórias Discretas
7. Distribuições Discretas (Bernoulli, Binomial, Poisson)
8. Variáveis Aleatórias Contínuas
9. Distribuições Contínuas (Uniforme, Normal, Exponencial)
10. Esperança e Variância
11. Exercícios Práticos
```

---

### 0.7 Probabilidade II: Tópicos Avançados

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `0_7_probabilidade_avancada.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebooks 0.3, 0.6 |

#### 📋 Conteúdo Detalhado

```
1. Distribuições Conjuntas
2. Covariância e Correlação
3. Distribuições Condicionais
4. Lei dos Grandes Números
5. Teorema Central do Limite (TCL)
6. Estimação de Parâmetros
7. Máxima Verossimilhança (MLE)
   └── Conexão com funções de perda
8. Inferência Bayesiana (Introdução)
   └── Regularização como prior
9. Distribuição Normal Multivariada
   └── Aplicações: GMM, Gaussian Processes
10. Teoria da Informação (Entropia, KL)
    └── Aplicação: Cross-entropy loss
11. Exercícios Práticos
```

---

### 0.8 Otimização para Machine Learning

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `0_8_otimizacao_ml.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Notebooks 0.3, 0.4 |

#### 📋 Conteúdo Detalhado

```
1. ML como Otimização
2. Funções de Custo Comuns (MSE, Cross-Entropy, Hinge)
3. Convexidade
4. Condições de Otimalidade
5. Gradient Descent: O Algoritmo Central
6. Variantes (Batch, SGD, Mini-batch)
7. Learning Rate Schedules
8. Otimizadores Adaptativos
   └── Momentum, AdaGrad, RMSprop, Adam, AdamW
9. Regularização como Otimização (L1, L2)
10. Problemas Comuns (Vanishing/Exploding gradients)
11. Aplicação: Regressão Linear com GD
12. Aplicação: Regressão Logística com GD
13. Exercícios Práticos
```

---

## 📊 NÍVEL 1: ESTATÍSTICA COMPLETA

> **Objetivo:** Dominar análise estatística para tomada de decisão baseada em dados.  
> **Notebooks:** 5 | **Tempo:** ~50 horas

---

### 1.1 Estatística Descritiva e Exploratória

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `1_1_estatistica_descritiva.ipynb` |
| **Tempo Estimado** | 8-10 horas |
| **Pré-requisitos** | Notebook 0.6 |
| **Datasets** | Tips, Titanic, Penguins, dados sintéticos |

#### 📋 Conteúdo Detalhado

```
1. Estatística no Contexto de Data Science
   ├── Estatística descritiva vs inferencial
   ├── População vs amostra
   └── Tipos de variáveis

2. Medidas de Tendência Central
   ├── Média (aritmética, ponderada, geométrica)
   ├── Mediana
   ├── Moda
   └── Quando usar cada uma

3. Medidas de Dispersão
   ├── Variância e desvio padrão
   ├── Range e IQR
   ├── Coeficiente de variação
   └── MAD (Median Absolute Deviation)

4. Medidas de Forma
   ├── Assimetria (Skewness)
   ├── Curtose (Kurtosis)
   └── Interpretação visual

5. Percentis e Quartis
   ├── Definição e cálculo
   ├── Boxplots
   └── Detecção de outliers (IQR, Z-score)

6. Visualização de Distribuições
   ├── Histogramas
   ├── KDE plots
   ├── Violin plots
   ├── QQ-plots
   └── Escolha de bins e bandwidth

7. Análise Bivariada
   ├── Scatter plots
   ├── Tabelas de contingência
   ├── Correlação (Pearson, Spearman, Kendall)
   └── Heatmaps de correlação

8. Análise Multivariada Exploratória
   ├── Pair plots
   ├── Correlações parciais
   └── Matriz de correlação

9. Resumos Estatísticos Automatizados
   ├── pandas describe()
   ├── pandas-profiling/ydata-profiling
   └── Interpretação crítica

10. Comunicação de Resultados
    ├── Tabelas de resumo
    ├── Visualizações efetivas
    └── Storytelling com dados

11. Exercícios Práticos
```

---

### 1.2 Estatística Inferencial e Testes de Hipótese

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `1_2_estatistica_inferencial.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Notebooks 0.6, 0.7, 1.1 |
| **Datasets** | Student Performance, A/B Testing data, dados sintéticos |

#### 📋 Conteúdo Detalhado

```
1. Fundamentos de Inferência
   ├── Da amostra para a população
   ├── Estimação pontual
   ├── Erro padrão
   └── Distribuição amostral

2. Intervalos de Confiança
   ├── IC para média (σ conhecido e desconhecido)
   ├── IC para proporção
   ├── IC para diferença de médias
   ├── Interpretação correta (erros comuns!)
   └── Tamanho de amostra necessário

3. Testes de Hipótese: Framework
   ├── Hipótese nula (H₀) e alternativa (H₁)
   ├── Erros tipo I e tipo II
   ├── Nível de significância (α)
   ├── p-valor: o que realmente significa
   ├── Poder estatístico (1 - β)
   └── Tamanho de efeito

4. Testes para Uma Amostra
   ├── Teste Z (σ conhecido)
   ├── Teste t (σ desconhecido)
   ├── Teste de proporção
   └── Implementação em scipy.stats

5. Testes para Duas Amostras
   ├── Teste t para amostras independentes
   ├── Teste t pareado
   ├── Teste de Welch (variâncias diferentes)
   ├── Teste Z para proporções
   └── Pressupostos e verificações

6. Testes Não-Paramétricos
   ├── Quando usar (violação de pressupostos)
   ├── Mann-Whitney U
   ├── Wilcoxon signed-rank
   ├── Kruskal-Wallis
   └── Comparação com paramétricos

7. ANOVA (Análise de Variância)
   ├── ANOVA de um fator
   ├── Pressupostos (normalidade, homogeneidade)
   ├── Testes post-hoc (Tukey, Bonferroni)
   ├── ANOVA de dois fatores
   └── ANOVA de medidas repetidas

8. Testes Qui-Quadrado
   ├── Teste de independência
   ├── Teste de aderência (goodness of fit)
   └── Tabelas de contingência

9. Correção para Múltiplas Comparações
   ├── Problema das comparações múltiplas
   ├── Correção de Bonferroni
   ├── Correção de Holm
   ├── FDR (Benjamini-Hochberg)
   └── Quando aplicar cada uma

10. Armadilhas e Boas Práticas
    ├── p-hacking
    ├── HARKing
    ├── Significância estatística vs prática
    ├── Intervalos de confiança > p-valores
    └── Replicabilidade

11. Exercícios Práticos
```

---

### 1.3 Estatística Bayesiana Aplicada

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `1_3_estatistica_bayesiana.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebooks 0.7, 1.2 |
| **Datasets** | A/B Testing, dados sintéticos, exemplos de negócio |

#### 📋 Conteúdo Detalhado

```
1. Filosofia Bayesiana vs Frequentista
   ├── Interpretação de probabilidade
   ├── Quando usar cada abordagem
   └── Vantagens do Bayesianismo

2. Teorema de Bayes Revisitado
   ├── Prior, Likelihood, Posterior
   ├── Atualização sequencial
   └── Exemplos intuitivos

3. Escolha de Priors
   ├── Priors informativos vs não-informativos
   ├── Priors conjugados
   │   ├── Beta-Binomial
   │   ├── Normal-Normal
   │   └── Gamma-Poisson
   ├── Priors fracamente informativos
   └── Análise de sensibilidade

4. Inferência Bayesiana para Proporções
   ├── Modelo Beta-Binomial
   ├── A/B Testing Bayesiano
   ├── Probabilidade de ser melhor
   └── Comparação com teste frequentista

5. Inferência Bayesiana para Médias
   ├── Modelo Normal
   ├── Prior conjugado
   └── Credible intervals vs Confidence intervals

6. Métodos Computacionais (Introdução)
   ├── Por que precisamos de MCMC
   ├── Metropolis-Hastings (conceito)
   ├── Gibbs sampling (conceito)
   └── Diagnósticos de convergência

7. PyMC3/PyMC Básico
   ├── Definição de modelos
   ├── Sampling
   ├── Visualização de posteriors
   └── Summarização de resultados

8. Aplicações Práticas
   ├── A/B Testing Bayesiano completo
   ├── Estimação de taxas de conversão
   ├── Forecasting simples
   └── Tomada de decisão sob incerteza

9. Comparação de Modelos
   ├── Bayes Factor
   ├── WAIC e LOO-CV
   └── Model averaging

10. Exercícios Práticos
```

---

### 1.4 Regressão Estatística (vs ML)

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `1_4_regressao_estatistica.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebooks 1.1, 1.2 |
| **Datasets** | Boston Housing, Auto MPG, dados socioeconômicos |

#### 📋 Conteúdo Detalhado

```
1. Regressão: Perspectiva Estatística vs ML
   ├── Foco em inferência vs predição
   ├── Interpretabilidade vs performance
   └── Quando usar cada abordagem

2. Regressão Linear Simples
   ├── Modelo: Y = β₀ + β₁X + ε
   ├── Estimação por OLS
   ├── Interpretação de coeficientes
   ├── R² e R² ajustado
   └── Inferência sobre β (testes t, IC)

3. Pressupostos da Regressão Linear
   ├── Linearidade
   ├── Independência dos erros
   ├── Homocedasticidade
   ├── Normalidade dos resíduos
   └── Ausência de multicolinearidade

4. Diagnósticos de Regressão
   ├── Análise de resíduos
   │   ├── Resíduos vs Fitted
   │   ├── QQ-plot
   │   ├── Scale-Location
   │   └── Resíduos vs Leverage
   ├── Detecção de outliers e pontos influentes
   │   ├── Cook's distance
   │   ├── Leverage (hat values)
   │   └── DFBETAS, DFFITS
   └── Testes formais (Breusch-Pagan, Durbin-Watson)

5. Regressão Linear Múltipla
   ├── Extensão para múltiplas variáveis
   ├── Interpretação de coeficientes (ceteris paribus)
   ├── Testes F para modelo global
   ├── Coeficientes parciais
   └── Comparação de modelos aninhados

6. Multicolinearidade
   ├── Detecção (VIF, correlação)
   ├── Consequências
   └── Tratamento

7. Variáveis Categóricas
   ├── Dummy variables
   ├── Categoria de referência
   ├── Interpretação
   └── Interações com numéricas

8. Interações e Termos Polinomiais
   ├── Interações entre variáveis
   ├── Termos quadráticos
   ├── Interpretação
   └── Quando incluir

9. Seleção de Variáveis (Perspectiva Estatística)
   ├── Forward selection
   ├── Backward elimination
   ├── Stepwise
   ├── Critérios (AIC, BIC, R² ajustado)
   └── Problemas e limitações

10. Regressão com statsmodels
    ├── OLS completo
    ├── Interpretação de output
    ├── Diagnósticos automatizados
    └── Comparação com sklearn

11. Extensões (Menção)
    ├── Regressão robusta
    ├── Regressão quantílica
    └── Modelos mistos

12. Exercícios Práticos
```

---

### 1.5 Design de Experimentos e A/B Testing

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `1_5_design_experimentos_ab_testing.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebooks 1.2, 1.3 |
| **Datasets** | Dados de A/B testing, simulações |

#### 📋 Conteúdo Detalhado

```
1. Fundamentos de Experimentação
   ├── Correlação vs causalidade
   ├── Variáveis de confusão
   ├── Randomização
   └── Grupos de controle

2. Design de Experimentos
   ├── Completely Randomized Design
   ├── Randomized Block Design
   ├── Factorial Design
   └── Latin Square (menção)

3. A/B Testing: Fundamentos
   ├── O que é e quando usar
   ├── Métricas de sucesso
   ├── Unit of randomization
   └── Duration e sample size

4. Cálculo de Tamanho de Amostra
   ├── Para diferença de médias
   ├── Para diferença de proporções
   ├── MDE (Minimum Detectable Effect)
   ├── Poder estatístico
   └── Ferramentas e calculadoras

5. Execução de Experimentos
   ├── Aleatorização correta
   ├── Grupos balanceados
   ├── Avoiding peeking (problema de parar cedo)
   └── Guardrail metrics

6. Análise de Resultados
   ├── Análise frequentista
   │   ├── Teste de proporções
   │   ├── Teste t
   │   └── Intervalos de confiança
   ├── Análise Bayesiana
   │   ├── Probabilidade de ser melhor
   │   ├── Expected loss
   │   └── Credible intervals
   └── Comparação de abordagens

7. A/B Testing Avançado
   ├── Testes A/B/n (múltiplas variantes)
   ├── Sequential testing
   ├── Multi-armed bandits
   │   ├── Epsilon-greedy
   │   ├── UCB
   │   └── Thompson sampling
   └── Contextual bandits (menção)

8. Segmentação de Resultados
   ├── Heterogeneidade de efeitos
   ├── Análise por segmentos
   └── Causal forests (menção)

9. Problemas Comuns
   ├── Network effects
   ├── Novelty effects
   ├── Selection bias
   ├── Simpson's paradox
   └── Multiple testing

10. Métricas de Negócio
    ├── Definição de métricas primárias e secundárias
    ├── Overall Evaluation Criterion (OEC)
    ├── Métricas de longo prazo
    └── Proxy metrics

11. Cultura de Experimentação
    ├── Documentação de experimentos
    ├── Plataformas de A/B testing
    └── Democratização de experimentos

12. Exercícios Práticos
```

---

## 💻 NÍVEL 2: FUNDAMENTOS DE PROGRAMAÇÃO E DADOS

> **Objetivo:** Dominar ferramentas práticas para manipulação de dados.  
> **Notebooks:** 4 | **Tempo:** ~35 horas

---

### 2.1 Python para Data Science

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `2_1_python_data_science.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Python básico, Nível 0 (recomendado) |
| **Datasets** | Tips, Titanic, Gapminder |

#### 📋 Conteúdo Detalhado

```
1. NumPy: Computação Numérica
   ├── Arrays vs Listas
   ├── Criação de arrays
   ├── Indexação e slicing
   ├── Broadcasting
   ├── Operações vetorizadas
   └── Random

2. Pandas: Manipulação de Dados
   ├── Series e DataFrames
   ├── Leitura/escrita de dados
   ├── Seleção (loc, iloc, query)
   ├── Dados faltantes
   ├── Transformações (apply, map)
   ├── Agregações (groupby, pivot_table)
   ├── Joins e merges
   └── Method chaining

3. Matplotlib: Visualização Base
   ├── Anatomia de figura
   ├── Gráficos básicos
   ├── Subplots
   ├── Customização
   └── Estilos

4. Seaborn: Visualização Estatística
   ├── Distribuições
   ├── Relações
   ├── Categóricos
   └── Heatmaps

5. Estudo de Caso: EDA Completa
6. Boas Práticas e Performance
7. Exercícios Práticos
```

---

### 2.2 Análise Exploratória de Dados (EDA) Profunda

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `2_2_eda_profunda.ipynb` |
| **Tempo Estimado** | 8-10 horas |
| **Pré-requisitos** | Notebooks 1.1, 2.1 |
| **Datasets** | Titanic, House Prices, múltiplos |

#### 📋 Conteúdo Detalhado

```
1. Framework de EDA
2. Análise de Qualidade de Dados
3. Análise Univariada
4. Análise Bivariada
5. Análise Multivariada
6. Ferramentas Automatizadas
7. Comunicação de Insights
8. Exercícios Práticos
```

---

### 2.3 SQL e Bancos de Dados para Data Science

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `2_3_sql_bancos_dados.ipynb` |
| **Tempo Estimado** | 8-10 horas |
| **Pré-requisitos** | Notebook 2.1 |
| **Datasets** | SQLite databases, exemplos de negócio |

#### 📋 Conteúdo Detalhado

```
1. SQL Fundamentals
   ├── SELECT, WHERE, ORDER BY
   ├── Funções de agregação
   ├── GROUP BY e HAVING
   └── DISTINCT

2. JOINs
   ├── INNER JOIN
   ├── LEFT/RIGHT JOIN
   ├── FULL OUTER JOIN
   ├── CROSS JOIN
   └── Self joins

3. Subqueries e CTEs
   ├── Subqueries no WHERE
   ├── Subqueries no FROM
   ├── CTEs (WITH clause)
   └── Recursive CTEs

4. Window Functions
   ├── ROW_NUMBER, RANK, DENSE_RANK
   ├── LAG, LEAD
   ├── Running totals
   └── Moving averages

5. SQL para Análise
   ├── Cohort analysis
   ├── Funnel analysis
   ├── Retention
   └── Métricas de negócio

6. Pandas + SQL
   ├── read_sql
   ├── to_sql
   └── SQLAlchemy

7. Conexão com Bancos
   ├── SQLite
   ├── PostgreSQL
   └── MySQL

8. Exercícios Práticos
```

---

### 2.4 APIs, Web Scraping e Coleta de Dados

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `2_4_apis_web_scraping.ipynb` |
| **Tempo Estimado** | 8-10 horas |
| **Pré-requisitos** | Notebook 2.1 |
| **Datasets** | APIs públicas, websites para scraping |

#### 📋 Conteúdo Detalhado

```
1. APIs REST
   ├── Conceitos (endpoints, HTTP methods)
   ├── requests library
   ├── Autenticação
   ├── Paginação
   └── Rate limiting

2. APIs Públicas Úteis
   ├── OpenWeather
   ├── Twitter/X
   ├── Yahoo Finance
   └── Outras

3. Web Scraping
   ├── Ética e legalidade
   ├── BeautifulSoup
   ├── Selenium (dinâmico)
   └── Tratamento de dados

4. Formatos de Dados
   ├── JSON
   ├── XML
   ├── Parquet
   └── Feather

5. Boas Práticas
   ├── Caching
   ├── Error handling
   └── Logging

6. Exercícios Práticos
```

---

## 🤖 NÍVEL 3: CORE MACHINE LEARNING

> **Objetivo:** Dominar algoritmos fundamentais de aprendizado supervisionado e não-supervisionado.  
> **Notebooks:** 6 | **Tempo:** ~55 horas

---

### 3.1 Classificação Completa ✅

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `3_1_classificacao_completa.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Status** | ✅ **CRIADO** |

---

### 3.2 Regressão Completa

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `3_2_regressao_completa.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebooks 0.8, 1.4, 2.1 |
| **Datasets** | California Housing, Ames Housing, Auto MPG |

#### 📋 Conteúdo Detalhado

```
1. Regressão: Perspectiva ML
2. Regressão Linear (sklearn)
3. Regularização: Ridge, Lasso, ElasticNet
4. Regressão Polinomial
5. Árvores de Regressão
6. Random Forest Regressor
7. Gradient Boosting Regressor
8. XGBoost Regressor
9. Métricas (MSE, RMSE, MAE, R², MAPE)
10. Cross-validation para Regressão
11. Análise de Resíduos (perspectiva ML)
12. Feature Importance
13. Estudo de Caso Completo
14. Exercícios Práticos
```

---

### 3.3 Algoritmos Baseados em Árvores

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `3_3_algoritmos_arvores.ipynb` |
| **Tempo Estimado** | 8-10 horas |
| **Pré-requisitos** | Notebooks 3.1 ou 3.2 |
| **Datasets** | Titanic, Adult Income, Wine Quality |

#### 📋 Conteúdo Detalhado

```
1. Decision Trees Fundamentos
2. Critérios de Split (Entropia, Gini, MSE)
3. Pruning
4. Ensemble Methods: Conceito
5. Random Forest
6. Gradient Boosting
7. XGBoost em Detalhes
8. LightGBM e CatBoost
9. Comparação de Algoritmos
10. Interpretabilidade de Árvores
11. Exercícios Práticos
```

---

### 3.4 Support Vector Machines (SVM)

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `3_4_svm.ipynb` |
| **Tempo Estimado** | 6-8 horas |
| **Pré-requisitos** | Notebooks 0.2, 3.1 |
| **Datasets** | Iris, Digits, Breast Cancer |

#### 📋 Conteúdo Detalhado

```
1. Intuição Geométrica
2. SVM Linear
3. Kernel Trick
4. Kernels (Linear, RBF, Poly)
5. SVM para Classificação
6. SVR para Regressão
7. Tuning (C, gamma)
8. Quando Usar SVM
9. Exercícios Práticos
```

---

### 3.5 Clustering Completo

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `3_5_clustering_completo.ipynb` |
| **Tempo Estimado** | 8-10 horas |
| **Pré-requisitos** | Notebooks 0.2, 0.6 |
| **Datasets** | Mall Customers, Wine, Digits |

#### 📋 Conteúdo Detalhado

```
1. Aprendizado Não-Supervisionado
2. K-Means
3. Clustering Hierárquico
4. DBSCAN
5. Gaussian Mixture Models
6. Métricas de Avaliação
7. Pré-processamento para Clustering
8. Estudo de Caso: Segmentação
9. Exercícios Práticos
```

---

### 3.6 Redução de Dimensionalidade

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `3_6_reducao_dimensionalidade.ipynb` |
| **Tempo Estimado** | 6-8 horas |
| **Pré-requisitos** | Notebooks 0.3, 3.5 |
| **Datasets** | MNIST, Digits, Faces, Wine |

#### 📋 Conteúdo Detalhado

```
1. Maldição da Dimensionalidade
2. PCA
3. t-SNE
4. UMAP
5. LDA
6. Aplicações
7. Estudo de Caso
8. Exercícios Práticos
```

---

## 🧠 NÍVEL 4: DEEP LEARNING FUNDAMENTOS

> **Objetivo:** Dominar fundamentos de redes neurais e técnicas de treinamento.  
> **Notebooks:** 6 | **Tempo:** ~70 horas

---

### 4.1 Fundamentos de Redes Neurais

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `4_1_fundamentos_redes_neurais.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Notebooks 0.4, 0.8, 3.1 |
| **Datasets** | MNIST, Fashion MNIST, dados sintéticos |

#### 📋 Conteúdo Detalhado

```
1. Do Perceptron ao MLP
   ├── Perceptron revisitado
   ├── Limitações (XOR problem)
   └── Multi-Layer Perceptron

2. Anatomia de uma Rede Neural
   ├── Camadas (input, hidden, output)
   ├── Neurônios e conexões
   ├── Pesos e biases
   └── Forward propagation

3. Funções de Ativação
   ├── Sigmoid
   ├── Tanh
   ├── ReLU e variantes (LeakyReLU, PReLU, ELU)
   ├── Softmax
   ├── GELU, SiLU/Swish
   └── Como escolher

4. Funções de Perda
   ├── MSE para regressão
   ├── Cross-Entropy para classificação
   ├── Binary vs Categorical
   └── Focal loss (menção)

5. Backpropagation
   ├── Regra da cadeia revisitada
   ├── Cálculo de gradientes
   ├── Computational graphs
   └── Implementação manual simplificada

6. Otimizadores em Deep Learning
   ├── SGD com momentum
   ├── Adam, AdamW
   ├── Learning rate schedulers
   └── Gradient clipping

7. PyTorch Básico
   ├── Tensores
   ├── Autograd
   ├── nn.Module
   ├── Definindo modelos
   └── DataLoaders

8. Construindo um MLP
   ├── Arquitetura
   ├── Training loop
   ├── Validation
   └── Inference

9. Debugging de Redes Neurais
   ├── Verificação de shapes
   ├── Gradient checking
   ├── Visualização de ativações
   └── Problemas comuns

10. Exercícios Práticos
```

---

### 4.2 Arquiteturas e Design de Redes

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `4_2_arquiteturas_redes.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebook 4.1 |
| **Datasets** | CIFAR-10, MNIST, Tabular data |

#### 📋 Conteúdo Detalhado

```
1. Princípios de Design de Redes
   ├── Profundidade vs largura
   ├── Número de parâmetros
   ├── Receptive field
   └── Inductive biases

2. Arquiteturas para Dados Tabulares
   ├── MLP design
   ├── Entity embeddings
   ├── Wide & Deep
   └── TabNet (menção)

3. Conexões Residuais (Skip Connections)
   ├── Problema do vanishing gradient
   ├── ResNet blocks
   ├── Highway networks
   └── DenseNet (menção)

4. Normalização
   ├── Batch Normalization
   │   ├── Funcionamento
   │   ├── Training vs inference
   │   └── Problemas
   ├── Layer Normalization
   ├── Instance Normalization
   ├── Group Normalization
   └── Quando usar cada uma

5. Inicialização de Pesos
   ├── Por que importa
   ├── Xavier/Glorot
   ├── He/Kaiming
   ├── Inicialização por camada
   └── Pré-treinamento

6. Arquiteturas de Encoder-Decoder
   ├── Conceito geral
   ├── Bottleneck
   ├── Aplicações
   └── Skip connections em encoders-decoders

7. Attention Mechanisms (Introdução)
   ├── Intuição
   ├── Self-attention básico
   └── Preparação para transformers

8. AutoML e NAS (Menção)
   ├── Neural Architecture Search
   ├── AutoML frameworks
   └── Trade-offs

9. Exercícios Práticos
```

---

### 4.3 Técnicas de Treinamento Avançadas

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `4_3_tecnicas_treinamento.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Notebooks 4.1, 4.2 |
| **Datasets** | CIFAR-10, dados sintéticos |

#### 📋 Conteúdo Detalhado

```
1. Regularização em Deep Learning
   ├── L1/L2 weight decay
   ├── Dropout
   │   ├── Standard dropout
   │   ├── Spatial dropout
   │   └── DropConnect
   ├── Data augmentation como regularização
   ├── Early stopping
   └── Label smoothing

2. Learning Rate Strategies
   ├── Learning rate finder
   ├── Step decay
   ├── Exponential decay
   ├── Cosine annealing
   ├── Warm restarts
   ├── Cyclical learning rates
   └── One-cycle policy

3. Batch Size e Training Dynamics
   ├── Efeito do batch size
   ├── Gradient accumulation
   ├── Large batch training
   └── Learning rate scaling

4. Data Augmentation
   ├── Augmentations clássicas
   ├── Cutout, Mixup, CutMix
   ├── AutoAugment
   └── Augmentação específica por domínio

5. Técnicas de Ensemble
   ├── Model averaging
   ├── Snapshot ensembles
   ├── Stochastic Weight Averaging (SWA)
   └── Test-time augmentation (TTA)

6. Curriculum Learning
   ├── Conceito
   ├── Implementação
   └── Aplicações

7. Knowledge Distillation
   ├── Teacher-student
   ├── Soft labels
   └── Aplicações

8. Mixed Precision Training
   ├── FP16 vs FP32
   ├── Loss scaling
   ├── PyTorch AMP
   └── Benefícios e cuidados

9. Checkpointing e Logging
   ├── Model checkpoints
   ├── TensorBoard
   ├── Weights & Biases
   └── MLflow para DL

10. Debugging de Treinamento
    ├── Loss curves analysis
    ├── Gradient flow
    ├── Activation statistics
    └── Overfitting diagnostics

11. Exercícios Práticos
```

---

### 4.4 Transfer Learning e Fine-tuning

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `4_4_transfer_learning.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebooks 4.1, 4.3 |
| **Datasets** | Custom datasets, Kaggle competitions |

#### 📋 Conteúdo Detalhado

```
1. Conceito de Transfer Learning
   ├── Por que funciona
   ├── Feature extraction vs fine-tuning
   └── Quando usar

2. Modelos Pré-treinados
   ├── ImageNet models
   ├── Hugging Face Hub
   ├── PyTorch Hub
   └── Timm library

3. Feature Extraction
   ├── Congelando camadas
   ├── Usando como feature extractor
   └── Treinando apenas classificador

4. Fine-tuning Completo
   ├── Descongelando camadas
   ├── Discriminative learning rates
   ├── Gradual unfreezing
   └── Fine-tuning strategies

5. Fine-tuning por Domínio
   ├── Visão: ImageNet → Custom
   ├── NLP: BERT → Custom
   ├── Domain adaptation
   └── Few-shot learning

6. Práticas de Fine-tuning
   ├── Learning rate selection
   ├── Regularização
   ├── Data augmentation
   └── Quando parar

7. Transfer Learning para Dados Pequenos
   ├── Estratégias
   ├── Augmentation pesada
   └── Progressive resizing

8. Exercícios Práticos
```

---

### 4.5 Aceleração e Deployment de Deep Learning

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `4_5_aceleracao_deployment_dl.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebooks 4.1-4.4 |
| **Datasets** | Modelos treinados anteriormente |

#### 📋 Conteúdo Detalhado

```
1. Otimização de Modelos
   ├── Pruning
   │   ├── Unstructured pruning
   │   ├── Structured pruning
   │   └── Lottery ticket hypothesis
   ├── Quantização
   │   ├── Post-training quantization
   │   ├── Quantization-aware training
   │   └── INT8 vs FP16
   └── Knowledge distillation (revisão)

2. Arquiteturas Eficientes
   ├── MobileNet
   ├── EfficientNet
   ├── ShuffleNet
   └── Design principles

3. Inferência Otimizada
   ├── ONNX
   ├── TensorRT
   ├── OpenVINO
   └── Core ML

4. GPU e Hardware
   ├── CUDA basics
   ├── Memory management
   ├── Multi-GPU training
   └── TPUs (menção)

5. Deployment
   ├── TorchScript
   ├── ONNX Runtime
   ├── FastAPI + PyTorch
   ├── Triton Inference Server
   └── Edge deployment

6. Profiling e Benchmarking
   ├── PyTorch profiler
   ├── Memory profiling
   ├── Latency vs throughput
   └── Bottleneck identification

7. Exercícios Práticos
```

---

### 4.6 Frameworks e Ecossistema Deep Learning

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `4_6_frameworks_ecossistema.ipynb` |
| **Tempo Estimado** | 6-8 horas |
| **Pré-requisitos** | Notebook 4.1 |
| **Datasets** | Diversos |

#### 📋 Conteúdo Detalhado

```
1. PyTorch Ecosystem
   ├── PyTorch Lightning
   ├── Hugging Face integration
   ├── Timm
   └── TorchMetrics

2. High-Level APIs
   ├── PyTorch Lightning
   ├── FastAI
   ├── Keras (TensorFlow)
   └── Comparação

3. Experiment Tracking
   ├── TensorBoard
   ├── Weights & Biases
   ├── MLflow
   └── Neptune

4. Distributed Training
   ├── DataParallel
   ├── DistributedDataParallel
   ├── Horovod
   └── DeepSpeed (menção)

5. Cloud ML Platforms
   ├── Google Colab Pro
   ├── AWS SageMaker
   ├── GCP Vertex AI
   └── Azure ML

6. Reprodutibilidade
   ├── Seeds
   ├── Deterministic algorithms
   ├── Configuration management
   └── Docker para DL

7. Exercícios Práticos
```

---

## 👁️ NÍVEL 5A: COMPUTER VISION

> **Objetivo:** Dominar técnicas de visão computacional com deep learning.  
> **Notebooks:** 5 | **Tempo:** ~60 horas

---

### 5A.1 CNNs: Fundamentos e Arquiteturas

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5A_1_cnn_fundamentos.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Notebook 4.1 |
| **Datasets** | MNIST, CIFAR-10, Fashion MNIST |

#### 📋 Conteúdo Detalhado

```
1. Por que CNNs para Imagens
   ├── Limitações de MLPs
   ├── Invariância translacional
   ├── Compartilhamento de parâmetros
   └── Hierarquia de features

2. Operação de Convolução
   ├── Kernel/filtro
   ├── Stride e padding
   ├── Receptive field
   ├── Cálculo de dimensões output
   └── Visualização de filtros

3. Pooling
   ├── Max pooling
   ├── Average pooling
   ├── Global pooling
   └── Strided convolution vs pooling

4. Arquiteturas Clássicas
   ├── LeNet-5
   ├── AlexNet
   ├── VGG (16, 19)
   ├── GoogLeNet/Inception
   └── Evolução e lições

5. ResNet e Skip Connections
   ├── Residual blocks
   ├── ResNet-18, 34, 50, 101, 152
   ├── Bottleneck blocks
   └── Pre-activation ResNet

6. Arquiteturas Modernas
   ├── DenseNet
   ├── EfficientNet
   ├── ConvNeXt
   └── Comparação

7. Implementação em PyTorch
   ├── nn.Conv2d
   ├── Construindo CNN do zero
   ├── Usando modelos pré-treinados
   └── torchvision.models

8. Visualização e Interpretabilidade
   ├── Visualização de filtros
   ├── Feature maps
   ├── Grad-CAM
   └── Occlusion sensitivity

9. Data Augmentation para Imagens
   ├── Transformações geométricas
   ├── Transformações de cor
   ├── torchvision.transforms
   ├── albumentations
   └── Augmentações avançadas

10. Exercícios Práticos
```

---

### 5A.2 Classificação de Imagens Avançada

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5A_2_classificacao_imagens.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebooks 4.4, 5A.1 |
| **Datasets** | CIFAR-100, Flowers, Custom datasets |

#### 📋 Conteúdo Detalhado

```
1. Transfer Learning para Classificação
   ├── ImageNet pretrained models
   ├── Feature extraction
   ├── Fine-tuning completo
   └── Discriminative learning rates

2. Training Recipes Modernos
   ├── Progressive resizing
   ├── Test-time augmentation
   ├── Model ensembling
   └── Pseudo-labeling

3. Problemas Específicos
   ├── Fine-grained classification
   ├── Multi-label classification
   ├── Hierarchical classification
   └── Long-tail distribution

4. Loss Functions Avançadas
   ├── Focal loss
   ├── Label smoothing
   ├── Mixup loss
   ├── ArcFace (metric learning)
   └── Contrastive loss

5. Métricas e Avaliação
   ├── Top-k accuracy
   ├── Confusion matrix para imagens
   ├── Per-class metrics
   └── Calibração

6. Kaggle Competition Strategies
   ├── Cross-validation para imagens
   ├── Ensemble strategies
   ├── Post-processing
   └── Leaderboard vs CV

7. Exercícios Práticos
```

---

### 5A.3 Detecção de Objetos

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5A_3_deteccao_objetos.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Notebook 5A.1 |
| **Datasets** | COCO, Pascal VOC, Custom |

#### 📋 Conteúdo Detalhado

```
1. Introdução à Detecção de Objetos
   ├── Classificação vs detecção
   ├── Bounding boxes
   ├── IoU (Intersection over Union)
   └── Métricas (mAP, AP50, AP75)

2. Two-Stage Detectors
   ├── R-CNN
   ├── Fast R-CNN
   ├── Faster R-CNN
   │   ├── Region Proposal Network (RPN)
   │   ├── Anchor boxes
   │   └── ROI Pooling
   └── Cascade R-CNN

3. One-Stage Detectors
   ├── YOLO (v1 até v8)
   │   ├── Arquitetura
   │   ├── Loss function
   │   └── Evolução
   ├── SSD
   ├── RetinaNet (Focal Loss)
   └── Comparação: velocidade vs precisão

4. Anchor-Free Detectors
   ├── FCOS
   ├── CenterNet
   └── Vantagens

5. Feature Pyramid Networks (FPN)
   ├── Multi-scale detection
   ├── Arquitetura
   └── Variantes

6. Non-Maximum Suppression (NMS)
   ├── NMS clássico
   ├── Soft-NMS
   └── NMS-free approaches

7. Implementação Prática
   ├── Detectron2
   ├── YOLOv5/YOLOv8 (Ultralytics)
   ├── MMDetection
   └── Treinamento custom

8. Data Augmentation para Detecção
   ├── Mosaic
   ├── Copy-paste augmentation
   └── Augmentações que preservam boxes

9. Exercícios Práticos
```

---

### 5A.4 Segmentação de Imagens

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5A_4_segmentacao.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Notebook 5A.1 |
| **Datasets** | COCO, Cityscapes, ADE20K, Medical images |

#### 📋 Conteúdo Detalhado

```
1. Tipos de Segmentação
   ├── Semantic segmentation
   ├── Instance segmentation
   ├── Panoptic segmentation
   └── Comparação

2. Arquiteturas para Semantic Segmentation
   ├── FCN (Fully Convolutional Networks)
   ├── U-Net
   │   ├── Encoder-decoder
   │   ├── Skip connections
   │   └── Variantes
   ├── DeepLab (v1, v2, v3, v3+)
   │   ├── Atrous convolution
   │   ├── ASPP
   │   └── Encoder-decoder
   ├── PSPNet
   └── HRNet

3. Instance Segmentation
   ├── Mask R-CNN
   │   ├── Arquitetura
   │   ├── ROI Align
   │   └── Mask head
   ├── YOLACT
   └── SOLOv2

4. Loss Functions para Segmentação
   ├── Cross-entropy pixel-wise
   ├── Dice loss
   ├── Focal loss
   ├── Boundary loss
   └── Combinações

5. Métricas
   ├── IoU / Jaccard
   ├── Dice score
   ├── Pixel accuracy
   └── Mean IoU

6. Técnicas Avançadas
   ├── Multi-scale inference
   ├── Test-time augmentation
   ├── CRF post-processing
   └── Boundary refinement

7. Aplicações
   ├── Medical image segmentation
   ├── Autonomous driving
   ├── Satellite imagery
   └── Video segmentation

8. Implementação Prática
   ├── segmentation_models_pytorch
   ├── MMSegmentation
   └── Treinamento custom

9. Exercícios Práticos
```

---

### 5A.5 Vision Transformers e Modelos Modernos

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5A_5_vision_transformers.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Notebooks 4.2, 5A.1 |
| **Datasets** | ImageNet, CIFAR, Custom |

#### 📋 Conteúdo Detalhado

```
1. Transformers para Visão
   ├── Do NLP para CV
   ├── Patches como tokens
   └── Limitações de CNNs

2. Vision Transformer (ViT)
   ├── Arquitetura
   ├── Patch embedding
   ├── Position embedding
   ├── Class token
   └── Variantes (ViT-B, ViT-L, ViT-H)

3. Variantes de ViT
   ├── DeiT (Data-efficient)
   ├── Swin Transformer
   │   ├── Shifted windows
   │   ├── Hierarchical features
   │   └── Aplicações
   ├── BEiT
   └── CaiT

4. Hybrid Architectures
   ├── CNN + Transformer
   ├── ConvNeXt
   ├── CoAtNet
   └── MaxViT

5. Self-Supervised Learning para Visão
   ├── Contrastive learning (SimCLR, MoCo)
   ├── BYOL, SimSiam
   ├── MAE (Masked Autoencoders)
   ├── DINO
   └── Aplicações

6. CLIP e Vision-Language Models
   ├── Contrastive Language-Image Pre-training
   ├── Zero-shot classification
   ├── CLIP for detection/segmentation
   └── OpenCLIP

7. Foundation Models para Visão
   ├── Segment Anything (SAM)
   ├── DINOv2
   └── Tendências

8. Implementação Prática
   ├── timm library
   ├── Hugging Face Transformers
   └── Fine-tuning ViTs

9. Exercícios Práticos
```

---

## 📝 NÍVEL 5B: NLP (Natural Language Processing)

> **Objetivo:** Dominar processamento de linguagem natural do clássico ao moderno.  
> **Notebooks:** 6 | **Tempo:** ~70 horas

---

### 5B.1 NLP Clássico e Pré-processamento

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5B_1_nlp_classico.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebook 2.1 |
| **Datasets** | 20 Newsgroups, IMDB, Twitter |

#### 📋 Conteúdo Detalhado

```
1. Fundamentos de NLP
   ├── Desafios do processamento de texto
   ├── Níveis de análise (morfológico, sintático, semântico)
   └── Pipeline de NLP

2. Pré-processamento de Texto
   ├── Lowercasing
   ├── Remoção de pontuação
   ├── Tokenização
   │   ├── Word tokenization
   │   ├── Sentence tokenization
   │   └── Subword tokenization (BPE, WordPiece)
   ├── Stopwords
   ├── Stemming vs Lemmatization
   └── Normalização

3. Representação de Texto: Sparse
   ├── Bag of Words (BoW)
   ├── TF-IDF
   │   ├── Term Frequency
   │   ├── Inverse Document Frequency
   │   └── Implementação
   ├── N-grams
   └── Hashing vectorizer

4. Classificação de Texto
   ├── Naive Bayes
   ├── Logistic Regression
   ├── SVM
   └── Métricas específicas

5. Análise de Sentimento
   ├── Sentiment lexicons
   ├── Classificação supervisionada
   └── Aspect-based sentiment

6. Modelagem de Tópicos
   ├── LDA (Latent Dirichlet Allocation)
   ├── NMF
   ├── Escolha de número de tópicos
   └── Interpretação

7. NER (Named Entity Recognition)
   ├── Tipos de entidades
   ├── Abordagens clássicas
   └── spaCy

8. Libraries Essenciais
   ├── NLTK
   ├── spaCy
   ├── scikit-learn
   └── Comparação

9. Exercícios Práticos
```

---

### 5B.2 Word Embeddings

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5B_2_word_embeddings.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebooks 0.2, 5B.1 |
| **Datasets** | Wikipedia, Custom corpora |

#### 📋 Conteúdo Detalhado

```
1. Limitações de Sparse Representations
   ├── Dimensionalidade
   ├── Semântica
   └── Relações entre palavras

2. Distributed Representations
   ├── Intuição
   ├── Espaço vetorial semântico
   └── Word analogies

3. Word2Vec
   ├── CBOW (Continuous Bag of Words)
   ├── Skip-gram
   ├── Negative sampling
   ├── Hiperparâmetros
   └── Treinamento com Gensim

4. GloVe
   ├── Global Vectors
   ├── Co-occurrence matrix
   ├── Diferenças do Word2Vec
   └── Embeddings pré-treinados

5. FastText
   ├── Subword embeddings
   ├── Handling OOV words
   └── Multilingual

6. Usando Embeddings Pré-treinados
   ├── Download e carregamento
   ├── Embedding layer em PyTorch
   └── Fine-tuning vs frozen

7. Avaliação de Embeddings
   ├── Analogias
   ├── Similarity benchmarks
   └── Downstream tasks

8. Visualização
   ├── t-SNE para embeddings
   ├── Projector tools
   └── Análise de clusters

9. Limitações de Static Embeddings
   ├── Polissemia
   ├── Contextualização
   └── Motivação para BERT

10. Exercícios Práticos
```

---

### 5B.3 RNNs e LSTMs para NLP

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5B_3_rnn_lstm_nlp.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Notebooks 4.1, 5B.2 |
| **Datasets** | IMDB, Language modeling data |

#### 📋 Conteúdo Detalhado

```
1. Dados Sequenciais
   ├── Por que sequências importam
   ├── Dependências de longo prazo
   └── Limitações de feedforward

2. RNN Básica
   ├── Arquitetura
   ├── Hidden state
   ├── Backpropagation Through Time (BPTT)
   └── Problemas: vanishing/exploding gradients

3. LSTM (Long Short-Term Memory)
   ├── Cell state
   ├── Gates (forget, input, output)
   ├── Fluxo de informação
   └── Por que resolve vanishing gradient

4. GRU (Gated Recurrent Unit)
   ├── Simplificação do LSTM
   ├── Reset e update gates
   └── LSTM vs GRU

5. Arquiteturas RNN
   ├── Many-to-one (classificação)
   ├── One-to-many (geração)
   ├── Many-to-many (seq2seq)
   └── Bidirectional RNNs

6. Implementação em PyTorch
   ├── nn.RNN, nn.LSTM, nn.GRU
   ├── Packed sequences
   ├── Handling variable lengths
   └── Stacked layers

7. Classificação de Texto com LSTMs
   ├── Arquitetura
   ├── Embedding + LSTM + FC
   └── Treinamento

8. Language Modeling
   ├── O que é
   ├── Perplexity
   ├── Character-level vs word-level
   └── Geração de texto

9. Sequence-to-Sequence
   ├── Encoder-decoder
   ├── Teacher forcing
   └── Aplicações

10. Attention (Introdução)
    ├── Limitações do encoder fixo
    ├── Attention mechanism básico
    └── Preparação para Transformers

11. Exercícios Práticos
```

---

### 5B.4 Transformers e BERT

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5B_4_transformers_bert.ipynb` |
| **Tempo Estimado** | 14-16 horas |
| **Pré-requisitos** | Notebook 5B.3 |
| **Datasets** | GLUE benchmark, Custom |

#### 📋 Conteúdo Detalhado

```
1. Limitações de RNNs
   ├── Sequencialidade
   ├── Long-range dependencies
   └── Paralelização

2. Mecanismo de Atenção
   ├── Query, Key, Value
   ├── Scaled Dot-Product Attention
   ├── Multi-Head Attention
   └── Visualização de attention

3. Arquitetura Transformer
   ├── Encoder stack
   ├── Decoder stack
   ├── Positional encoding
   ├── Feed-forward layers
   ├── Layer normalization
   └── Residual connections

4. BERT (Bidirectional Encoder)
   ├── Pre-training tasks
   │   ├── Masked Language Model (MLM)
   │   └── Next Sentence Prediction (NSP)
   ├── Arquitetura (BERT-base, BERT-large)
   ├── WordPiece tokenization
   └── [CLS] e [SEP] tokens

5. Variantes de BERT
   ├── RoBERTa
   ├── ALBERT
   ├── DistilBERT
   ├── ELECTRA
   └── Multilingual BERT

6. Fine-tuning BERT
   ├── Classification
   ├── NER
   ├── Question Answering
   └── Sentence similarity

7. Hugging Face Transformers
   ├── AutoModel, AutoTokenizer
   ├── Pipeline API
   ├── Trainer API
   └── Custom training loops

8. Tokenizers
   ├── BPE
   ├── WordPiece
   ├── SentencePiece
   └── Hugging Face Tokenizers library

9. Práticas de Fine-tuning
   ├── Learning rates
   ├── Warmup
   ├── Regularização
   └── Epochs e early stopping

10. Benchmarks e Avaliação
    ├── GLUE
    ├── SuperGLUE
    ├── SQuAD
    └── Métricas específicas

11. Exercícios Práticos
```

---

### 5B.5 Large Language Models (LLMs)

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5B_5_large_language_models.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Notebook 5B.4 |
| **Datasets** | Diversos, APIs |

#### 📋 Conteúdo Detalhado

```
1. Evolução para LLMs
   ├── Scaling laws
   ├── Emergent abilities
   └── GPT-1, 2, 3, 4

2. Arquiteturas de LLMs
   ├── Decoder-only (GPT)
   ├── Encoder-only (BERT)
   ├── Encoder-decoder (T5, BART)
   └── Mixture of Experts

3. GPT e Autoregressive Models
   ├── Language modeling objective
   ├── Unidirectional attention
   └── Text generation

4. Instruction-Tuning e RLHF
   ├── InstructGPT
   ├── RLHF pipeline
   ├── Reward modeling
   └── ChatGPT, Claude

5. Open Source LLMs
   ├── LLaMA / Llama 2 / Llama 3
   ├── Mistral
   ├── Falcon
   └── Comparação

6. Usando LLMs via API
   ├── OpenAI API
   ├── Anthropic API
   ├── Hugging Face Inference
   └── Boas práticas

7. Prompt Engineering
   ├── Zero-shot prompting
   ├── Few-shot prompting
   ├── Chain-of-thought
   ├── Self-consistency
   └── Prompt templates

8. Limitações e Desafios
   ├── Hallucinations
   ├── Context length
   ├── Factuality
   └── Bias e safety

9. Avaliação de LLMs
   ├── Benchmarks (MMLU, HellaSwag)
   ├── Human evaluation
   └── Automatic metrics

10. Exercícios Práticos
```

---

### 5B.6 RAG e Aplicações de LLMs

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5B_6_rag_aplicacoes_llm.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Notebook 5B.5 |
| **Datasets** | Custom documents, knowledge bases |

#### 📋 Conteúdo Detalhado

```
1. Retrieval-Augmented Generation (RAG)
   ├── Motivação
   ├── Arquitetura básica
   └── Retriever + Generator

2. Document Processing
   ├── Chunking strategies
   ├── Metadata extraction
   └── Preprocessing

3. Embeddings para Retrieval
   ├── Sentence embeddings
   ├── Dense vs sparse retrieval
   ├── Modelos: SBERT, E5, BGE
   └── Reranking

4. Vector Databases
   ├── Conceitos
   ├── Pinecone
   ├── Weaviate
   ├── ChromaDB
   ├── FAISS
   └── Comparação

5. Building RAG Pipelines
   ├── LangChain
   ├── LlamaIndex
   ├── Haystack
   └── Custom pipelines

6. RAG Avançado
   ├── Hybrid search
   ├── Query rewriting
   ├── Multi-hop reasoning
   └── Self-RAG

7. Agents e Tool Use
   ├── ReAct framework
   ├── Function calling
   ├── Agents com LangChain
   └── Autonomous agents

8. Avaliação de RAG
   ├── Retrieval metrics
   ├── Generation metrics
   ├── End-to-end evaluation
   └── RAGAS framework

9. Aplicações Práticas
   ├── Chatbots sobre documentos
   ├── Q&A systems
   ├── Semantic search
   └── Knowledge assistants

10. Exercícios Práticos
```

---

## 🎨 NÍVEL 5C: GENERATIVE AI

> **Objetivo:** Dominar modelos generativos para imagens, texto e multimodal.  
> **Notebooks:** 5 | **Tempo:** ~60 horas

---

### 5C.1 GANs (Generative Adversarial Networks)

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5C_1_gans.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Notebook 4.1, 5A.1 |
| **Datasets** | MNIST, CelebA, CIFAR-10 |

#### 📋 Conteúdo Detalhado

```
1. Introdução a Modelos Generativos
   ├── Discriminativo vs Generativo
   ├── Tipos de modelos generativos
   └── Aplicações

2. GAN: Conceito
   ├── Generator vs Discriminator
   ├── Minimax game
   ├── Nash equilibrium
   └── Training dynamics

3. Arquitetura de GANs
   ├── Generator network
   ├── Discriminator network
   ├── Latent space
   └── Implementação básica

4. DCGAN
   ├── Convolutional GANs
   ├── Architectural guidelines
   └── Implementação

5. Problemas de Treinamento
   ├── Mode collapse
   ├── Vanishing gradients
   ├── Training instability
   └── Evaluation challenges

6. Técnicas de Estabilização
   ├── Wasserstein GAN (WGAN)
   ├── Spectral normalization
   ├── Progressive growing
   └── Two-timescale update

7. Conditional GANs
   ├── Class-conditional generation
   ├── cGAN, ACGAN
   └── Pix2Pix

8. Arquiteturas Avançadas
   ├── StyleGAN (1, 2, 3)
   ├── BigGAN
   ├── CycleGAN
   └── Image-to-image translation

9. Métricas de Avaliação
   ├── Inception Score (IS)
   ├── FID (Fréchet Inception Distance)
   ├── LPIPS
   └── Human evaluation

10. Exercícios Práticos
```

---

### 5C.2 VAEs (Variational Autoencoders)

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5C_2_vaes.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebooks 0.7, 4.1 |
| **Datasets** | MNIST, CelebA, dSprites |

#### 📋 Conteúdo Detalhado

```
1. Autoencoders Revisitados
   ├── Encoder-decoder
   ├── Bottleneck
   ├── Reconstruction loss
   └── Limitações para geração

2. VAE: Motivação
   ├── Latent space contínuo
   ├── Amostragem para geração
   └── Regularização do espaço latente

3. Matemática do VAE
   ├── Evidence Lower Bound (ELBO)
   ├── KL divergence
   ├── Reparametrization trick
   └── Loss function

4. Implementação
   ├── Encoder (mean, logvar)
   ├── Decoder
   ├── Training loop
   └── Geração

5. Explorando o Espaço Latente
   ├── Interpolação
   ├── Atributos aprendidos
   └── Disentanglement

6. Variantes de VAE
   ├── β-VAE
   ├── VQ-VAE (Vector Quantized)
   ├── VQ-VAE-2
   └── NVAE

7. Conditional VAE
   ├── Arquitetura
   ├── Aplicações
   └── Implementação

8. VAE vs GAN
   ├── Trade-offs
   ├── Qualidade vs coverage
   └── Quando usar cada um

9. Aplicações
   ├── Geração de imagens
   ├── Anomaly detection
   ├── Data augmentation
   └── Representation learning

10. Exercícios Práticos
```

---

### 5C.3 Diffusion Models

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5C_3_diffusion_models.ipynb` |
| **Tempo Estimado** | 14-16 horas |
| **Pré-requisitos** | Notebooks 0.7, 4.1, 5C.1 |
| **Datasets** | CIFAR-10, CelebA, Custom |

#### 📋 Conteúdo Detalhado

```
1. Introdução a Diffusion Models
   ├── Histórico
   ├── Intuição: destruir e reconstruir
   └── Por que funcionam tão bem

2. Forward Process (Diffusion)
   ├── Adição gradual de ruído
   ├── Noise schedule
   └── Matemática

3. Reverse Process (Denoising)
   ├── Aprendendo a remover ruído
   ├── Score matching
   └── Denoising score matching

4. DDPM (Denoising Diffusion Probabilistic Models)
   ├── Training objective
   ├── Sampling process
   └── Implementação

5. Arquiteturas
   ├── U-Net para diffusion
   ├── Time embedding
   ├── Attention layers
   └── Condicionamento

6. Avanços em Sampling
   ├── DDIM (Deterministic)
   ├── Fewer steps
   └── Guidance scales

7. Conditional Generation
   ├── Class-conditional
   ├── Classifier guidance
   ├── Classifier-free guidance
   └── Text-conditional (intro)

8. Latent Diffusion Models
   ├── Stable Diffusion architecture
   ├── VAE encoder/decoder
   ├── Latent space diffusion
   └── Eficiência computacional

9. Stable Diffusion
   ├── Arquitetura completa
   ├── Text encoder (CLIP)
   ├── Inference pipeline
   └── Diffusers library

10. Aplicações
    ├── Text-to-image
    ├── Image-to-image
    ├── Inpainting
    ├── Super-resolution
    └── ControlNet

11. Exercícios Práticos
```

---

### 5C.4 Fine-tuning e Customização de Modelos Generativos

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5C_4_finetuning_generativo.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Notebooks 5B.4, 5C.3 |
| **Datasets** | Custom datasets |

#### 📋 Conteúdo Detalhado

```
1. Por que Fine-tuning
   ├── Modelos base vs customizados
   ├── Domain adaptation
   └── Personalization

2. Fine-tuning de LLMs
   ├── Full fine-tuning
   ├── Catastrophic forgetting
   └── Custo computacional

3. Parameter-Efficient Fine-Tuning (PEFT)
   ├── LoRA (Low-Rank Adaptation)
   │   ├── Conceito
   │   ├── Implementação
   │   └── Hiperparâmetros
   ├── QLoRA
   │   ├── Quantização
   │   └── Eficiência
   ├── Prefix tuning
   ├── Prompt tuning
   └── Adapters

4. Fine-tuning de Diffusion Models
   ├── DreamBooth
   │   ├── Few-shot personalization
   │   └── Implementação
   ├── Textual Inversion
   ├── LoRA para Stable Diffusion
   └── ControlNet training

5. Datasets para Fine-tuning
   ├── Curação de dados
   ├── Quality vs quantity
   ├── Data augmentation
   └── Labeling

6. Training Recipes
   ├── Learning rates
   ├── Batch sizes
   ├── Epochs
   └── Regularização

7. Evaluation e Quality Control
   ├── Métricas automáticas
   ├── Human evaluation
   └── Overfitting detection

8. Infraestrutura
   ├── GPU requirements
   ├── Cloud options
   ├── Gradient accumulation
   └── Mixed precision

9. Deployment de Modelos Fine-tuned
   ├── Merging LoRA weights
   ├── Quantização para inference
   └── Serving

10. Exercícios Práticos
```

---

### 5C.5 Multimodal AI e Aplicações Avançadas

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5C_5_multimodal_ai.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Notebooks 5A.5, 5B.5, 5C.3 |
| **Datasets** | Multimodal datasets |

#### 📋 Conteúdo Detalhado

```
1. Multimodal Learning
   ├── O que é
   ├── Modalidades (texto, imagem, áudio, vídeo)
   └── Desafios

2. Vision-Language Models
   ├── CLIP
   │   ├── Contrastive learning
   │   ├── Zero-shot capabilities
   │   └── Aplicações
   ├── BLIP / BLIP-2
   ├── Flamingo
   └── LLaVA

3. Text-to-Image Generation
   ├── DALL-E (1, 2, 3)
   ├── Stable Diffusion
   ├── Midjourney
   └── Imagen

4. Image-to-Text
   ├── Image captioning
   ├── Visual Question Answering (VQA)
   ├── OCR avançado
   └── Document understanding

5. Video Models
   ├── Video generation
   ├── Video understanding
   └── Temporal modeling

6. Audio e Speech
   ├── Text-to-Speech (TTS)
   ├── Speech-to-Text (Whisper)
   ├── Music generation
   └── Voice cloning

7. Unified Models
   ├── GPT-4V
   ├── Gemini
   └── Tendências

8. Aplicações Práticas
   ├── Content creation
   ├── Accessibility
   ├── Creative tools
   └── Business applications

9. Ética e Responsible AI
   ├── Deepfakes
   ├── Copyright
   ├── Bias em geração
   └── Mitigações

10. Exercícios Práticos
```

---

## 📈 NÍVEL 5D: SÉRIES TEMPORAIS

> **Objetivo:** Dominar análise e previsão de séries temporais.  
> **Notebooks:** 4 | **Tempo:** ~40 horas

---

### 5D.1 Séries Temporais: Fundamentos

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5D_1_series_temporais_fundamentos.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebooks 1.1, 1.2 |
| **Datasets** | Airline Passengers, Daily Temperature |

#### 📋 Conteúdo Detalhado

```
1. Conceitos Fundamentais
2. Decomposição (Tendência, Sazonalidade, Resíduo)
3. Estacionariedade e Testes (ADF, KPSS)
4. Autocorrelação (ACF, PACF)
5. Transformações (Differencing, Log, Box-Cox)
6. Visualização de Séries Temporais
7. EDA para Séries Temporais
8. Exercícios Práticos
```

---

### 5D.2 Modelos Estatísticos (ARIMA, Prophet)

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5D_2_arima_prophet.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebook 5D.1 |
| **Datasets** | Multiple time series datasets |

#### 📋 Conteúdo Detalhado

```
1. AR, MA, ARMA Models
2. ARIMA
3. SARIMA (Seasonal)
4. Auto ARIMA
5. Prophet
6. Exponential Smoothing
7. Validação Temporal (Walk-forward)
8. Métricas (MAE, RMSE, MAPE, SMAPE)
9. Exercícios Práticos
```

---

### 5D.3 Machine Learning para Séries Temporais

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5D_3_ml_series_temporais.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebooks 3.2, 3.3, 5D.1 |
| **Datasets** | Walmart Sales, Energy Consumption |

#### 📋 Conteúdo Detalhado

```
1. Feature Engineering Temporal
   ├── Lag features
   ├── Rolling statistics
   ├── Date/time features
   └── Fourier features

2. ML Models para TS
   ├── Random Forest
   ├── XGBoost
   ├── LightGBM
   └── Comparação com estatísticos

3. Multi-step Forecasting
   ├── Recursive strategy
   ├── Direct strategy
   ├── Multi-output
   └── Trade-offs

4. Multiple Time Series
   ├── Global models
   ├── Hierarchical forecasting
   └── Cross-learning

5. Validação e Backtesting
6. Exercícios Práticos
```

---

### 5D.4 Deep Learning para Séries Temporais

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `5D_4_dl_series_temporais.ipynb` |
| **Tempo Estimado** | 10-12 horas |
| **Pré-requisitos** | Notebooks 4.1, 5B.3, 5D.3 |
| **Datasets** | Complex time series datasets |

#### 📋 Conteúdo Detalhado

```
1. LSTMs para Forecasting
2. Sequence-to-Sequence
3. Temporal Convolutional Networks (TCN)
4. Transformers para Time Series
5. N-BEATS
6. Temporal Fusion Transformer (TFT)
7. Darts Library
8. Exercícios Práticos
```

---

## 🚀 NÍVEL 6: PRODUÇÃO (MLOps)

> **Objetivo:** Colocar modelos em produção e mantê-los.  
> **Notebooks:** 4 | **Tempo:** ~50 horas

---

### 6.1 Deploy de Modelos

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `6_1_deploy_modelos.ipynb` |
| **Tempo Estimado** | 12-14 horas |
| **Pré-requisitos** | Níveis 3-5 |

#### 📋 Conteúdo

```
1. Do Notebook à Produção
2. Serialização (joblib, pickle, ONNX)
3. FastAPI para ML
4. Docker para ML
5. Testes de ML
6. CI/CD básico
7. Cloud Deployment
8. Exercícios Práticos
```

---

### 6.2 MLflow e Experiment Tracking

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `6_2_mlflow_tracking.ipynb` |
| **Tempo Estimado** | 10-12 horas |

#### 📋 Conteúdo

```
1. Experiment Tracking
2. MLflow Tracking
3. MLflow Projects
4. MLflow Models
5. Model Registry
6. Integração com frameworks
7. Exercícios Práticos
```

---

### 6.3 Monitoramento e Data Drift

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `6_3_monitoramento_drift.ipynb` |
| **Tempo Estimado** | 12-14 horas |

#### 📋 Conteúdo

```
1. Por que Modelos Degradam
2. Data Drift
3. Concept Drift
4. Model Decay
5. Métricas de Monitoramento
6. Alertas
7. Estratégias de Retraining
8. Ferramentas (Evidently, WhyLabs)
9. Exercícios Práticos
```

---

### 6.4 Pipelines de ML Automatizados

| Atributo | Detalhe |
|----------|---------|
| **Arquivo** | `6_4_pipelines_automatizados.ipynb` |
| **Tempo Estimado** | 12-14 horas |

#### 📋 Conteúdo

```
1. CI/CD para ML
2. Testes para ML
3. Orquestração (Airflow/Prefect)
4. Feature Stores
5. Pipeline End-to-End
6. Boas Práticas MLOps
7. Exercícios Práticos
```

---

## 📊 RESUMO EXECUTIVO FINAL

| Nível | Nome | Notebooks | Horas |
|-------|------|-----------|-------|
| **0** | Matemática | 8 | ~80h |
| **1** | Estatística | 5 | ~50h |
| **2** | Fundamentos | 4 | ~35h |
| **3** | Core ML | 6 | ~55h |
| **4** | Deep Learning | 6 | ~70h |
| **5A** | Computer Vision | 5 | ~60h |
| **5B** | NLP | 6 | ~70h |
| **5C** | Generative AI | 5 | ~60h |
| **5D** | Séries Temporais | 4 | ~40h |
| **6** | MLOps | 4 | ~50h |
| **TOTAL** | | **53** | **~570h** |

---

## 🎯 TRILHAS DE APRENDIZADO

### Trilha Completa (Data Scientist Sênior)
```
0.x → 1.x → 2.x → 3.x → 4.x → [Escolher especialização 5x] → 6.x
Tempo: ~400-500 horas
```

### Trilha ML Engineer
```
2.x → 3.x → 4.1-4.3 → 6.x
Tempo: ~200 horas
```

### Trilha Computer Vision
```
0.2-0.4 → 2.1 → 4.x → 5A.x
Tempo: ~250 horas
```

### Trilha NLP/LLM
```
0.6-0.7 → 2.1 → 4.1-4.3 → 5B.x → 5C.4
Tempo: ~280 horas
```

### Trilha Generative AI
```
0.4, 0.7 → 4.x → 5A.1 → 5B.4-5B.5 → 5C.x
Tempo: ~250 horas
```

### Trilha Data Analyst → Data Scientist
```
1.x → 2.x → 3.1-3.3 → 5D.1-5D.2
Tempo: ~180 horas
```

### Quick Start (Mínimo Viável)
```
2.1 → 3.1 → 3.2 → 6.1
Tempo: ~50 horas
```

---

## 📋 ORDEM DE CRIAÇÃO RECOMENDADA

### Fase 1: Base
1-8. Nível 0 (Matemática)
9-13. Nível 1 (Estatística)
14-17. Nível 2 (Fundamentos)

### Fase 2: Core
18-23. Nível 3 (Core ML)
24-29. Nível 4 (Deep Learning)

### Fase 3: Especializações
30-34. Nível 5A (Computer Vision)
35-40. Nível 5B (NLP)
41-45. Nível 5C (Generative AI)
46-49. Nível 5D (Séries Temporais)

### Fase 4: Produção
50-53. Nível 6 (MLOps)

---

**Versão:** 3.0  
**Total de Notebooks:** 53  
**Tempo Total:** ~570 horas  
**Última Atualização:** Janeiro 2025
