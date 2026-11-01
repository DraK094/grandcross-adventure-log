# GrandCross Local — checkpoint 2236: divergências nominais em handlers e stubs

## Evidência

Análise do metadata IL2CPP v29 após a classificação das 52 exceções do passo 2233. Comparação aproximada de nomes de métodos de handlers com os nomes de campos e métodos `ProcessReceivedMessage_*` presentes no mesmo conjunto de stubs.

Quatro exemplos com similaridade textual acima de 0,93, mas **sem igualdade exata**, foram verificados:

- `GuildRoom_Relay_PacketHandler.RC_NotifyGuildroomOtherPlayerJoinOK` versus `SevenDSRelayR2C.Stub.RC_NotifyGuildRoomOtherPlayerJoinOK` (maiúsculas em `Room`).
- `Guild_PacketHandler.CG_RequestGuildBossUserRankInfoOK` versus `SevenDSGameS2C_Guild.Stub.CG_Request_GuildBoss_User_Rank_InfoOK` (sublinhados).
- `Guild_PacketHandler.CG_RequestGuildBossUserRankInfoRangeOK` versus `SevenDSGameS2C_Guild.Stub.CG_Request_GuildBoss_User_Rank_Info_RangeOK` (sublinhados).
- `Cooperate_PacketHandler.CG_RquestCooperateStartOK` versus `SevenDSGameS2C.Stub.CG_RequestCooperateStartOK` (grafia diferente).

Os quatro nomes de destino possuem **tanto campo quanto método de processamento** no stub indicado. O handler de origem existe nos metadados. **Não** foi confirmada ligação de execução, tipo do delegate ou igualdade integral das assinaturas; por isso esses casos são **candidatos a apelidos/renomeações**, não correspondências exatas válidas para somar às 1.396 anteriores.

Outra família de dez exceções usa `ArenaRealTimeDecision` no handler, enquanto existem nomes próximos `ArenaRealTimePvp` nos stubs. A relação semântica ainda é hipótese, sem prova de identidade de mensagem.

## Situação

Há agora três classes de exceção: nomes auxiliares, nomes de mensagem sem tríade exata e nomes potencialmente divergentes. O mapa deve preservar a diferença entre correspondência textual, correspondência tipada e fluxo real.

**Servidor local:** nenhum handshake/RMI/login do Grand Cross validado. Não publicar binários comerciais nem dados de contas.
