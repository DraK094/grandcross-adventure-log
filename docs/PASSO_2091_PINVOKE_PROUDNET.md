# PASSO 2091 — Declarações P/Invoke ProudNet

Concluído após análise somente leitura do metadata IL2CPP v29: 34.488 TypeDefinitions e 263.448 MethodDefinitions. Busca por nomes de classes contendo Proud, PInvoke, SWIG ou Interop identificou 100 classes candidatas, 141 métodos selecionados, 120 nomes impressos e **116 métodos com flag PInvoke** dentro do universo analisado. Esses 116 não representam 116 conexões nem necessariamente todos os P/Invoke do binário.

## Evidência fundamental
- `Nettention.Proud.ProudNetClientPluginPINVOKE` TypeDef **33446** com métodos `PInvokeImpl=True`, `Flags=0x2096`.
- `NativeNetClient_Create` MethodIndex 257876.
- `NativeNetClient_Connect__SWIG_0` 257881.
- `NativeNetClient_FrameMove__SWIG_0` 257882.
- `NativeNetClient_SetEventSink` 257883.
- `NativeNetClient_AttachProxy` 257884, `NativeNetClient_AttachStub` 257885.
- `NetClientEvent_SetCallbackJoinServerComplete` 257939, erro 257946.
- `NetConnectionParam_serverIP_set` 257860, `serverPort_set` 257861, `protocolVersion_get` 257863.
- `Nettention.Proud.NetClient` e `Nettention.Proud.NativeNetClient` seguem sem PInvoke flag nas 44 definições examinadas no PASSO 2090.

## Interpretação e restrições
**Verificado:** classe gerenciada com métodos PInvoke que nominalmente correspondem aos exports `CSharp_*` do ProudNetClientPlugin.dll. **A confirmar:** mapeamento exato ModuleRef/entrypoint, chamadas efetivas, valores da conexão, formato de protocolo, handshake, sessão local. Arquivos, memória e rede não foram modificados. Próximo passo 2092: validar mapeamento com os exports e metadados de importação, em somente leitura.

Marco de cliente: `A Ponte Nativa`, categoria Lendária (analítica apenas); servidor local permanece sem handshake ou login demonstrado.
