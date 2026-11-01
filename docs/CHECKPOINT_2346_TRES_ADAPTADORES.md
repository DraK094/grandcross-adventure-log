# Checkpoint 2346 — três adaptadores nativos tipados

Análise somente leitura do metadata IL2CPP v29. Três classes adaptadoras declaram construtores fortemente tipados e getters com retorno `System.IntPtr` (índice IL2CPP 37861):

- `NativeInternalProxy..ctor(clrObj: RmiProxy)` e `GetNativeProxy(): IntPtr`.
- `NativeInternalStub..ctor(stub: RmiStub)` e `GetNativeStub(): IntPtr`.
- `NativeInternalNetClientEvent..ctor(netclient: NetClient)` e `GetNativeNetClientEvent(): IntPtr`.

`NativeNetClient` declara três operações `AttachProxy(obj: IntPtr)`, `AttachStub(obj: IntPtr)` e `SetEventSink(obj: IntPtr)`, todas com retorno `Void`. As assinaturas combinam em tipos, porém **nenhuma chamada real ou ordem de inicialização foi observada**. Também não há comprovação de protocolo ou de servidor local compatível.

Reprodução: arquivos derivados locais `gc_2341_2346_bridge.py`, `GrandCross_2341_2346_bridge_signatures.json`, `GrandCross_Local_CHECKPOINT_2346.md`. Não publicar binários proprietários ou dados de contas.