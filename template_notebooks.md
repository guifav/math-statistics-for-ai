# 📐 Padrão de Criação de Notebooks Educacionais de Machine Learning

> **Versão:** 1.0  
> **Última atualização:** Janeiro 2025  
> **Objetivo:** Garantir consistência, qualidade pedagógica e aplicabilidade prática em todos os notebooks da série.

---

## 1. Filosofia Educacional

### 1.1 Princípios Fundamentais

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         PIRÂMIDE DE APRENDIZAGEM                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│                            ┌─────────┐                                  │
│                            │ CRIAR   │  ← Projetos próprios             │
│                           ┌┴─────────┴┐                                 │
│                           │  AVALIAR  │  ← Comparar modelos             │
│                          ┌┴───────────┴┐                                │
│                          │  ANALISAR   │  ← Interpretar resultados      │
│                         ┌┴─────────────┴┐                               │
│                         │   APLICAR     │  ← Exercícios práticos        │
│                        ┌┴───────────────┴┐                              │
│                        │   COMPREENDER   │  ← Explicações conceituais   │
│                       ┌┴─────────────────┴┐                             │
│                       │    LEMBRAR        │  ← Definições e fórmulas    │
│                       └───────────────────┘                             │
│                                                                         │
│  Cada notebook deve atingir pelo menos o nível "APLICAR"                │
└─────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Proporção Teoria/Prática

| Componente | Proporção | Descrição |
|------------|-----------|-----------|
| **Teoria conceitual** | 30% | Explicações, intuição, matemática |
| **Código comentado** | 40% | Implementação com explicações inline |
| **Visualizações** | 15% | Gráficos que reforçam conceitos |
| **Exercícios/Desafios** | 15% | Prática guiada e livre |

### 1.3 Abordagem Pedagógica

1. **Contexto primeiro:** Sempre começar com o "porquê" antes do "como"
2. **Exemplos concretos:** Usar analogias do mundo real
3. **Progressão gradual:** Do simples ao complexo
4. **Erros comuns:** Mostrar armadilhas e como evitá-las
5. **Conexões:** Relacionar com conhecimentos anteriores

---

## 2. Estrutura Padrão do Notebook

### 2.1 Template de Seções

```markdown
# 📚 [Título do Notebook]

**[Subtítulo descritivo]**

---

## Índice
[Índice clicável com âncoras]

---

## 1. Introdução e Motivação
- O que é [conceito]?
- Por que isso é importante?
- Onde é aplicado no mundo real?
- O que você vai aprender neste notebook?

## 2. Configuração do Ambiente
- Instalação de dependências
- Imports organizados por categoria
- Configurações globais (seeds, estilos)

## 3. Fundamentos Teóricos
- Conceitos essenciais
- Matemática necessária (com visualizações)
- Intuição geométrica/estatística

## 4. Dataset(s)
- Apresentação do(s) dataset(s)
- Contexto e fonte
- Análise exploratória (EDA)

## 5-N. [Tópicos Específicos do Tema]
- Teoria do tópico
- Implementação passo a passo
- Visualizações
- Interpretação dos resultados

## N+1. Estudo de Caso Completo
- Problema real do início ao fim
- Aplicação integrada dos conceitos

## N+2. Erros Comuns e Boas Práticas
- Armadilhas frequentes
- Como evitar/resolver
- Checklist de boas práticas

## N+3. Exercícios Práticos
- Exercícios guiados (com hints)
- Desafios (sem solução imediata)
- Projeto mini para praticar

## N+4. Resumo e Próximos Passos
- Recapitulação dos pontos-chave
- Conexão com próximos notebooks
- Recursos adicionais (livros, papers, cursos)

## Referências
- Papers
- Livros
- Documentação oficial
```

### 2.2 Cabeçalho Padrão (Primeira Célula Markdown)

```markdown
# 📚 [Emoji] Título do Notebook

**Subtítulo: Uma frase que resume o conteúdo**

---

| Informação | Detalhe |
|------------|---------|
| **Nível** | Fundamentos / Core / Avançado / Especialização |
| **Pré-requisitos** | Links para notebooks anteriores |
| **Tempo estimado** | X horas |
| **Datasets** | Nome dos datasets utilizados |
| **Bibliotecas** | Principais libs usadas |

---

## 🎯 Objetivos de Aprendizagem

Ao final deste notebook, você será capaz de:

1. [Verbo de ação] + [conceito] + [contexto]
2. [Verbo de ação] + [conceito] + [contexto]
3. [Verbo de ação] + [conceito] + [contexto]
4. [Verbo de ação] + [conceito] + [contexto]

---
```

### 2.3 Emojis Padrão por Seção

| Emoji | Uso |
|-------|-----|
| 📚 | Título principal |
| 🎯 | Objetivos |
| ⚙️ | Configuração/Setup |
| 📖 | Teoria/Conceitos |
| 📊 | Datasets/Dados |
| 💻 | Código/Implementação |
| 📈 | Visualizações |
| ⚠️ | Avisos/Cuidados |
| 💡 | Dicas/Insights |
| 🔍 | Análise/Investigação |
| ✅ | Boas práticas |
| ❌ | Erros comuns |
| 🧪 | Experimentos |
| 🏆 | Exercícios/Desafios |
| 📝 | Resumo |
| 🔗 | Referências |
| 🚀 | Próximos passos |

---

## 3. Padrões de Código

### 3.1 Célula de Imports (Template)

```python
# ============================================================
# CONFIGURAÇÃO DO AMBIENTE
# ============================================================

# Instalação de dependências (executar apenas uma vez)
# !pip install pandas numpy matplotlib seaborn scikit-learn -q

# ------------------------------------------------------------
# Imports: Manipulação de Dados
# ------------------------------------------------------------
import numpy as np
import pandas as pd

# ------------------------------------------------------------
# Imports: Visualização
# ------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# Imports: Machine Learning
# ------------------------------------------------------------
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# ... outros imports específicos

# ------------------------------------------------------------
# Imports: Utilidades
# ------------------------------------------------------------
import warnings
warnings.filterwarnings('ignore')

# ------------------------------------------------------------
# Configurações Globais
# ------------------------------------------------------------
# Reprodutibilidade
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# Visualização
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('husl')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

# Pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 4)
pd.set_option('display.float_format', '{:.4f}'.format)

print("✅ Ambiente configurado com sucesso!")
print(f"📌 Random state: {RANDOM_STATE}")
```

### 3.2 Padrões de Nomenclatura

```python
# Variáveis
dados_brutos = ...          # snake_case para variáveis
X_train, X_test = ...       # X maiúsculo para features
y_train, y_test = ...       # y minúsculo para target
df_clientes = ...           # prefixo df_ para DataFrames

# Constantes
RANDOM_STATE = 42           # UPPER_CASE para constantes
MAX_ITERATIONS = 1000
LEARNING_RATE = 0.01

# Funções
def calcular_metricas():    # snake_case para funções
    pass

def plotar_distribuicao():  # verbos descritivos
    pass

# Classes (quando necessário)
class MeuModelo:            # PascalCase para classes
    pass
```

### 3.3 Padrão de Documentação de Funções

```python
def calcular_metricas_classificacao(y_true, y_pred, y_proba=None):
    """
    Calcula métricas de avaliação para problemas de classificação.
    
    Esta função computa as principais métricas usadas para avaliar
    modelos de classificação, incluindo métricas baseadas em 
    probabilidade quando disponíveis.
    
    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        Rótulos verdadeiros.
    y_pred : array-like of shape (n_samples,)
        Rótulos previstos pelo modelo.
    y_proba : array-like of shape (n_samples, n_classes), optional
        Probabilidades previstas. Necessário para calcular AUC-ROC.
    
    Returns
    -------
    dict
        Dicionário contendo:
        - 'accuracy': Acurácia do modelo
        - 'precision': Precisão (macro)
        - 'recall': Recall (macro)
        - 'f1': F1-Score (macro)
        - 'auc_roc': AUC-ROC (se y_proba fornecido)
    
    Examples
    --------
    >>> metricas = calcular_metricas_classificacao(y_test, y_pred, y_proba)
    >>> print(f"Acurácia: {metricas['accuracy']:.2%}")
    Acurácia: 95.00%
    
    Notes
    -----
    Para problemas multiclasse, as métricas são calculadas usando
    a estratégia 'macro', que computa a métrica para cada classe
    e retorna a média não ponderada.
    
    See Also
    --------
    sklearn.metrics.accuracy_score : Calcula acurácia
    sklearn.metrics.classification_report : Relatório completo
    """
    # Implementação...
    pass
```

### 3.4 Padrão de Visualizações

```python
def criar_figura_padrao(nrows=1, ncols=1, figsize=None, titulo_geral=None):
    """Cria figura com estilo padronizado."""
    if figsize is None:
        figsize = (6 * ncols, 5 * nrows)
    
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    
    if titulo_geral:
        fig.suptitle(titulo_geral, fontsize=16, fontweight='bold', y=1.02)
    
    return fig, axes


# Paleta de cores padrão
CORES = {
    'primaria': '#2E86AB',      # Azul
    'secundaria': '#A23B72',    # Rosa
    'sucesso': '#4ECDC4',       # Verde água
    'alerta': '#F18F01',        # Laranja
    'erro': '#C73E1D',          # Vermelho
    'neutro': '#6C757D',        # Cinza
    'destaque': '#FFE66D',      # Amarelo
}

PALETA_CATEGORICA = ['#2E86AB', '#A23B72', '#4ECDC4', '#F18F01', '#C73E1D', '#6C757D']
PALETA_SEQUENCIAL = 'Blues'
PALETA_DIVERGENTE = 'RdYlBu_r'
```

### 3.5 Padrão de Output/Resultados

```python
# Para resultados importantes, usar formatação destacada
print("═" * 60)
print("📊 RESULTADOS DO MODELO")
print("═" * 60)
print(f"   Acurácia:  {accuracy:.2%}")
print(f"   Precisão:  {precision:.2%}")
print(f"   Recall:    {recall:.2%}")
print(f"   F1-Score:  {f1:.2%}")
print("═" * 60)

# Para tabelas comparativas
print(f"\n{'Modelo':<25} {'Treino':>12} {'Teste':>12} {'Tempo':>10}")
print("─" * 60)
for nome, resultado in resultados.items():
    print(f"{nome:<25} {resultado['treino']:>12.2%} {resultado['teste']:>12.2%} {resultado['tempo']:>10.2f}s")
```

---

## 4. Datasets Recomendados

### 4.1 Repositórios de Dados

| Repositório | URL | Descrição |
|-------------|-----|-----------|
| **UCI ML Repository** | https://archive.ics.uci.edu/ml | Clássicos de ML |
| **Kaggle Datasets** | https://www.kaggle.com/datasets | Variedade enorme |
| **Scikit-learn** | Built-in | Datasets toy e reais |
| **Seaborn** | Built-in | Datasets para visualização |
| **OpenML** | https://www.openml.org | Benchmark datasets |
| **Google Dataset Search** | https://datasetsearch.research.google.com | Agregador |
| **Data.gov** | https://data.gov | Dados governamentais EUA |
| **Brasil.io** | https://brasil.io/datasets | Dados brasileiros |
| **IBGE** | https://www.ibge.gov.br | Dados demográficos BR |

### 4.2 Datasets por Tópico

#### Fundamentos (Nível 1)
| Dataset | Fonte | Uso | Tamanho |
|---------|-------|-----|---------|
| Iris | sklearn | Classificação intro | 150 |
| Tips | seaborn | Estatística, visualização | 244 |
| Titanic | seaborn/kaggle | EDA, classificação | 891 |
| Boston Housing* | sklearn | Regressão intro | 506 |
| California Housing | sklearn | Regressão | 20,640 |
| Gapminder | plotly | Visualização | ~1,700 |
| MPG | seaborn | Regressão | 398 |
| Penguins | seaborn | Alternativa ao Iris | 344 |
| Diamonds | seaborn | Regressão, EDA | 53,940 |

*Boston Housing tem issues éticos; usar California Housing como alternativa.

#### Core ML (Nível 2)
| Dataset | Fonte | Uso | Tamanho |
|---------|-------|-----|---------|
| Wine | sklearn | Classificação multiclasse | 178 |
| Breast Cancer | sklearn | Classificação binária | 569 |
| Digits | sklearn | Classificação imagens | 1,797 |
| Heart Disease | UCI/Kaggle | Classificação médica | 303 |
| Adult Income | UCI | Classificação, desbalanceamento | 48,842 |
| Credit Card Fraud | Kaggle | Classes desbalanceadas | 284,807 |
| Ames Housing | Kaggle | Regressão avançada | 1,460 |
| Customer Churn | Kaggle | Classificação negócios | ~7,000 |

#### Avançado (Nível 3)
| Dataset | Fonte | Uso | Tamanho |
|---------|-------|-----|---------|
| MNIST | keras/sklearn | Deep learning intro | 70,000 |
| Fashion MNIST | keras | CNN | 70,000 |
| CIFAR-10 | keras | CNN avançado | 60,000 |
| IMDB Reviews | keras | NLP, sentiment | 50,000 |
| 20 Newsgroups | sklearn | NLP, classificação texto | 18,846 |
| Airline Passengers | seaborn | Séries temporais | 144 |
| Walmart Sales | Kaggle | Séries temporais | ~400,000 |

### 4.3 Template de Carregamento de Dados

```python
# ============================================================
# CARREGAMENTO DO DATASET
# ============================================================

def carregar_dataset_nome(caminho=None):
    """
    Carrega o dataset [Nome] para análise.
    
    O dataset contém informações sobre [descrição breve].
    
    Fonte: [URL da fonte]
    Licença: [Tipo de licença]
    
    Parameters
    ----------
    caminho : str, optional
        Caminho local para o arquivo. Se None, baixa da internet.
    
    Returns
    -------
    pd.DataFrame
        DataFrame com os dados carregados.
    
    Notes
    -----
    Colunas do dataset:
    - coluna1: descrição
    - coluna2: descrição
    - target: variável alvo
    """
    if caminho:
        df = pd.read_csv(caminho)
    else:
        url = "https://..."
        df = pd.read_csv(url)
    
    return df


# Exemplo de uso
df = carregar_dataset_nome()

print("📊 Dataset: [Nome]")
print(f"   Fonte: [URL]")
print(f"   Shape: {df.shape}")
print(f"   Período: [se aplicável]")
print(f"\n📋 Colunas:")
for col in df.columns:
    print(f"   • {col}: {df[col].dtype}")
```

---

## 5. Padrões de Conteúdo Teórico

### 5.1 Explicação de Conceitos

```markdown
### [Nome do Conceito]

#### O que é?
[Definição clara e concisa em 2-3 frases]

#### Analogia
[Comparação com algo do mundo real que o aluno conhece]

#### Intuição Matemática
[Explicação da fórmula com interpretação de cada termo]

$$\text{fórmula} = \frac{\text{numerador}}{\text{denominador}}$$

Onde:
- $\text{termo}_1$: significado
- $\text{termo}_2$: significado

#### Visualização
[Gráfico ou diagrama que ilustra o conceito]

#### Quando usar?
- Situação 1
- Situação 2

#### Quando NÃO usar?
- Situação 1
- Situação 2

#### Exemplo Prático
[Código demonstrando o conceito]
```

### 5.2 Caixas de Destaque (Markdown)

```markdown
> 💡 **Dica:** Texto da dica importante que ajuda o aprendizado.

> ⚠️ **Atenção:** Alerta sobre algo que pode dar errado ou causar confusão.

> 📖 **Teoria:** Explicação teórica mais profunda para quem quer se aprofundar.

> ✅ **Boa Prática:** Recomendação de como fazer corretamente.

> ❌ **Erro Comum:** Descrição de um erro frequente e como evitar.

> 🔗 **Saiba Mais:** Link ou referência para aprofundamento.
```

### 5.3 Diagramas ASCII

```markdown
Para conceitos que precisam de diagramas, usar ASCII art:

```
Pipeline de ML:
┌─────────┐   ┌─────────────┐   ┌─────────┐   ┌──────────┐   ┌───────────┐
│  Dados  │ → │ Pré-process │ → │ Treino  │ → │ Avaliação│ → │  Deploy   │
└─────────┘   └─────────────┘   └─────────┘   └──────────┘   └───────────┘
```

Bias-Variance Tradeoff:
```
    Error
      │
      │   Total Error
      │   ╲
      │    ╲    ╱
      │     ╲  ╱
      │      ╲╱     Variance
      │      /╲
      │     /  ╲
      │    /    ────── Bias²
      │   /
      └───────────────────────
         Simple    Complex
          Model Complexity
```
```

---

## 6. Exercícios e Desafios

### 6.1 Estrutura de Exercícios

```markdown
## 🏆 Exercícios Práticos

### Exercício 1: [Título] (Nível: ⭐)

**Objetivo:** [O que o aluno deve conseguir fazer]

**Contexto:** [Breve descrição do problema]

**Tarefas:**
1. [Tarefa específica 1]
2. [Tarefa específica 2]
3. [Tarefa específica 3]

**Dica:** [Hint que ajuda sem entregar a resposta]

<details>
<summary>🔍 Ver Solução</summary>

```python
# Código da solução
```

**Explicação:** [Por que essa é a solução correta]

</details>

---

### Exercício 2: [Título] (Nível: ⭐⭐)
...

### Desafio: [Título] (Nível: ⭐⭐⭐)

**Descrição:** [Problema mais aberto, sem solução única]

**Critérios de sucesso:**
- [ ] Critério 1
- [ ] Critério 2
- [ ] Critério 3

**Não há solução única!** Compare sua abordagem com colegas.
```

### 6.2 Níveis de Dificuldade

| Nível | Símbolo | Descrição |
|-------|---------|-----------|
| Básico | ⭐ | Aplicação direta do que foi ensinado |
| Intermediário | ⭐⭐ | Requer combinação de conceitos |
| Avançado | ⭐⭐⭐ | Requer pesquisa adicional ou criatividade |

---

## 7. Checklist de Qualidade

### 7.1 Antes de Finalizar

```markdown
## Checklist do Notebook

### Estrutura
- [ ] Título e subtítulo claros
- [ ] Índice com âncoras funcionando
- [ ] Objetivos de aprendizagem definidos
- [ ] Seções bem organizadas e numeradas
- [ ] Resumo e próximos passos ao final

### Conteúdo Teórico
- [ ] Conceitos explicados com analogias
- [ ] Fórmulas matemáticas com interpretação
- [ ] Visualizações que reforçam a teoria
- [ ] Conexões com notebooks anteriores
- [ ] Erros comuns documentados

### Código
- [ ] Imports organizados e documentados
- [ ] Seed definido para reprodutibilidade
- [ ] Funções documentadas (docstrings)
- [ ] Código comentado em pontos-chave
- [ ] Outputs formatados e legíveis
- [ ] Sem erros de execução (kernel restart + run all)

### Dados
- [ ] Fonte do dataset documentada
- [ ] EDA básica realizada
- [ ] Dados explicados contextualmente
- [ ] Download automático ou instruções claras

### Exercícios
- [ ] Mínimo 3 exercícios práticos
- [ ] Níveis de dificuldade variados
- [ ] Soluções com explicações
- [ ] Pelo menos 1 desafio aberto

### Acessibilidade
- [ ] Texto alternativo para imagens importantes
- [ ] Não depender apenas de cores para informação
- [ ] Linguagem clara e inclusiva

### Metadados
- [ ] Tempo estimado realista
- [ ] Pré-requisitos listados
- [ ] Referências bibliográficas
- [ ] Versões das bibliotecas documentadas
```

### 7.2 Teste Final

```python
# Executar no final de cada notebook para validação
def validar_notebook():
    """Validações básicas do notebook."""
    import sys
    
    checks = {
        "Python >= 3.8": sys.version_info >= (3, 8),
        "NumPy importado": 'numpy' in dir(),
        "Pandas importado": 'pandas' in dir(),
        "Matplotlib importado": 'matplotlib' in dir(),
        "Random state definido": 'RANDOM_STATE' in dir(),
    }
    
    print("🔍 Validação do Notebook:")
    for check, passou in checks.items():
        status = "✅" if passou else "❌"
        print(f"   {status} {check}")
    
    if all(checks.values()):
        print("\n✅ Notebook válido!")
    else:
        print("\n⚠️ Corrija os itens marcados com ❌")

validar_notebook()
```

---

## 8. Referências e Recursos

### 8.1 Template de Referências

```markdown
## 📚 Referências

### Livros
1. **[Título do Livro]** - Autor (Ano). Editora. Capítulos X-Y.
   - [Breve descrição do que o livro cobre]

### Papers
1. Autor et al. (Ano). "[Título do Paper](link)". *Conferência/Journal*.
   - [Por que esse paper é relevante]

### Documentação Oficial
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

### Cursos e Tutoriais
- [Nome do Curso](link) - Plataforma
- [Nome do Tutorial](link) - Autor

### Notebooks Relacionados
- [Notebook Anterior](link) - Pré-requisito
- [Notebook Seguinte](link) - Continuação
```

### 8.2 Livros Recomendados por Nível

| Nível | Livro | Autor |
|-------|-------|-------|
| Fundamentos | "Python for Data Analysis" | Wes McKinney |
| Fundamentos | "Think Stats" | Allen B. Downey |
| Core ML | "Hands-On Machine Learning" | Aurélien Géron |
| Core ML | "Introduction to Statistical Learning" | James et al. |
| Avançado | "Deep Learning" | Goodfellow et al. |
| Avançado | "Pattern Recognition and ML" | Bishop |

---

## 9. Versionamento

### 9.1 Convenção de Nomes

```
[nivel]_[numero]_[titulo_snake_case]_v[versao].ipynb

Exemplos:
- 1_1_fundamentos_python_data_science_v1.0.ipynb
- 2_1_classificacao_completa_v1.2.ipynb
- 4_1_intro_redes_neurais_pytorch_v2.0.ipynb
```

### 9.2 Changelog no Notebook

```markdown
## Histórico de Versões

| Versão | Data | Alterações |
|--------|------|------------|
| 1.0 | 2025-01-01 | Versão inicial |
| 1.1 | 2025-01-15 | Adicionado exercício 4, corrigido bug na célula 23 |
| 1.2 | 2025-02-01 | Atualizado para sklearn 1.4, nova visualização na seção 5 |
```

---

## 10. Exemplo de Aplicação do Padrão

Veja o notebook `tutorial_completo_classificacao_ml.ipynb` como referência de implementação deste padrão.

---

**Documento mantido por:** [Guilherme Favaron/ MindApps]  
**Última revisão:** Janeiro 2025
