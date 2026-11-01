# GrandCross Local — Checkpoint 2305: ligação nominal P/Invoke ↔ DLL

Leitura somente estática de metadata IL2CPP v29 e exportações PE do ProudNetClientPlugin.dll. Na classe Nettention.Proud.ProudNetClientPluginPINVOKE há **114 métodos declarados**: **113/113 métodos que não são o inicializador estático `.cctor`** possuem uma exportação de nome **exatamente correspondente** depois da adição do prefixo `CSharp_`. O único sem exportação é `.cctor`.

Exemplos confirmados:
- `RmiStub_SetCallbackProcessReceivedMessage` — argumentos IL2CPP `jarg1:37861`, `jarg2:67765`; exportação `CSharp_RmiStub_SetCallbackProcessReceivedMessage`, RVA `0x9C20`.
- `RmiStub_SetCallbackGetRmiIDList` — `jarg1:37861`, `jarg2:67767`.
- `RmiStub_SetCallbackGetRmiIDListCount` — `jarg1:37861`, `jarg2:67760`.
- `RmiProxy_RmiSend` — oito argumentos no wrapper gerenciado e exportação correspondente.
- `NativeNetClient_AttachProxy` e `AttachStub` — pareamento nominal exato.

**O que isso demonstra:** contrato de nomes da fronteira de interoperabilidade gerenciada/nativa do SDK; mais forte que semelhanças genéricas entre classes. **O que não demonstra:** chamadas executadas pelo cliente, registro real dos callbacks, ABI da função nativa, IDs ou conteúdo das mensagens, protocolo/autenticação do Grand Cross ou compatibilidade do servidor local.

Reprodutibilidade local: `gc_2301_2305_pinvoke.py`, `GrandCross_2301_2305_pinvoke_matches.json`, `GrandCross_Local_CHECKPOINT_2305.md`. Nenhum binário proprietário ou dado de conta publicado. Trilha cliente: marco validado. Trilha servidor funcional: inalterada.