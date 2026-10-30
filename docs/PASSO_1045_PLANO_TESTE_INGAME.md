# PASSO 1045 — Plano de teste in-game seguro

**Planejado; NÃO executado no Windows do usuário.** Último passo aprovado de análise: 1044. Objetivo 2 permanece EM ANDAMENTO.

Evidência disponível: captura da tela do jogo com interface de sincronização aberta; prova de renderização da UI, não de captura do fluxo de `il2cpp_init`. Ferramentas de inspeção do processo retornaram listagem de módulos inconclusiva e acesso negado ao caminho, sem justificação para contornar restrições.

**Experimento 1045 proposto:** executar script PowerShell de leitura que confirma PID e thread count via CIM, SHA256/tamanho da DLL instalada e procura apenas metadados (nomes, tamanhos, datas) de arquivos Player.log, Player-prev.log e output_log.txt em AppData/LocalLow. Fazer duas medições com UI aberta e depois de uma interação reversível sem login; nunca imprimir conteúdo de logs nem códigos, senhas ou tokens. O script foi gerado como artefato anexo à conversa `GrandCross_Teste_InGame_Seguro_1045.ps1` e ainda precisa de validação no Windows (não é um teste concluído).

**Critério de aprovação:** processo vivo, UI reage à ação simples, alterações observáveis comparadas, sem modificações do cliente. Isso é teste funcional superficial da UI, não validação de inicialização IL2CPP completa nem de servidor offline. Plano local completo: `GrandCross_Passo_1045_Plano_InGame.md`.

Material de referência: DLL instalada SHA256 `01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624`; .vdata SHA256 `72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231`.
