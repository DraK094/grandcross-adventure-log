# PASSOS 1134–1136 — Foco em login local e compatibilidade

Análise efetivamente executada no `global-metadata(2).dat` IL2CPP 29 da versão atual: 9 tipos relevantes, 173 métodos. Confirmadas as associações estruturais `PageLogin.GameServerConnect`, `OnSecurityTokenRes`, `OnNetmarbleAuthCompleted`, `Auth_PacketHandler.CG_RequestLoginOK`, `CG_RequestLoginInstantlyOK`, `CG_RequestNetmarbleAuthOK`, `CG_RequestVerifySecurityCertValueOK`, `WorldInfo` e `WorldInfoManager`, `WestSidePacketManager`, `NetConnectionParam`.

O parser inicial usou offsets errados para campos, foi corrigido para fieldDefinitions no header[11] e fieldStart em typeDef+32. A versão corrigida validou campos `WorldInfo.m_ip`, `m_port`, `m_worldId` e encontrou 173 métodos nos nove tipos. Repetidos testes independentes do backend SQLite: 5/5 PASS.

**O servidor oficial Netmarble não foi testado e não se deve supor que aceite uma identidade local fictícia.** O cliente oficial 7dsgc.exe não foi conectado ao backend local; falta conhecer configuração de destino legítima e protocolo aceito. Nenhum bypass ou reescrita de autenticação foi executado. Próximo passo 1137 pendente.