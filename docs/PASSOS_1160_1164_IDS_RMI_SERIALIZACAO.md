# GrandCross Local — PASSOS 1160–1164: IDs RMI e serialização

Testes realizados em metadata v29 e GameAssembly atual, sem executar cliente.

**1160** Documentação ProudNet: IDs RMI declarados em PIDL por base+incremento, com suporte a atribuição explícita `[id=...]`; **não** são tokens ou índices IL2CPP.
**1161** Inventário de 10 classes; `RmiID` é tipo com `value__`, `RmiID_None`, `RmiID_Last`, sem IDs de mensagens do Grand Cross. `WestSideProxy.RmiSend` e `WestSidePacketManager.EnqueueSendMessage` declaram campos/argumentos de RMI.
**1162** Busca por strings ASCII/UTF16LE no GameAssembly atual retornou zero hits para nomes como `CG_RequestLoginOK`, apesar de aparecerem no metadata. Isso não prova ausência em código ou dados compactados.
**1163** Nenhum `.pidl`, `.pcap` ou `.pcapng` diretamente presente no diretório de entrada do laboratório.
**1164** Documentação ProudNet: serialização de parâmetros com `CMessage` e marshalers, mas nenhuma representação binária real do Grand Cross recuperada.

**Resultados:** IDs numéricos concretos de Grand Cross recuperados = **0**; frames de Grand Cross decodificados = **0**; conexão local do cliente validada = **0**. Próximo foco: fonte confiável de IDs (PIDL ou equivalentes), serialização e captura consentida de sessão de teste; não inventar IDs ou formatos. Nenhuma DLL proprietária publicada.

Fontes: https://docs.proudnet.com/proudnet.eng/proudnet/using_pn/pidl ; https://docs.proudnet.com/proudnet.eng/proudnet/using_pn/rmi/using_rmi ; https://docs.proudnet.com/proudnet.eng/proudnet/using_pn/pidl/using_pidl