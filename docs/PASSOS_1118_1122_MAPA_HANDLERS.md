# GrandCross Local — PASSOS 1118–1122

Testes autonomos efetivamente executados no metadata IL2CPP v29 antigo e atual. Metadados: antigo 34451 tipos e 262861 metodos; atual 34488 tipos e 263448 metodos. Classes PacketHandler: 53 antigo, 54 atual.

PASSO 1119: no recorte de classes com PacketHandler/PacketManager e classes prioritarias, 63 classes compartilhadas, 1 adicionada (`ArenaTagPvp_PacketHandler`), 0 removidas, 7 classes com assinaturas nominais alteradas: `ArenaRealTimePvp_PacketHandler`, `Artifact_PacketHandler`, `Costume_PacketHandler`, `Guild_PacketHandler`, `Lobby_PacketHandler`, `Mail_PacketHandler`, `Skin_PacketHandler`.

PASSO 1120: 10 classes prioritarias e metodos inventariados. PASSO 1121: 1432 metodos com prefixos de mensagens em 53 classes PacketHandler na versao atual, entre eles 1212 CG_, 108 CR_, 68 RC_, 30 GC_ e 14 CW_. PASSO 1122: auditoria; nomes e assinaturas **nao identificam o formato binario, ids RMI, handshake, autenticacao ou ordem de execucao**. Nenhuma sessao local comprovada. Arquivos proprietarios nao publicados.

Proximo passo 1123 nao executado.