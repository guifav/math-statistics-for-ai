# Protecao da branch main

Este repositorio deve manter a branch `main` protegida. A protecao nao e
configurada por arquivos versionados; ela precisa ser aplicada nas configuracoes
do GitHub.

## Configuracao recomendada

Em `Settings > Branches > Add branch protection rule`:

- Branch name pattern: `main`
- Marcar `Require a pull request before merging`
- Exigir pelo menos 1 aprovacao
- Marcar `Dismiss stale pull request approvals when new commits are pushed`
- Marcar `Require review from Code Owners`
- Marcar `Require status checks to pass before merging`
- Selecionar o check `validate`
- Marcar `Require conversation resolution before merging`
- Bloquear force pushes
- Bloquear delecao da branch

## Motivo

Essas regras impedem push direto, force push e delecao acidental da branch
principal. Tambem fazem com que toda contribuicao passe pelo validador de
notebooks e por revisao humana antes do merge.
