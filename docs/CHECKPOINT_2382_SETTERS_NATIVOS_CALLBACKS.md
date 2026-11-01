# GrandCross Local — Checkpoint 2382: implementação nativa dos callbacks RmiStub

**Marco confirmado por leitura dos bytes e desmontagem x64 da cópia de ProudNetClientPlugin.dll.** O plugin contém três rotinas que armazenam o segundo argumento (`rdx`) em um objeto apontado por `rcx` e retornam. Cada instrução foi confirmada por comparação com cinco bytes da seção `.text` e desmontagem com `objdump`.

| Exportação | RVA | Corpo validado |
|---|---|---|
| `CSharp_RmiStub_SetCallbackGetRmiIDList` | `0x9C00` | `mov qword ptr [rcx+0x28],rdx; ret` |
| `CSharp_RmiStub_SetCallbackGetRmiIDListCount` | `0x9C10` | `mov qword ptr [rcx+0x30],rdx; ret` |
| `CSharp_RmiStub_SetCallbackProcessReceivedMessage` | `0x9C20` | `mov qword ptr [rcx+0x38],rdx; ret` |

**Limite rigoroso:** comprovamos o comportamento *se essas exportações forem chamadas*, não a chamada efetiva pelo Grand Cross, nem os valores de callbacks, nem registro durante uma sessão. Não foram recuperados IDs RMI, protocolo específico, autenticação ou servidor jogável. Nenhum binário proprietário ou informação de conta incluído.

Reprodução local: `gc_2379_2382_callback_code.py`, evidências `GrandCross_2379_2382_native_callback_evidence.json`, relatório `GrandCross_Local_CHECKPOINT_2382.md`. Trilha de análise do cliente: avanço para instruções nativas; trilha servidor funcional: inalterada.