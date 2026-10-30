# Checkpoints automatizados do GrandCross Local

O workflow `.github/workflows/grandcross-checkpoint.yml` é disparado ao adicionar ou alterar um arquivo `checkpoints/PASSO_NNNN.json`. Ele **não detecta passos dentro do ChatGPT**: o assistente precisa publicar o manifesto e as evidências primeiro.

## Próximo marco: PASSO 1290
Assim que os passos 1289 e 1290 forem realmente concluídos, publicar os arquivos sanitizados de evidência, criar `checkpoints/PASSO_1290.json` e confirmar os commits. **Não publicar o manifesto 1290 antes da conclusão.**

Exemplo de manifesto (adaptar caminhos aos arquivos efetivamente publicados):

```json
{
  "step": 1290,
  "status": "concluido",
  "files": [
    {
      "path": "Copias_de_seguranca_relatorios_e_scripts_backup/relatorios/PASSOS_1289_1290.md",
      "sha256": ""
    },
    {
      "path": "Copias_de_seguranca_relatorios_e_scripts_backup/evidencias/PASSOS_1289_1290.json"
    }
  ]
}
```

No exemplo, o campo `sha256` vazio significa que o validador calculará o hash; preenchido, deve bater com o arquivo. O manifesto e os arquivos devem estar no **mesmo commit ou em commits anteriores** no branch de execução.

## O que realmente acontece
1. O GitHub Actions usa `actions/checkout@v4` e executa `scripts/validate_checkpoint.py`.
2. O validador verifica que o passo é múltiplo de 10, que o manifesto tem status `concluido`, e que seus arquivos existem e são tipos permitidos.
3. Ele confere SHA-256 quando fornecido, empacota cópias e publica um artifact GitHub Actions com retenção de **90 dias**.
4. A cópia **permanente e versionada** é o próprio commit GitHub que contém as evidências. O artifact é redundância temporária, não substitui o commit.
5. Se qualquer validação falhar, o workflow marca erro. Não há backup completo declarado.
6. É possível executar manualmente no GitHub Actions via `workflow_dispatch`, informando o número de passo.

## Limites importantes
- O workflow não possui acesso à memória do PC, à conversa nem a arquivos que não estejam commitados; não gera evidência científica por conta própria.
- O workflow tem `contents: read` e **não faz commits**, prevenindo alteração ou sobrescrita automática.
- Não publicar binários do cliente, metadata de terceiros, segredos, credenciais ou dumps sensíveis. Verificar manualmente o conteúdo; o validador oferece apenas verificações básicas de nomes/extensões.
- Dependendo das configurações do repositório, GitHub Actions pode precisar ser habilitado; e é preciso observar a quota aplicável.
- Manter relatórios formais de 100 em 100 passos, além destes checkpoints de 10 em 10.

Veja também `LEIA_PRIMEIRO_PROXIMO_CHAT.md` e `Copias_de_seguranca_relatorios_e_scripts_backup/relatorios/POLITICA_BACKUP_CADA_10_PASSOS.md`.
