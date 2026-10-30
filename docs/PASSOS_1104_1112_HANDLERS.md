# PASSOS 1104-1112 — GrandCross Local

Analise estatica da copia atual do metadata IL2CPP 29. PASSO 1104: 79 campos em 11 classes formam 36 grupos de indices de tipos, com correspondencia biunivoca entre as duas versoes nos campos examinados. PASSO 1105: indices de tipos de retorno inspecionados, ainda nao resolvidos. PASSOS 1106-1107: tipos nomeados de handlers, proxies e metodos identificados; nomes nao demonstram mensagens de rede.

PASSOS 1108-1110: seis classes e 80 metodos verificados estruturalmente, sem inconsistencias. Classes: Auth_PacketHandler (26), WestSideContents_PacketHandler (14), WestSide_Game_PacketHandler (10), WestSidePacketHandler (7), WestSidePacketManager (14), ArenaTagPvp_PacketHandler (9). Exemplos: CG_RequestLoginOK e CW_RequestJoinChannelOK com nomes de parametros obtidos do metadata.

PASSO 1111: 39 metodos com prefixo CG, 14 CW, 2 GC, e 25 outros. PASSO 1112: auditoria concluiu que identificadores numericos RMI, formatos serializados, ordem de handshake e compatibilidade com cliente oficial nao foram demonstrados. PASSO 1113 ainda pendente. Nenhum emulador ou taverna local jogavel.