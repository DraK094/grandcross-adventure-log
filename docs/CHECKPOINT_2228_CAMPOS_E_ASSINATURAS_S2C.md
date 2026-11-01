# GrandCross Local — checkpoint 2223–2228

## Evidências novas (metadata IL2CPP v29)

Revalidação direta dos 1.388 pares de métodos e campos identificados no checkpoint 2222. Os campos dos stubs associados às mensagens têm **índices de tipo diferentes** para mensagens diferentes; exemplos no `SevenDSGameS2C.Stub`: `CG_RequestLoginOK` = 71060; `CG_RequestHeartBeatOK` = 70925; `CG_RequestSecurityTokenOK` = 71222. A hipótese de campos de callback/delegate específicos de mensagem é consistente, mas os nomes concretos dos tipos desses campos **não foram resolvidos** pela tabela simples `byvalTypeIndex`.

Os métodos de despacho `ProcessReceivedMessage_CG_RequestLoginOK`, `ProcessReceivedMessage_CG_RequestHeartBeatOK` e `ProcessReceivedMessage_CG_RequestSecurityTokenOK` compartilham a mesma interface de quatro parâmetros: `__msg` (índice 40600), `pa` (43733), `hostTag` (41691), `remote` (35126).

Os métodos correspondentes do `Auth_PacketHandler` têm assinaturas diferentes, próprias da mensagem: `CG_RequestLoginOK(remote:35126,rmiContext:44373,userInfo:40152,loginServiceInfo:40148)`; `CG_RequestHeartBeatOK(remote:35126,rmiContext:44373,apInfoList:13538)`; `CG_RequestSecurityTokenOK(remote:35126,rmiContext:44373,securityToken:46773)`.

**Interpretação:** o stub apresenta uma interface genérica de recepção e o handler declara argumentos de negócio específicos de cada resposta. Essa observação fortalece a hipótese de desserialização e despacho intermediário, **sem comprovar** chamadas reais, formato binário, IDs RMI ou compatibilidade do servidor experimental.

**Status:** análise estática avançou; servidor local jogável ainda não demonstrado. Não publicar arquivos proprietários, segredos ou dados reais de conta.
