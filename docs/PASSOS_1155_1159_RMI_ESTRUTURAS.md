# GrandCross Local — PASSOS 1155–1159 RMI

Analise offline do metadata IL2CPP v29 atual. Foram verificados 18 tipos-alvo, 64 campos e 138 metodos. `RmiMessage` declara remotes, rmiContext, msg, rmiID, rmiName; `WestSidePacketManager.EnqueueSendMessage` e `WestSideProxy.RmiSend` declaram os mesmos 5 nomes de argumentos. `RmiStub.ProcessReceivedMessage` e `NativeNetClient.AttachProxy`/`AttachStub` estao presentes. `RmiContext` declara controles reliability, encryptMode, compressMode.

Documentacao ProudNet confirma que IDs de mensagens RMI sao definidos no PIDL, que Proxy/Stub sao gerados e que `CMessage` e marshalers definem a serializacao de parametros. Campos e nomes no metadata **nao** fornecem valores concretos dos IDs do Grand Cross nem bytes de rede. Nenhuma conexao do cliente oficial a um backend local, nem login compativel, nem taverna local foi demonstrada. Compreensao 100% RMI NAO atingida.

Docs: https://docs.proudnet.com/proudnet.eng/proudnet/using_pn/rmi ; https://docs.proudnet.com/proudnet.eng/proudnet/using_pn/pidl ; https://docs.proudnet.com/proudnet.eng/proudnet/using_pn/pidl/using_pidl .