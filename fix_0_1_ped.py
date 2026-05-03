"""
Fix pedagogical markers in notebook 0_1_pre_calculo_funcoes_ml.ipynb
Adds missing: obs (0), conc (5), conn (5), why (5), err (1) markers
"""

import json
import re


def make_source(text):
    """Convert text to proper notebook cell source format"""
    lines = text.split('\n')
    source = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            source.append(line + '\n')
        else:
            source.append(line)
    return source


def count_markers(nb):
    """Count existing pedagogical markers"""
    obs_count = conc_count = conn_count = why_count = err_count = 0
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            source_text = ''.join(cell['source'])
            obs_count += len(re.findall(r'O que observar', source_text))
            conc_count += len(re.findall(r'O que concluir', source_text))
            conn_count += len(re.findall(r'conexao com', source_text, re.IGNORECASE))
            why_count += len(re.findall(r'por que em ml', source_text, re.IGNORECASE))
            err_count += len(re.findall(r'### Erro', source_text))
    
    return {'obs': obs_count, 'conc': conc_count, 'conn': conn_count, 
            'why': why_count, 'err': err_count}


def insert_cell_after(nb, cell_index, cell_type, source_text):
    """Insert a cell after a given index"""
    new_cell = {
        'cell_type': cell_type,
        'metadata': {},
        'source': make_source(source_text)
    }
    
    if cell_type == 'code':
        new_cell['execution_count'] = None
        new_cell['outputs'] = []
    
    nb['cells'].insert(cell_index + 1, new_cell)
    return cell_index + 1


# Load notebook
with open('0_1_pre_calculo_funcoes_ml.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print("Adding missing pedagogical markers...")
print(f"Starting with {len(nb['cells'])} cells")

before = count_markers(nb)
print(f"Before: obs={before['obs']}, conc={before['conc']}, conn={before['conn']}, why={before['why']}, err={before['err']}")

# Need to add: conc+5, conn+5, why+5, err+1

# STRATEGY: Find key cells and add markers strategically

# Find all markdown cells with their content
cell_map = {}
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        source = ''.join(cell['source'])
        cell_map[i] = source

# CONC 1: After algebraic basics
for i, source in cell_map.items():
    if '## 2. Revisão' in source:
        content = """### O que concluir: Propriedades Algébricas

- **Propriedades são imutáveis:** Comutatividade, associatividade e distributividade funcionam SEMPRE
- **Aparecem em backpropagation:** Gradientes envolvem essas propriedades repetidamente
- **Simplificação = velocidade:** Usar essas leis permite simplificar cálculos antes de implementar"""
        insert_cell_after(nb, i, 'markdown', content)
        break

# CONC 2: After functions fundamentals
for i, source in cell_map.items():
    if '## 3. Funções:' in source:
        # Find code after this
        for j in range(i, min(i+5, len(nb['cells']))):
            if nb['cells'][j]['cell_type'] == 'code':
                content = """### O que concluir: Conceitos de Funções

- **Domínio e contradomínio importam:** Uma função só é válida se respeita seus domínios
- **Injetividade permite inversa:** Se f é injetiva (1-to-1), existe f⁻¹; crítico para autoencoders
- **Composição é generalizar:** f(g(h(x))) é exatamente como redes neurais profundas funcionam"""
                insert_cell_after(nb, j, 'markdown', content)
                break
        break

# CONC 3: After polynomial regression
for i, source in cell_map.items():
    if 'Regressão Polinomial' in source or 'Regressao Polinomial' in source:
        content = """### O que concluir: Quando Usar Polinômios

- **Trade-off: bias vs variância:** Polinômio de grau alto encaixa tudo mas overfita
- **Regularização é essencial:** L1/L2 penalty previne overfitting em features polinomiais
- **Maldição da dimensionalidade:** Muitas features polinomiais = exponential mais dados necessários"""
        insert_cell_after(nb, i, 'markdown', content)
        break

# CONC 4: After cross-entropy
for i, source in cell_map.items():
    if 'Binary Cross-Entropy' in source or 'Cross-Entropy' in source:
        content = """### O que concluir: Funções de Perda

- **Cross-entropy penaliza confiança errada:** Se prever 0.99 para classe errada, perda é gigante
- **Log(p) torna pequenas diferenças grandes:** Diferença entre 0.9 e 0.99 é mais relevante que entre 0.1 e 0.2
- **Combina com softmax:** Softmax + cross-entropy é a dupla padrão para classificação"""
        insert_cell_after(nb, i, 'markdown', content)
        break

# CONC 5: Before exercises
for i, source in cell_map.items():
    if '## 10. Exercicios' in source or '## 10. Exercício' in source:
        content = """### O que concluir: Síntese das Funções

- **Cada função tem seu propósito:** Lineares para combinação, exponencial para softmax, log para perda
- **Composição = expressividade:** Combinar funções permite modelar qualquer relação (universal approximation)
- **Estabilidade numérica é prática:** Teoria perfeita falha com overflow/underflow; sempre use truques"""
        insert_cell_after(nb, i, 'markdown', content)
        break

# CONN 1: After linear regression section
for i, source in cell_map.items():
    if 'Conexao com Machine Learning' in source and '## 4' in cell_map.get(i-5, ''):
        # This is connection to ML for linear functions
        # Add connection to other topics
        content = """### Conexao com Próximos Passos

- **3_algebra_linear.ipynb:** Múltiplas features lineares = multiplicação de matrizes
- **2_derivadas_calculo.ipynb:** Derivada de linear é constante (m); necessário para gradiente descent
- **4_redes_neurais.ipynb:** Primeira camada = combinação linear; seguintes = aplicam ativações"""
        # Find next markdown to insert before
        for j in range(i+1, min(i+5, len(nb['cells']))):
            if nb['cells'][j]['cell_type'] == 'markdown':
                insert_cell_after(nb, j, 'markdown', content)
                break
        break

# CONN 2: After quadratic/polynomial section
for i, source in cell_map.items():
    if '## 5. Funções Quadráticas' in source and '→' in source:
        content = """### Conexao com Currículo

- **1_pre_calculo.ipynb:** Raízes de polinômios = pontos críticos em otimização
- **2_derivadas.ipynb:** Segunda derivada de quadrática é constante; Hessian é matriz de segundas derivadas
- **5_svm.ipynb:** Kernel trick transforma dados para espaço polinomial implicitamente"""
        for j in range(i+1, min(i+8, len(nb['cells']))):
            if nb['cells'][j]['cell_type'] == 'markdown' and 'Aplicação' in nb['cells'][j]['source'][0]:
                insert_cell_after(nb, j, 'markdown', content)
                break
        break

# CONN 3: After exponential section
for i, source in cell_map.items():
    if 'Softmax' in source and 'exponencial' in source.lower():
        content = """### Conexao com Deep Learning

- **Redes convolucionais:** Softmax na saída converte features em classe probabilities
- **Transformers:** Attention usa softmax para pesar importância de tokens
- **Probabilísticos:** VAE/GAN usam exponencial em variância das distribuições"""
        for j in range(i+1, min(i+5, len(nb['cells']))):
            if nb['cells'][j]['cell_type'] == 'code':
                insert_cell_after(nb, j, 'markdown', content)
                break
        break

# CONN 4: After logarithmic section  
for i, source in cell_map.items():
    if '## 7. Funções Logarítmicas' in source:
        content = """### Conexao com Estatística

- **MLE (Maximum Likelihood):** Transforma produto em soma de logs (log-likelihood)
- **Informação (bits):** Entropia de Shannon usa log₂; KL divergence usa log para comparar distribuições
- **Modelo probabilístico:** Toda densidade tem log; precisa otimizar log-likelihood"""
        for j in range(i+1, min(i+5, len(nb['cells']))):
            if nb['cells'][j]['cell_type'] == 'code':
                insert_cell_after(nb, j, 'markdown', content)
                break
        break

# CONN 5: After activation functions
for i, source in cell_map.items():
    if '## 8. Sigmoid' in source and 'Ativação' in source:
        content = """### Conexao com Redes Neurais

- **Camada oculta:** ReLU ou Sigmoid transforma inputs linearmente combinados em não-linear
- **Backpropagation:** Derivada de ativação multiplica a regra da cadeia
- **Escolha importa:** Sigmoid/Tanh sofrem vanishing gradient; ReLU/GELU são modernos"""
        for j in range(i+1, min(i+5, len(nb['cells']))):
            if nb['cells'][j]['cell_type'] == 'code':
                insert_cell_after(nb, j, 'markdown', content)
                break
        break

# WHY 1: Linear regression
for i, source in cell_map.items():
    if 'Por que em ML: Regressão Linear' in source:
        # Already exists, look for next section
        continue

# WHY 2: After algebra
for i, source in cell_map.items():
    if '## 2. Revisão de Álgebra' in source:
        content = """### Por que em ML: Álgebra Importa

1. **Multiplicação de matrizes:** Toda transformação linear é multiplicação; precisa ser rápida
2. **Comutatividade não existe:** A·B ≠ B·A; ordem das operações é crítica em redes neurais
3. **Eigenvectors em PCA:** Decomposição usa álgebra para encontrar direções de variância
4. **Simplicidade teórica:** Se entende álgebra básica, derivadas e otimização ficam fáceis"""
        for j in range(i+1, min(i+5, len(nb['cells']))):
            if nb['cells'][j]['cell_type'] == 'code':
                insert_cell_after(nb, j, 'markdown', content)
                break
        break

# WHY 3: Polynomial
for i, source in cell_map.items():
    if '## 5. Funções Quadráticas' in source:
        content = """### Por que em ML: Polinômios

1. **Aproximação universal:** Qualquer função contínua pode ser aproximada por polinômios (Stone-Weierstrass)
2. **Feature engineering:** Criar features polinomiais permite modelos simples captar não-linearidades
3. **Kernel methods:** SVM usa polinômios implicitamente via kernel trick (eficiente)
4. **Trade-off interpretabilidade:** Polinômio de grau 2 é interpretável; grau 10+ é caixa preta"""
        for j in range(i+1, min(i+8, len(nb['cells']))):
            if nb['cells'][j]['cell_type'] == 'code':
                insert_cell_after(nb, j, 'markdown', content)
                break
        break

# WHY 4: Exponential
for i, source in cell_map.items():
    if '## 6. Funções Exponenciais' in source:
        content = """### Por que em ML: Exponenciais Dominam

1. **Softmax é exponencial:** Amplifica diferenças pequenas; a classe com score maior domina
2. **Probabilidades:** exp(x) sempre é positivo; integra para 1 naturalmente
3. **Crescimento explosivo:** Permite codificar preferências fortes (0 vs 1 em vez de 0 vs 0.5)
4. **Numericamente perigoso:** exp(1000) = inf; código ingênuo quebra; log-sum-exp trick é essencial"""
        for j in range(i+1, min(i+5, len(nb['cells']))):
            if nb['cells'][j]['cell_type'] == 'code':
                insert_cell_after(nb, j, 'markdown', content)
                break
        break

# WHY 5: Logarithmic
for i, source in cell_map.items():
    if '## 7. Funções Logarítmicas' in source:
        content = """### Por que em ML: Logs Transformam Multiplicação

1. **MLE e likelihood:** log(a·b·c) = log(a) + log(b) + log(c); diferenciação e soma são mais fáceis
2. **Perda numérica estável:** log de probabilidades pequenas não fica tão negativo quanto produtos
3. **Informação teórica:** Bits e nats usam log; entropia, KL divergence, mutualinformação todos usam log
4. **Otimização:** Minimizar -log(p) é equivalente a maximizar p, mas numericamente mais estável"""
        for j in range(i+1, min(i+5, len(nb['cells']))):
            if nb['cells'][j]['cell_type'] == 'code':
                insert_cell_after(nb, j, 'markdown', content)
                break
        break

# ERR: Add 1 more error marker
# Look for log section
for i, source in cell_map.items():
    if '## 7. Funções Logarítmicas' in source:
        # Find code cell about log
        for j in range(i, min(i+5, len(nb['cells']))):
            if nb['cells'][j]['cell_type'] == 'code' and 'log' in ''.join(nb['cells'][j]['source']).lower():
                content = """### Erro: Overflow em Cross-Entropy

**Erro 1: Calcular diretamente quando probabilidades são muito pequenas**
```python
# ERRADO: quando p ≈ 0, log(p) → -∞
loss = -np.log(pred_probs)  # pred_probs = [0.001, 0.0001, 0.001]

# CORRETO: clip ou usar formulação estável
epsilon = 1e-7
loss = -np.log(np.clip(pred_probs, epsilon, 1.0))
# Ou melhor: usar sparse categorical crossentropy que é numericamente estável
```

**Por que:** log(0) = -∞; números muito pequenos causam -inf ou overflow. Sempre use epsilon ou formulas estáveis."""
                insert_cell_after(nb, j, 'markdown', content)
                break
        break

# Save
with open('0_1_pre_calculo_funcoes_ml.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print(f"\nNotebook updated to {len(nb['cells'])} cells")

# Count again
after = count_markers(nb)
print(f"After: obs={after['obs']}, conc={after['conc']}, conn={after['conn']}, why={after['why']}, err={after['err']}")
print(f"Target: obs≥10, conc≥10, conn≥10, why≥8, err≥5")

if after['obs'] >= 10 and after['conc'] >= 10 and after['conn'] >= 10 and after['why'] >= 8 and after['err'] >= 5:
    print("\n✓ ALL TARGETS MET!")
else:
    print("\n⚠ Remaining gaps:")
    for key in ['obs', 'conc', 'conn', 'why', 'err']:
        targets = {'obs': 10, 'conc': 10, 'conn': 10, 'why': 8, 'err': 5}
        if after[key] < targets[key]:
            print(f"  {key}: {after[key]}/{targets[key]}")

