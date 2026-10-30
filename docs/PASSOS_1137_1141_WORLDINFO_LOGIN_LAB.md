# GrandCross Local — PASSOS 1137–1141

Testes efetivamente executados na versao atual IL2CPP v29 (global-metadata atual).

**1137:** `WorldInfoManager` declara `AddWorldInfo(name,worldId,region,ip,port,chatkitSetting)` e `AddWorldInfo(newWorldInfo)`, `SetMyWorldInfo(worldName)` e `SetMyWorldInfo(world)`; campos `m_worldInfoList`, `m_selectWorldInfo`, `m_dicRegionCode`.

**1138:** `WorldInfo` define `m_name`, `m_worldId`, `m_region`, `m_ip`, `m_port`; `PageLogin.GameServerConnect(worldInfo)` confirmado. **1139:** `Auth_PacketHandler.CG_RequestLoginOK(remote,rmiContext,userInfo,loginServiceInfo)` e `CG_RequestLoginInstantlyOK(...)` confirmados estruturalmente. **1140:** `WestSidePacketManager.ConnectToWestSideServer(ip,port)` e setters de IP/porta de `NetConnectionParam` confirmados.

**1141:** testes HTTP dinamicos no backend independente localhost, com SQLite temporario: **7/7 APROVADOS** (health, negacao sem token, criacao de sessao local, perfil autorizado, segunda sessao para mesmo perfil, negacao de token invalido, rota inexistente 404).

**LIMITES:** metadados de classes nao comprovam fluxo de chamadas ou possibilidade de adicionar servidor ao cliente. O backend independente nao implementa o protocolo do Grand Cross; nenhum handshake ou login com cliente oficial demonstrado. PASSO 1142 ainda pendente. Nenhum binario proprietario publicado.