# GrandCross Local — Checkpoint 2310

Pesquisa estática, somente leitura, no metadata IL2CPP v29: foram resolvidos os tipos dos parâmetros de três métodos P/Invoke de callback RmiStub e comparadas suas assinaturas com NativeInternalStub.

| P/Invoke | Tipo de callback (segundo argumento) | Delegate.Invoke | Método NativeInternalStub | Assinatura exata |
| --- | --- | --- | --- | --- |
| RmiStub_SetCallbackProcessReceivedMessage | 67765 = Delegate_4 | (System.IntPtr, System.IntPtr, System.Int64) -> System.Boolean | ProcessReceivedMessage | Sim |
| RmiStub_SetCallbackGetRmiIDList | 67767 = Delegate_6 | (System.IntPtr) -> System.IntPtr | GetRmiIDList | Sim |
| RmiStub_SetCallbackGetRmiIDListCount | 67760 = Delegate_1 | (System.IntPtr) -> System.Int32 | GetRmiIDListCount | Sim |

O primeiro argumento dos três métodos P/Invoke é System.IntPtr (índice IL2CPP 37861). Tipos, ordem dos argumentos e retorno coincidem em 3/3 comparações. A existência das exportações CSharp_* correspondentes foi verificada no checkpoint 2305.

Este é um contrato estrutural de interoperabilidade explicitamente tipado, não evidência de que o jogo registre ou execute callbacks, nem prova de protocolo específico, autenticação ou servidor jogável.

Arquivos derivados locais: gc_2306_2310_validation.py, GrandCross_2306_2310_callback_contracts.json, GrandCross_Local_CHECKPOINT_2310.md. Não publicar binários proprietários nem dados de conta.

Trilha cliente: marco estrutural confirmado. Trilha servidor local funcional: nenhuma compatibilidade demonstrada.