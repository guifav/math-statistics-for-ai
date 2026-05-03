# Sumário dos 9 Notebooks Jupyter Educacionais de ML

## Resumo Executivo

Foram criados **9 notebooks Jupyter educacionais** em português (pt-BR) cobrindo Estatística e Fundamentos de Data Science para Machine Learning. Todos os notebooks estão salvos em `/sessions/kind-ecstatic-archimedes/mnt/notebooks-math&statistics/`.

---

## NÍVEL 1: ESTATÍSTICA (5 Notebooks)

### 1. **1_1_estatistica_descritiva.ipynb** (44 células)
- **Título:** Estatística Descritiva e Exploratória
- **Pré-requisito:** 0.6
- **Tempo:** 8-10 horas
- **Conteúdo:**
  - Média, mediana, moda, ponderada, geométrica
  - Variância, desvio padrão, IQR, coeficiente de variação, MAD
  - Skewness, kurtosis, QQ-plots
  - Percentis, quartis, detecção de outliers (IQR e Z-score)
  - Histogramas, KDE plots, violin plots
  - Análise bivariada: scatter, correlação Pearson/Spearman
  - Heatmap e pair plots
  - Exercícios: análise completa do Titanic

### 2. **1_2_estatistica_inferencial.ipynb** (40 células)
- **Título:** Estatística Inferencial e Testes de Hipótese
- **Pré-requisitos:** 0.6, 0.7, 1.1
- **Tempo:** 12-14 horas
- **Conteúdo:**
  - Distribuição amostral e erro padrão
  - Intervalos de confiança (z e t)
  - Teste de hipótese: H₀, H₁, p-value, erro tipo I/II
  - Teste t de Student (1 e 2 amostras, pareado)
  - Teste qui-quadrado para independência
  - ANOVA one-way e comparações post-hoc
  - Teste de normalidade (Shapiro-Wilk) e homocedasticidade
  - A/B Testing completo: tamanho amostral, poder
  - Bootstrap para intervalos sem pressupostos
  - Múltiplos testes: Bonferroni e FDR
  - Exercícios: A/B test e bootstrap

### 3. **1_3_estatistica_bayesiana.ipynb** (35 células)
- **Título:** Estatística Bayesiana para ML
- **Pré-requisitos:** 0.7, 1.2
- **Tempo:** 10-12 horas
- **Conteúdo:**
  - Frequentista vs Bayesiano: filosofia e diferenças
  - Teorema de Bayes: prior, likelihood, posterior, evidência
  - Priors conjugados: Beta-Binomial e Normal-Normal
  - Atualização bayesiana sequencial (com animação)
  - Naive Bayes: GaussianNB, MultinomialNB, BernoulliNB
  - Classificador de spam com Naive Bayes
  - Credible intervals vs confidence intervals
  - MAP e conexão com regularização (Ridge/Lasso)
  - Exercícios: Bayesian update sequencial, Naive Bayes from scratch

### 4. **1_4_regressao_estatistica.ipynb** (23 células)
- **Título:** Regressão Estatística: da Teoria ao Diagnóstico
- **Pré-requisitos:** 0.4, 0.7, 1.2
- **Tempo:** 10-12 horas
- **Conteúdo:**
  - Regressão linear simples e múltipla (OLS)
  - Diagnóstico de resíduos: normalidade, homocedasticidade
  - Multicolinearidade: VIF (Variance Inflation Factor)
  - Regularização: Ridge (L2), Lasso (L1), ElasticNet
  - Validação cruzada para seleção de λ
  - Regressão polinomial e overfitting
  - Learning curves: diagnóstico viés/variância
  - Exercícios: análise completa com diagnóstico

### 5. **1_5_design_experimentos.ipynb** (19 células)
- **Título:** Design de Experimentos e Análise Estatística
- **Pré-requisitos:** 1.2, 1.4
- **Tempo:** 8-10 horas
- **Conteúdo:**
  - Princípios: randomização, replicação, controle
  - Cálculo de tamanho amostral e poder
  - A/B testing bayesiano vs frequentista
  - Stopping rule e peaking problem
  - A/B/C testing multivariado
  - Causalidade: DAGs, confounding, mediação
  - Cross-validation como design experimental
  - Time series CV para dados temporais
  - Exercícios: planejamento de A/B test

---

## NÍVEL 2: DATA SCIENCE (4 Notebooks)

### 6. **2_1_python_data_science.ipynb** (23 células)
- **Título:** Python para Data Science: NumPy, Pandas e Visualização
- **Pré-requisito:** Nenhum (independente)
- **Tempo:** 10-12 horas
- **Conteúdo:**
  - NumPy: arrays, indexing, broadcasting, ufuncs
  - Álgebra linear: produto matricial, determinante, inversa
  - Pandas Series e DataFrame: criação, indexing (.loc, .iloc)
  - Leitura de dados: CSV, JSON, Excel
  - Limpeza: valores ausentes (fillna, dropna, interpolate), duplicatas
  - Feature engineering: apply, map, groupby, pivot_table, merge/join
  - Matplotlib: subplots, gráficos de linha, scatter, histograma, barras
  - Seaborn: boxplot, violinplot, pairplot, heatmap
  - Plotly: gráficos interativos com scatter e animações
  - Exercícios: pipeline completo de limpeza e visualização

### 7. **2_2_eda_completa.ipynb** (23 células)
- **Título:** Análise Exploratória de Dados (EDA) Completa
- **Pré-requisitos:** 2.1, 1.1
- **Tempo:** 10-12 horas
- **Conteúdo:**
  - Framework de EDA: perguntas antes de olhar dados
  - Inspeções básicas: shape, dtypes, describe()
  - Análise univariada: histogramas, box plots, contagens
  - Detecção de outliers: IQR, Z-score, visualização
  - Valores ausentes: mapa de ausências, estratégias MCAR/MAR/MNAR
  - Análise bivariada: scatter, correlação, contingência
  - Pair plots e relacionamentos multivariados
  - Feature engineering exploratório: categorização, interações
  - Detecção de data leakage na fase exploratória
  - Relatório EDA automático
  - Exercícios: EDA completa no Titanic com insights

### 8. **2_3_sql_e_apis.ipynb** (23 células)
- **Título:** SQL e APIs para Coleta de Dados em ML
- **Pré-requisito:** 2.1
- **Tempo:** 8-10 horas
- **Conteúdo:**
  - SQL básico: SELECT, WHERE, GROUP BY, HAVING, ORDER BY
  - SQL avançado para ML: agregações, joins, window functions
  - Integração Pandas ↔ SQL: read_sql, to_sql
  - REST APIs: GET, POST, PUT, DELETE
  - Autenticação: Bearer Token, API Key, Basic Auth
  - JSON parsing: acesso aninhado, normalização com json_normalize
  - Paginação em APIs: offset/limit, page-based, cursor-based
  - Coleta com JSONPlaceholder (API gratuita)
  - Rate limiting e retry logic com backoff exponencial
  - Tratamento de erros: timeouts, conexão, JSON inválido, HTTP errors
  - Web scraping básico com BeautifulSoup
  - Exercícios: coleta de API com paginação e tratamento de erro

### 9. **2_4_acesso_banco_dados.ipynb** (23 células)
- **Título:** Bancos de Dados para Projetos de ML
- **Pré-requisito:** 2.3
- **Tempo:** 8-10 horas
- **Conteúdo:**
  - Tipos de banco: relacional, NoSQL (documento, chave-valor), vetorial
  - Series temporal e data warehouses
  - SQLite para prototipagem local
  - PostgreSQL e SQLAlchemy ORM
  - Feature Store: armazenar features pré-computadas
  - Parquet: formato colunar comprimido para ML
  - Pipeline de dados: ingestion → processing → features → treino/inference
  - Versionamento e auditoria: rastreamento de mudanças
  - Boas práticas: separação de layers, schema validation, monitoramento
  - Segurança: anonimização, controle de acesso, compliance
  - Exercícios: feature store completo e pipeline end-to-end

---

## Estatísticas dos Notebooks

| Métrica | Valor |
|---------|-------|
| **Total de Notebooks** | 9 |
| **Total de Células** | ~280 |
| **Linhas de Código (aprox.)** | ~3500+ |
| **Idioma** | Português (pt-BR) |
| **Tamanho Total (arquivos)** | ~190 KB |
| **Tempo de Estudo Total** | 75-90 horas |

---

## Arquivos Criados

```
/sessions/kind-ecstatic-archimedes/mnt/notebooks-math&statistics/
├── 1_1_estatistica_descritiva.ipynb         (44 células, ~30 KB)
├── 1_2_estatistica_inferencial.ipynb        (40 células, ~46 KB)
├── 1_3_estatistica_bayesiana.ipynb          (35 células, ~33 KB)
├── 1_4_regressao_estatistica.ipynb          (23 células, ~21 KB)
├── 1_5_design_experimentos.ipynb            (19 células, ~19 KB)
├── 2_1_python_data_science.ipynb            (23 células, ~15 KB)
├── 2_2_eda_completa.ipynb                   (23 células, ~17 KB)
├── 2_3_sql_e_apis.ipynb                     (23 células, ~21 KB)
└── 2_4_acesso_banco_dados.ipynb             (23 células, ~18 KB)
```

---

## Características Técnicas

### Markdown (pt-BR)
✓ Títulos e objetivos de aprendizado  
✓ Explicações conceituais completas  
✓ Exemplos práticos e casos de uso  
✓ Interpretação de resultados  

### Código Python
✓ Variáveis e comentários em inglês  
✓ Sem docstrings (aspas triplas) em cells — apenas `# comentários`  
✓ Imports organizados  
✓ Visualizações com matplotlib/seaborn  
✓ Exemplos reproduzíveis com seed  

### Estrutura
✓ 35-45 células por notebook (3 notebooks)  
✓ 19-40 células para notebooks menores  
✓ Progressão lógica: fundamentos → aplicações  
✓ 3-4 exercícios finais por notebook  

### Bibliotecas Principais
- NumPy, Pandas: manipulação de dados
- Matplotlib, Seaborn: visualizações
- SciPy, scikit-learn: estatística e ML
- SQLite, requests: dados
- Plotly: gráficos interativos

---

## Roadmap de Aprendizado Recomendado

### Semana 1-2: Estatística Descritiva
→ 1.1 (Análise univariada, bivariada)

### Semana 3-4: Estatística Inferencial
→ 1.2 (Testes, intervalos, A/B testing)
→ 1.3 (Bayesiano, priors, Naive Bayes)

### Semana 5-6: Regressão
→ 1.4 (OLS, diagnóstico, regularização)

### Semana 7: Design de Experimentos
→ 1.5 (A/B/C testing, causalidade)

### Semana 8-9: Data Science Prático
→ 2.1 (NumPy, Pandas, Matplotlib)
→ 2.2 (EDA completa)

### Semana 10: Dados em Produção
→ 2.3 (SQL, APIs)
→ 2.4 (Bancos de dados, pipelines)

---

## Como Usar

1. **Abrir os notebooks:**
   ```bash
   jupyter notebook /sessions/kind-ecstatic-archimedes/mnt/notebooks-math&statistics/
   ```

2. **Executar células:**
   - Pressione `Shift + Enter` para executar cada célula
   - Ou `Ctrl + Enter` para executar sem avanço

3. **Fazer modificações:**
   - Todos os notebooks são editáveis
   - Adicione suas próprias análises
   - Crie novos experimentos

4. **Seguir os exercícios:**
   - Cada notebook termina com 3-4 exercícios
   - Tente resolver antes de ver a solução
   - Adapte para seus próprios dados

---

## Pré-requisitos de Ambiente

**Python 3.8+**
```bash
pip install numpy pandas matplotlib seaborn scipy scikit-learn plotly requests beautifulsoup4 sqlalchemy
```

---

## Notas Importantes

- **Linguagem:** Markdown em português (pt-BR), código em inglês
- **Estilo:** Educacional, progressivo, com muitas visualizações
- **Dados:** Usa datasets públicos (Titanic, Iris, Diabetes, etc)
- **Reprodutibilidade:** Seed aleatória definida em todos os exemplos
- **Moderno:** Segue boas práticas de 2024-2025

---

**Criado em:** 08 de março de 2026  
**Total de tempo de criação:** ~40 minutos (9 notebooks em paralelo)  
**Qualidade:** Notebooks prontos para produção educacional

