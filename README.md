# Currículo de Machine Learning em Produção

Conjunto de 4 notebooks Jupyter educacionais em português cobrindo os tópicos fundamentais de MLOps e Deploy de modelos.

## Notebooks

### 1. 6_1_Deploy_de_Modelos_ML.ipynb
Aprenda a transformar um protótipo em produção.

**Tópicos:**
- Desafios de deploy e checklist de produção
- Serialização (joblib vs pickle)
- ONNX para portabilidade
- FastAPI para criar APIs
- Docker para containerização
- Testes e CI/CD
- Cloud deployment
- Monitoramento básico

**Exercícios:** 6 práticos

### 2. 6_2_MLflow_e_Experiment_Tracking.ipynb
Rastreie e compare experimentos como um profissional.

**Tópicos:**
- Por que experiment tracking é essencial
- MLflow: Tracking, Projects, Models, Registry
- Logging de parâmetros e métricas
- Reproducibilidade com MLproject
- Model Registry para versionamento
- Autologging com múltiplos frameworks
- Alternativas (W&B, Neptune, ClearML)

**Exercícios:** 6 práticos

### 3. 6_3_Monitoramento_e_Data_Drift.ipynb
Detecte quando seu modelo está degradando.

**Tópicos:**
- Data Drift vs Concept Drift vs Model Decay
- Métricas: PSI, KL divergence, KS test
- Implementação com Evidently
- Alertas e thresholds
- Estratégias de retraining
- Logging estruturado (JSON)
- Dashboards de monitoramento

**Exercícios:** 6 práticos

### 4. 6_4_Pipelines_de_ML_Automatizados.ipynb
Automatize todo seu workflow de ML.

**Tópicos:**
- CI/CD para ML (diferenças do software tradicional)
- Testes: data, modelo, integração, performance
- Orquestração: Airflow, Prefect
- Feature Stores (Feast)
- Sklearn Pipelines avançados
- Pipeline end-to-end
- DVC para versionamento
- Boas práticas MLOps
- Infrastructure as Code (Terraform)

**Exercícios:** 6 práticos

## Estrutura dos Notebooks

Cada notebook contém:

1. Introdução teórica
2. Conceitos fundamentais
3. Implementação prática
4. Exemplos do mundo real
5. Alternativas e comparações
6. Exercícios práticos

## Características Técnicas

- Markdown em Português: Todos os textos explicativos
- Código em Inglês: Variáveis, funções, comentários
- Código Real: Exemplos práticos que funcionam
- Sem Em-dash: Apenas hífens duplos (--) onde apropriado

## Bibliotecas Utilizadas

- numpy, pandas, scikit-learn
- fastapi, joblib, pickle, onnx
- mlflow
- evidently, scipy
- Docker, Terraform (exemplos)

## Quick Start

Pré-requisitos: Python 3.7+, Jupyter Notebook

Instalação:
```bash
pip install numpy pandas scikit-learn matplotlib scipy
```

Executar:
```bash
jupyter notebook
```

Abra qualquer notebook .ipynb para começar!

---

**Criado em:** 2026-03-08
**Total de Células:** 91
**Notebooks:** 4

Comece agora!
