# GrandCross Local — checkpoint 2328: contratos tipados de eventos ProudNet

Análise estática somente leitura do metadata IL2CPP v29. Comparação de três conjuntos: métodos `On...` de `Nettention.Proud.NativeInternalNetClientEvent`, métodos `NetClientEvent_SetCallback...` de `Nettention.Proud.ProudNetClientPluginPINVOKE` e definições de classes `Delegate_*`.

Resultados **validados**: 17/17 métodos de evento possuem declaração P/Invoke nominal; 17/17 índices do último parâmetro P/Invoke resolvem diretamente via `byvalTypeIndex` a classe Delegate correta; 17/17 assinaturas de `Delegate.Invoke` coincidem exatamente com a sequência de índices de tipos de parâmetros e de retorno do respectivo método `On...`. Há **nove tipos Delegate distintos** compartilhados pelos 17 eventos. `Delegate_0` é reutilizado em oito eventos.

Exemplos: `OnJoinServerComplete` -> `Delegate_8` (IntPtr, IntPtr, IntPtr); `OnNoRmiProcessed` -> `Delegate_12` (IntPtr, Int32); `OnReceiveUserMessage` -> `Delegate_7` (IntPtr, Int32, IntPtr, IntPtr, Int32); `OnError` -> `Delegate_0` (IntPtr, IntPtr).

**Escopo:** associações de tipos e assinaturas comprovadas em metadados, não registro/execução dos callbacks, serialização, protocolo específico do jogo, autenticação ou servidor local jogável. Nenhum binário proprietário, segredos ou dados de conta publicados.

Reprodução local: `gc_2321_2328_events.py`, `GrandCross_2321_2328_event_delegate_evidence.json`, `GrandCross_Local_CHECKPOINT_2328.md`.