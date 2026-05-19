# Math & Statistics for AI

Curriculo educacional em portugues para estudar matematica, estatistica, machine learning, deep learning, dominios aplicados e MLOps com notebooks Jupyter executaveis.

## Estado Atual

- **Notebooks:** 54
- **Celulas:** 2718 (1784 markdown, 934 codigo)
- **Organizacao:** notebooks separados por modulo em `notebooks/`; o modulo 05 agrupa submodulos 05A, 05B, 05C e 05D.
- **Validacao:** `python3 tools/validate_notebooks.py` checa JSON, cabecalho padrao, metadados, referencias internas `.ipynb`, sintaxe Python das celulas e vazamento de caminhos temporarios.
- **Exercicios:** prompts usam `TAREFA DO ALUNO`; celulas de solucao sao marcadas com tag `solution`.

## Estrutura

| Modulo | Pasta | Notebooks | Descricao |
|---|---:|---:|---|
| 00 - Matematica | `notebooks/00-matematica` | 8 | Base matematica para algoritmos de ML. |
| 01 - Estatistica | `notebooks/01-estatistica` | 5 | Estatistica descritiva, inferencial, bayesiana e experimental. |
| 02 - Data Science | `notebooks/02-data-science` | 4 | Python, EDA, SQL, APIs e bancos de dados. |
| 03 - Machine Learning | `notebooks/03-machine-learning` | 7 | Modelos classicos supervisionados e nao-supervisionados. |
| 04 - Deep Learning | `notebooks/04-deep-learning` | 6 | Redes neurais, treinamento, transfer learning e performance. |
| 05 - Dominios Aplicados | `notebooks/05-dominios-aplicados` | 20 | Modulo agregador para visao computacional, NLP, IA generativa e series temporais. |
| 06 - MLOps | `notebooks/06-mlops` | 4 | Deploy, tracking, monitoramento, drift e pipelines. |

### Submodulos do Modulo 05

| Submodulo | Pasta | Notebooks | Descricao |
|---|---:|---:|---|
| 05A - Computer Vision | `notebooks/05-dominios-aplicados/05A-computer-vision` | 5 | CNNs, classificacao, deteccao, segmentacao e ViTs. |
| 05B - NLP | `notebooks/05-dominios-aplicados/05B-nlp` | 6 | NLP classico, embeddings, RNNs, Transformers, LLMs e RAG. |
| 05C - Generative AI | `notebooks/05-dominios-aplicados/05C-generative-ai` | 5 | GANs, VAEs, diffusion, fine-tuning e IA multimodal. |
| 05D - Series Temporais | `notebooks/05-dominios-aplicados/05D-series-temporais` | 4 | Fundamentos, ARIMA/Prophet, ML e deep learning temporal. |

## Como Usar

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt (para CPU) ou requirements-gpu.txt (para GPU CUDA 12.1)
jupyter lab notebooks
```

Para uma checagem rapida sem instalar o stack cientifico completo:

```bash
python3 tools/validate_notebooks.py
```

## Catalogo dos Notebooks

### 00 - Matematica

| Notebook | Celulas | Descricao |
|---|---:|---|
| [`0_1_pre_calculo_funcoes_ml.ipynb`](notebooks/00-matematica/0_1_pre_calculo_funcoes_ml.ipynb) | 100 | Revisao de funcoes, algebra basica, exponenciais, logaritmos e ativacoes usadas em ML. |
| [`0_2_algebra_linear_vetores.ipynb`](notebooks/00-matematica/0_2_algebra_linear_vetores.ipynb) | 50 | Vetores, produto interno, normas, distancias, similaridade e projecoes aplicadas a ML. |
| [`0_3_algebra_linear_matrizes.ipynb`](notebooks/00-matematica/0_3_algebra_linear_matrizes.ipynb) | 101 | Matrizes, transformacoes lineares, sistemas, autovalores, PCA, SVD e recomendacao. |
| [`0_4_calculo_derivadas.ipynb`](notebooks/00-matematica/0_4_calculo_derivadas.ipynb) | 108 | Limites, derivadas, gradientes, Jacobiano, Hessiano, gradient descent e backpropagation. |
| [`0_5_calculo_integrais_series.ipynb`](notebooks/00-matematica/0_5_calculo_integrais_series.ipynb) | 113 | Integrais, series, metodos numericos, AUC, Taylor, Monte Carlo e conexoes com probabilidade. |
| [`0_6_probabilidade_fundamentos.ipynb`](notebooks/00-matematica/0_6_probabilidade_fundamentos.ipynb) | 63 | Eventos, probabilidade condicional, Bayes, variaveis aleatorias e distribuicoes fundamentais. |
| [`0_7_probabilidade_avancada.ipynb`](notebooks/00-matematica/0_7_probabilidade_avancada.ipynb) | 58 | Distribuicoes conjuntas, MLE, inferencia bayesiana, normal multivariada e GMM. |
| [`0_8_otimizacao_ml.ipynb`](notebooks/00-matematica/0_8_otimizacao_ml.ipynb) | 56 | Funcoes de custo, convexidade, GD, SGD, Momentum, AdaGrad, RMSprop, Adam e regularizacao. |

### 01 - Estatistica

| Notebook | Celulas | Descricao |
|---|---:|---|
| [`1_1_estatistica_descritiva.ipynb`](notebooks/01-estatistica/1_1_estatistica_descritiva.ipynb) | 47 | Medidas de tendencia, dispersao, outliers, visualizacoes e analise bivariada. |
| [`1_2_estatistica_inferencial.ipynb`](notebooks/01-estatistica/1_2_estatistica_inferencial.ipynb) | 45 | Amostragem, intervalos de confianca, testes, ANOVA, bootstrap e multiplos testes. |
| [`1_3_estatistica_bayesiana.ipynb`](notebooks/01-estatistica/1_3_estatistica_bayesiana.ipynb) | 43 | Priors, likelihood, posterior, modelos conjugados, Naive Bayes, MAP e regularizacao. |
| [`1_4_regressao_estatistica.ipynb`](notebooks/01-estatistica/1_4_regressao_estatistica.ipynb) | 42 | OLS, diagnostico de residuos, multicolinearidade, regularizacao e learning curves. |
| [`1_5_design_experimentos.ipynb`](notebooks/01-estatistica/1_5_design_experimentos.ipynb) | 38 | Randomizacao, poder estatistico, A/B testing, causalidade, DAGs e validacao temporal. |

### 02 - Data Science

| Notebook | Celulas | Descricao |
|---|---:|---|
| [`2_1_python_data_science.ipynb`](notebooks/02-data-science/2_1_python_data_science.ipynb) | 42 | NumPy, Pandas, visualizacao, limpeza, feature engineering e pipeline exploratorio. |
| [`2_2_eda_completa.ipynb`](notebooks/02-data-science/2_2_eda_completa.ipynb) | 42 | Framework de EDA, missing values, outliers, relacoes multivariadas e leakage. |
| [`2_3_sql_e_apis.ipynb`](notebooks/02-data-science/2_3_sql_e_apis.ipynb) | 42 | SQL, joins, window functions, REST APIs, paginacao, retry, JSON e scraping basico. |
| [`2_4_acesso_banco_dados.ipynb`](notebooks/02-data-science/2_4_acesso_banco_dados.ipynb) | 41 | SQLite, PostgreSQL, ORM, feature store, Parquet, pipelines e seguranca de dados. |

### 03 - Machine Learning

| Notebook | Celulas | Descricao |
|---|---:|---|
| [`3_1_classificacao_completa.ipynb`](notebooks/03-machine-learning/3_1_classificacao_completa.ipynb) | 51 | Regressao logistica, arvores, Random Forest, metricas, ROC, PR curve e validacao. |
| [`3_2_regressao_modelos.ipynb`](notebooks/03-machine-learning/3_2_regressao_modelos.ipynb) | 46 | Regressao linear, regularizacao, arvores, boosting, metricas e diagnostico de modelos. |
| [`3_3_arvores_ensemble.ipynb`](notebooks/03-machine-learning/3_3_arvores_ensemble.ipynb) | 41 | Decision trees, bagging, Random Forest, AdaBoost, Gradient Boosting e trade-offs. |
| [`3_4_svm_kernel.ipynb`](notebooks/03-machine-learning/3_4_svm_kernel.ipynb) | 40 | Margens, vetores de suporte, kernels, gamma, C e classificacao nao-linear. |
| [`3_5_clustering.ipynb`](notebooks/03-machine-learning/3_5_clustering.ipynb) | 38 | K-Means, DBSCAN, clustering hierarquico, GMM e avaliacao de clusters. |
| [`3_6_reducao_dimensionalidade.ipynb`](notebooks/03-machine-learning/3_6_reducao_dimensionalidade.ipynb) | 38 | Maldicao da dimensionalidade, PCA, t-SNE, UMAP, interpretacao e visualizacao. |
| [`3_0_tutorial_from_scratch.ipynb`](notebooks/03-machine-learning/3_0_tutorial_from_scratch.ipynb) | 53 | Fluxo completo de classificacao, da preparacao dos dados a avaliacao de modelos. |

### 04 - Deep Learning

| Notebook | Celulas | Descricao |
|---|---:|---|
| [`4_1_fundamentos_redes_neurais.ipynb`](notebooks/04-deep-learning/4_1_fundamentos_redes_neurais.ipynb) | 39 | Neuronios, ativacoes, perceptron, MLP, backpropagation e treinamento basico. |
| [`4_2_arquiteturas_deep.ipynb`](notebooks/04-deep-learning/4_2_arquiteturas_deep.ipynb) | 41 | CNNs, RNNs, Transformers, profundidade, conectividade e hierarquia de features. |
| [`4_3_treinamento_deep.ipynb`](notebooks/04-deep-learning/4_3_treinamento_deep.ipynb) | 39 | Inicializacao, otimizadores, regularizacao, normalizacao, schedules e diagnostico. |
| [`4_4_transfer_learning.ipynb`](notebooks/04-deep-learning/4_4_transfer_learning.ipynb) | 35 | Feature extraction, fine-tuning, congelamento de camadas e adaptacao de modelos. |
| [`4_5_aceleracao_hardware.ipynb`](notebooks/04-deep-learning/4_5_aceleracao_hardware.ipynb) | 35 | GPU, batching, precisao mista, memoria, paralelismo e otimizacao de treino. |
| [`4_6_otimizacao_python.ipynb`](notebooks/04-deep-learning/4_6_otimizacao_python.ipynb) | 35 | Profiling, vetorizacao, memoria, paralelismo e melhoria de performance em pipelines. |

### 05 - Dominios Aplicados

#### 05A - Computer Vision

| Notebook | Celulas | Descricao |
|---|---:|---|
| [`5A_1_cnn_fundamentos.ipynb`](notebooks/05-dominios-aplicados/05A-computer-vision/5A_1_cnn_fundamentos.ipynb) | 42 | Convolucao, pooling, feature maps, receptive field e blocos de CNNs. |
| [`5A_2_classificacao_imagens.ipynb`](notebooks/05-dominios-aplicados/05A-computer-vision/5A_2_classificacao_imagens.ipynb) | 35 | Dados de imagem, augmentations, desbalanceamento, avaliacao e interpretabilidade. |
| [`5A_3_deteccao_objetos.ipynb`](notebooks/05-dominios-aplicados/05A-computer-vision/5A_3_deteccao_objetos.ipynb) | 41 | Bounding boxes, IoU, NMS, anchor boxes, YOLO, R-CNN e metricas de deteccao. |
| [`5A_4_segmentacao.ipynb`](notebooks/05-dominios-aplicados/05A-computer-vision/5A_4_segmentacao.ipynb) | 38 | Segmentacao semantica, instance segmentation, panoptic segmentation, U-Net e metricas. |
| [`5A_5_vision_transformers.ipynb`](notebooks/05-dominios-aplicados/05A-computer-vision/5A_5_vision_transformers.ipynb) | 34 | Patches, self-attention visual, ViT, Swin, DETR e modelos vision-language. |

#### 05B - NLP

| Notebook | Celulas | Descricao |
|---|---:|---|
| [`5B_1_nlp_classico.ipynb`](notebooks/05-dominios-aplicados/05B-nlp/5B_1_nlp_classico.ipynb) | 37 | Tokenizacao, normalizacao, bag-of-words, TF-IDF, n-grams e classificacao classica. |
| [`5B_2_word_embeddings.ipynb`](notebooks/05-dominios-aplicados/05B-nlp/5B_2_word_embeddings.ipynb) | 31 | Word2Vec, GloVe, similaridade semantica, analogias e representacoes distribuidas. |
| [`5B_3_rnn_lstm_nlp.ipynb`](notebooks/05-dominios-aplicados/05B-nlp/5B_3_rnn_lstm_nlp.ipynb) | 38 | Sequencias, RNN, LSTM, GRU, vanishing gradients e tarefas NLP sequenciais. |
| [`5B_4_transformers_bert.ipynb`](notebooks/05-dominios-aplicados/05B-nlp/5B_4_transformers_bert.ipynb) | 36 | Self-attention, multi-head attention, positional encoding, BERT e fine-tuning. |
| [`5B_5_large_language_models.ipynb`](notebooks/05-dominios-aplicados/05B-nlp/5B_5_large_language_models.ipynb) | 48 | Scaling laws, prompting, zero-shot, few-shot, alinhamento e capacidades emergentes. |
| [`5B_6_rag_aplicacoes_llm.ipynb`](notebooks/05-dominios-aplicados/05B-nlp/5B_6_rag_aplicacoes_llm.ipynb) | 83 | Chunking, embeddings, busca vetorial, retrieval, geracao aumentada e avaliacao. |

#### 05C - Generative AI

| Notebook | Celulas | Descricao |
|---|---:|---|
| [`5C_1_gans.ipynb`](notebooks/05-dominios-aplicados/05C-generative-ai/5C_1_gans.ipynb) | 26 | Gerador, discriminador, treinamento adversarial, instabilidade e aplicacoes generativas. |
| [`5C_2_vaes.ipynb`](notebooks/05-dominios-aplicados/05C-generative-ai/5C_2_vaes.ipynb) | 52 | Encoder, decoder, espaco latente, ELBO, KL divergence, beta-VAE e interpolacao. |
| [`5C_3_diffusion_models.ipynb`](notebooks/05-dominios-aplicados/05C-generative-ai/5C_3_diffusion_models.ipynb) | 94 | Forward process, denoising, scheduler, sampling e fundamentos de diffusion models. |
| [`5C_4_finetuning_generativo.ipynb`](notebooks/05-dominios-aplicados/05C-generative-ai/5C_4_finetuning_generativo.ipynb) | 31 | Transfer learning, LoRA, adapters, datasets, avaliacao e riscos de overfitting. |
| [`5C_5_multimodal_ai.ipynb`](notebooks/05-dominios-aplicados/05C-generative-ai/5C_5_multimodal_ai.ipynb) | 81 | Representacoes multimodais, texto-imagem, audio, video, alinhamento e avaliacao. |

#### 05D - Series Temporais

| Notebook | Celulas | Descricao |
|---|---:|---|
| [`5D_1_series_temporais_fundamentos.ipynb`](notebooks/05-dominios-aplicados/05D-series-temporais/5D_1_series_temporais_fundamentos.ipynb) | 55 | Componentes temporais, estacionariedade, ACF, PACF, diferenciacao e suavizacao. |
| [`5D_2_arima_prophet.ipynb`](notebooks/05-dominios-aplicados/05D-series-temporais/5D_2_arima_prophet.ipynb) | 42 | ARIMA, SARIMA, Prophet, decomposicao, sazonalidade e validacao temporal. |
| [`5D_3_ml_series_temporais.ipynb`](notebooks/05-dominios-aplicados/05D-series-temporais/5D_3_ml_series_temporais.ipynb) | 85 | Lag features, rolling windows, validacao temporal, regressao e ensembles temporais. |
| [`5D_4_dl_series_temporais.ipynb`](notebooks/05-dominios-aplicados/05D-series-temporais/5D_4_dl_series_temporais.ipynb) | 81 | RNN, LSTM, GRU, TCN, Transformers e previsao sequencial multi-step. |

### 06 - MLOps

| Notebook | Celulas | Descricao |
|---|---:|---|
| [`6_1_deploy_modelos.ipynb`](notebooks/06-mlops/6_1_deploy_modelos.ipynb) | 31 | Serializacao, API, contratos, versionamento, health checks e preparacao para producao. |
| [`6_2_mlflow_tracking.ipynb`](notebooks/06-mlops/6_2_mlflow_tracking.ipynb) | 28 | Experimentos, parametros, metricas, artifacts, model registry e comparacao de runs. |
| [`6_3_monitoramento_drift.ipynb`](notebooks/06-mlops/6_3_monitoramento_drift.ipynb) | 40 | Data drift, concept drift, PSI, KS test, thresholds, alertas e retraining. |
| [`6_4_pipelines_automatizados.ipynb`](notebooks/06-mlops/6_4_pipelines_automatizados.ipynb) | 47 | CI/CD, testes, orquestracao, feature stores, DVC e pipelines end-to-end. |

## Politica de Exercicios

Os notebooks combinam aula, pratica guiada e solucoes executaveis. Para evitar confusao entre material incompleto e exercicio intencional:

- Enunciados usam a expressao `TAREFA DO ALUNO`, nao marcadores genericos de backlog.
- Celulas de pratica recebem tag `exercise`.
- Celulas com implementacao de referencia recebem tag `solution`.
- O validador falha se encontrar marcadores genericos de backlog, sintaxe Python invalida, referencias internas quebradas ou caminhos temporarios de geracao.

## Desenvolvimento e Qualidade

- `requirements.txt (para CPU) ou requirements-gpu.txt (para GPU CUDA 12.1)` contem as bibliotecas usadas nos notebooks e inclui Jupyter.
- `.github/workflows/validate.yml` executa a validacao leve em push e pull request.
- `.gitignore` exclui caches, ambientes virtuais e checkpoints de notebooks.
- `LICENSE` define a licenca MIT para o material deste repositorio.

## Contribuicoes

Contribuicoes sao bem-vindas por pull request. Antes de contribuir, leia
[`CONTRIBUTING.md`](CONTRIBUTING.md), rode `python3 tools/validate_notebooks.py`
e re-execute os notebooks afetados para manter os outputs versionados consistentes.

Para problemas de seguranca, consulte [`SECURITY.md`](SECURITY.md). Para regras
de convivencia do projeto, consulte [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Licenca

Distribuido sob a licenca MIT. Veja [`LICENSE`](LICENSE).
