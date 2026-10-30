# GrandCross Local — PASSOS 1124–1127

1124: Auditoria estrutural no metadata atual IL2CPP v29. `PageLogin` 87 métodos e 34 campos; `Auth_PacketHandler` 26 métodos; `WestSidePacketManager` 14 métodos e 6 campos. Nomes e parâmetros de login identificados: `OnSecurityTokenRes`, `OnNetmarbleAuthCompleted`, `GameServerConnect(worldInfo)`, `CG_RequestLoginOK`, `CG_RequestLoginInstantlyOK`. Não há fluxo de runtime demonstrado.

1125: Implementado e testado um backend **independente** de laboratório em localhost, com sessão de teste aleatória, conta local, SQLite e inventário. Testes de dados 5/5 e HTTP loopback 3/3 passaram. Este serviço **não implementa protocolo do jogo** e não se conectou ao cliente oficial.

1126: Distinção comprovada entre identidade local de laboratório e autenticação oficial; não há bypass do cliente. 1127: lacunas para interoperabilidade: configuração autorizada de endpoint, IDs RMI, mensagens, handshake, serialização, validação do cliente. **Nenhum emulador jogável demonstrado.** Próximo passo 1128 pendente. Não publicados DLLs, metadata, tokens nem código de terceiros.