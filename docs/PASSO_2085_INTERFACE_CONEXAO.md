# PASSO 2085 — Interfaces de conexão ProudNet

Data: 31/10/2026. Evidência: saída PowerShell de auditoria estática das exportações dos arquivos PE locais; nenhuma DLL executada, pacote enviado ou memória alterada.

- ProudNetClientPlugin.dll: 801 nomes exportados, 617 coincidiram com o filtro amplo.
- ProudNetClient.dll: 706 nomes exportados, 189 coincidiram com o filtro.
- Exportações relevantes da camada CSharp_ identificadas: NativeNetClient_Create (147), Connect__SWIG_0/1 (145/146), SetEventSink (194), FrameMove__SWIG_0/1 (152/153), AttachProxy (143), AttachStub (144); NetConnectionParam_protocolVersion_get/set (581/582), serverIP_get/set (583/584), serverPort_get/set (585/586); NetClientEvent_SetCallbackJoinServerComplete (543), SetCallbackLeaveServer (544), SetCallbackError (540); RmiProxy_RmiSend (702), RmiStub_SetCallbackProcessReceivedMessage (709).
- Biblioteca nativa também exporta símbolos C++ de CNetClient, CNetConnectionParam, IRmiProxy e IRmiStub.

Interpretação: caminho potencial API C# -> plugin nativo -> core ProudNet. Os nomes **não provam chamadas pelo jogo, parâmetros efetivos, sessão estabelecida ou compatibilidade de um backend**. Próxima etapa: inventário somente leitura de bindings e metadados gerenciados. Sem servidor local funcional demonstrado.
