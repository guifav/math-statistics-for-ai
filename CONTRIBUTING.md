# Contribuindo

Obrigado por ajudar a melhorar o Math & Statistics for AI. Este repositorio e
um curriculo educacional em portugues, baseado em notebooks Jupyter. O objetivo
das contribuicoes e manter o material correto, executavel, didatico e facil de
revisar.

## Tipos de contribuicao

Contribuicoes bem-vindas:

- Correcao de erros conceituais, matematicos, estatisticos ou de codigo.
- Melhorias de clareza em explicacoes, exemplos e exercicios.
- Novos exercicios acompanhados de solucoes de referencia.
- Correcoes em links, referencias internas e dependencias.
- Melhorias no validador, CI e organizacao do material.

Antes de adicionar um notebook novo, abra uma issue descrevendo o objetivo, o
modulo afetado e como ele se encaixa no curriculo.

## Ambiente local

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
jupyter lab notebooks
```

Para contribuicoes que usam CUDA 12.1:

```bash
python3 -m pip install -r requirements.txt
python3 -m pip install -r requirements-gpu.txt
```

## Validacao obrigatoria

Antes de abrir um pull request, execute:

```bash
python3 tools/validate_notebooks.py
```

O validador verifica:

- JSON valido nos notebooks.
- Cabecalho padrao na primeira celula.
- Metadados obrigatorios do curso.
- Sintaxe Python das celulas de codigo.
- Referencias internas para notebooks existentes.
- Tags `exercise` e `solution` consistentes.
- Ausencia de placeholders genericos e caminhos temporarios.
- Ausencia de outputs e `execution_count` versionados.

## Politica de notebooks

Mantenha os notebooks versionados sem outputs. Isso reduz diffs grandes, evita
expor dados locais e torna a revisao mais objetiva.

Antes de commitar, limpe outputs e contadores de execucao no Jupyter ou com:

```bash
jupyter nbconvert --clear-output --inplace notebooks/**/*.ipynb
```

Se o shell nao expandir `**`, use uma ferramenta equivalente ou limpe os
notebooks pelo Jupyter.

## Padrao de exercicios

- Enunciados de pratica devem usar a expressao `TAREFA DO ALUNO`.
- Celulas de pratica devem receber a tag `exercise`.
- Celulas com implementacao de referencia devem receber a tag `solution`.
- Cada grupo de celulas `exercise` deve ter uma solucao adjacente, dentro do
  grupo ou em ate 3 celulas depois.

## Estilo de conteudo

- Escreva em portugues.
- Prefira exemplos pequenos, reprodutiveis e didaticos.
- Evite depender de credenciais, caminhos locais ou datasets privados.
- Mantenha links relativos quando apontar para arquivos do repositorio.
- Evite mudancas mecanicas em muitos notebooks no mesmo PR quando a alteracao
  conceitual for pequena.

## Fluxo de pull request

1. Crie uma branch a partir de `main`.
2. Faca mudancas focadas em um unico tema.
3. Rode `python3 tools/validate_notebooks.py`.
4. Abra um pull request usando o template do repositorio.
5. Aguarde CI verde e revisao.

Pull requests para `main` devem passar pelo CI e por revisao antes do merge.
