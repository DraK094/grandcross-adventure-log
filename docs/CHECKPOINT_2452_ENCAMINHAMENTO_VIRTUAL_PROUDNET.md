# GrandCross Local — Checkpoint 2452: encaminhamento virtual ProudNet

Auditoria estática, somente leitura, de `ProudNetClientPlugin.dll` (SHA256 `91ef8ef7624491d1598f0f5ef31b83fa62a0e2a45a8324ebdb8b7edb43bd845c`). A tabela de exportações PE e os bytes das seguintes rotinas foram verificados:

| Exportação | RVA | Evidência nativa |
|---|---|---|
| CSharp_NetClientEvent_SetCSharpHandle | 0x9BD0 | grava `rdx` em `[rcx+0x10]` |
| CSharp_NativeNetClient_SetEventSink | 0x5040 | chamada virtual `[rax+0x138]` |
| CSharp_NativeNetClient_AttachProxy | 0x5060 | chamada virtual `[rax+0x8]` |
| CSharp_NativeNetClient_AttachStub | 0x5080 | chamada virtual `[rax+0x10]` |
| CSharp_NativeNetClient_FrameMove__SWIG_0 | 0x43B0 | chamada virtual `[rax+0xB0]` |
| CSharp_NativeNetClient_FrameMove__SWIG_1 | 0x43D0 | chamada virtual `[rax+0xB0]` |

**Comprovado:** seis exports possuem os prefixos de instruções verificados no binário e as operações do SDK encaminham ações por vtable. **Não comprovado:** identidade dos objetos em execução, destino da chamada virtual, chamada pela aplicação Grand Cross, handshake, IDs RMI, login local ou servidor jogável.

Reprodução local: `gc_2441_2452_virtual_dispatch.py`, `GrandCross_2441_2452_virtual_dispatch.json`, `GrandCross_Local_CHECKPOINT_2452.md`. Não publicar binários proprietários.