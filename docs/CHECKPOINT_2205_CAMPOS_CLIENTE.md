# Checkpoint 2201–2205

Inspeção estática do metadata IL2CPP v29. Campos verificados nos gerenciadores: PacketManager.m_gameClient (tipo índice 53127), GuildPacketManager.m_GuildClient (53187), WestSidePacketManager.m_WestSideClient (53130), RelayPacketManager.m_relayClient (53140).

PacketManager declara filas m_sendPriorityMessageQueue (18769) e m_sendMessageQueue (13159), além de estado de envio. RmiMessage declara campos remotes, rmiContext, msg, rmiID, rmiName. Auth_PacketHandler declara .ctor(s2cStub) com índice 46857 e UpdateGameData(userInfo) com índice 40152.

São dados de declarações no metadata, não prova de ligações de chamadas, protocolo, rede ativa nem autenticação funcional. Tipos 24537 e 13538 permanecem sem nome confirmado. Nenhuma compatibilidade de servidor jogável foi demonstrada. Binários comerciais e dados de conta não devem ser publicados.
