# GrandCross Local — PASSOS 1150–1154: auditoria RMI

**Testes executados** no metadata IL2CPP v29 atual do usuario (`global-metadata(2).dat`) usando parser de tabelas de tipos e metodos, sem executar o cliente.

1150: filtro amplo por nomes relacionado a RMI resultou 69 ocorrencias, incluindo falsos positivos devido a substring; **o numero 69 NAO e a quantidade real de tipos RMI**. 1151: 54 classes `PacketHandler` no metadata atual; entre seus metodos encontram-se 1212 CG_, 108 CR_, 68 RC_, 30 GC_, 14 CW_. 1152: interfaces concretas `Nettention.Proud.RmiProxy`, `RmiStub`, `RmiContext`, `NativeRmiContext`, `RmiID`, `IRmiHost`; em Assembly-CSharp ha `RmiMessage`, `WestSideProxy`, `WestSidePacketManager`, `Auth_PacketHandler`. 1153: os metodos `WestSideProxy.RmiSend(remotes,rmiContext,msg,rmiName,rmiID)`, `Auth_PacketHandler.CG_RequestLoginOK(remote,rmiContext,userInfo,loginServiceInfo)` e `CG_RequestLoginInstantlyOK(...)` tem os nomes de argumentos confirmados estruturalmente. Os campos `rmiID`/`rmiName` indicam argumentos declarados, **nao seus valores numericos de runtime**.

1154: filtro corrigido para nomes que incluem `Rmi` exatamente (case-sensitive), reduzido a 12 tipos, dentre eles `RmiProxy`, `RmiStub`, `RmiContext`, `NativeRmiContext`, `RmiID`, `BeforeRmiSummary`, `AfterRmiSummary`, `RmiMessage`. Resultado nao prova protocolo binario, handshake nem compatibilidade do cliente oficial com servidor local.

PASSO 1155 planejado: inspecao estrutural dos campos de `RmiMessage`, `RmiContext` e wrappers; nao executado. Nenhum binario do jogo publicado.