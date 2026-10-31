# PASSO 2089 — Classes declarantes de conexão e RMI

Concluído após correções de tipagem e exibição no PowerShell. Metadata IL2CPP v29, 263448 MethodDefinitions, 34488 TypeDefinitions, stride de TypeDefinition 88. Foram apresentados 80 métodos em 50 tipos.

## Descoberta principal
- `Nettention.Proud.NetClient` TypeDef 33408: AttachProxy 257638, AttachStub 257639, Connect 257643, Disconnect 257645, HasServerConnection 257647, FrameMove 257648.
- `Nettention.Proud.NativeNetClient` TypeDef 33436: Disconnect 257770, HasServerConnection 257773, Connect 257774, FrameMove 257775, SetEventSink 257776, AttachProxy 257777, AttachStub 257778.
- `Nettention.Proud.NativeInternalProxy` 33391: RmiSend 257621; `Nettention.Proud.NativeInternalStub` 33392: ProcessReceivedMessage 257629; `Nettention.Proud.RmiProxy` 33422: RmiSend 257721; `Nettention.Proud.RmiStub` 33425: ProcessReceivedMessage 257727.

## Outras classes relevantes
- `WestSideProxy` 8607, `GameProxy` 18229, `GuildProxy` 8594, `RelayProxy` 19561: RmiSend.
- Stubs SevenDS Game, West, Relay com ProcessReceivedMessage.
- `NetmarbleS.TCPSessionPlatform` 4306, `NetmarbleS.TCPSession` 8975, `WestSidePacketManager` 17436.

## Limites
Classes e métodos estão estruturalmente identificados no metadata. **Não comprovado:** chamadas efetivas em runtime, P/Invoke entrypoints, protocolo/handshake, sessão aceita pelo servidor, backend local. Próxima etapa: examinar importações/PInvoke estruturais e método gerenciado para conexão, somente leitura.
