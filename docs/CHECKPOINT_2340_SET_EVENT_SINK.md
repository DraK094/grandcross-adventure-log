# GrandCross Local — checkpoint 2340: ligação tipada da interface de eventos

Análise estática do metadata IL2CPP v29, somente leitura.

- NetClient mantém referências tipadas a NativeNetClient e NativeInternalNetClientEvent.
- NativeInternalNetClientEvent..ctor recebe NetClient; possui campo m_netclient: NetClient.
- NativeInternalNetClientEvent.GetNativeNetClientEvent() retorna System.IntPtr, índice de tipo 37861.
- NativeNetClient.SetEventSink(obj: System.IntPtr) aceita o mesmo índice de tipo 37861.
- ProudNetClientPluginPINVOKE.NativeNetClient_SetEventSink recebe (System.Runtime.InteropServices.HandleRef, System.IntPtr), retorna System.Void.
- ProudNetClientPluginPINVOKE.NativeNetClient_Create retorna System.IntPtr; NativeNetClient.Create retorna a classe NativeNetClient.
- Operações AttachProxy/AttachStub possuem padrão tipado análogo (HandleRef, IntPtr na ponte).

O conjunto constitui correspondência de **assinaturas de interface** para passagem de ponteiro do objeto de eventos à operação SetEventSink, mas não comprova que a chamada acontece, que os objetos estejam inicializados, nem registro efetivo de callbacks. Nenhuma compatibilidade de servidor local com o cliente foi demonstrada. Evidências e script locais no checkpoint 2340. Não publicar arquivos proprietários ou dados de conta.