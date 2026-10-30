# PASSO 1045 — Primeira coleta in-game, medição inicial

**Coleta inicial executada no Windows do usuário em 30/10/2026 02:33:31.** Comparação pré/pós interação não recebida: o passo **não está totalmente concluído** como experimento de UI.

- `7dsgc.exe`: PID 30012, 187 threads, iniciado às 02:32:45.

- `GameAssembly.dll` instalada: 47.294.480 bytes, SHA256 `01761332EA33C2FF2C88B3FEA8DA924CD8482D7DFA86B5B02C1C1CB6F1660624`. Confere com a versão atual analisada.

- `Player.log` do Grand Cross: `LocalLow/Netmarble FNC/SevenDeadlySinsGlobal/Player.log`, 1.333 bytes, modificado pela última vez em 28/10/2026 às 02:32:08, portanto NÃO atualizado até a medição de 30/10/2026 às 02:33:31.

- O script também listou metadados de logs de outros jogos, sem utilidade para o teste: próximos diagnósticos devem restringir a pasta do Grand Cross.

- Não foram coletados conteúdos de logs, credenciais, tokens nem código de sincronização.

- Evidência apenas de processo em execução e integridade da DLL. NÃO comprova sequência completa de inicialização IL2CPP ou servidor offline funcional.

**Próximo teste:** medir pré/pós uma interação reversível sem login: manter jogo aberto, fechar a janela de sincronização por Cancelar se seguro e observar visualmente mudança de interface; repetir apenas processo/threads/hash e metadados do único Player.log relevante. Pedir duas saídas e descrição da mudança; não enviar códigos ou dados de conta.

**Objetivo 2:** EM ANDAMENTO. Não publicar arquivos de jogo ou conteúdo de log.