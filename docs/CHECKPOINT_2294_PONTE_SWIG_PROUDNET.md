# GrandCross Local — Checkpoint 2294: ponte SWIG/C# identificada

Inspeção **somente leitura** de duas bibliotecas ProudNet previamente enviadas e do metadata IL2CPP do jogo.

## Evidências
- `ProudNetClientPlugin.dll`: **801 exportações nomeadas**, sendo **798** com prefixo `CSharp_` e **3** rotinas `SWIGRegister*Callbacks_ProudNetClientPlugin` (callbacks de exceção, argumentos e string). Os 801 nomes ocupam **659 RVAs distintos** na imagem.
- Todas as 801 exportações mapeiam bytes raw da seção `.text`.
- Diretório de importações PE de `ProudNetClientPlugin.dll` referencia nominalmente `ProudNetClient.dll`.
- A interface expõe nomes como `CSharp_NativeRmiContext_rmiID_get`, `CSharp_NativeRmiContext_rmiID_set` e `CSharp_NativeToRmiProxyWrap_New`.
- A cópia de metadata IL2CPP v29 declara tipos `Nettention.Proud.NativeRmiContext`, `Nettention.Proud.NativeNetClient`, `Nettention.Proud.NativeInternalProxy`, `Nettention.Proud.NativeInternalStub`, `Nettention.Proud.RmiContext`, `Nettention.Proud.RmiProxy`, `Nettention.Proud.RmiStub` e classes `SWIGExceptionHelper`, `SWIGPendingException`, `SWIGStringDelegate`, `SWIGStringHelper`.

## Significado e limites

**Marco estrutural:** ponte C#/nativo de padrão SWIG identificada por nomes de exportação, dependência importada e tipos correspondentes nos metadados. O SDK nativo dispõe de superfícies estáticas analisáveis sem depender da seção virtual do GameAssembly.

**Não comprovado:** ligação de chamadas específica em execução, assinaturas ABI completas, serialização de mensagens de Grand Cross, RMI IDs concretos, autenticação ou servidor local jogável.

Arquivos derivados reproduzíveis: `gc_2289_2294_bridge.py`, `GrandCross_2289_2294_proud_bridge.json` e `GrandCross_Local_CHECKPOINT_2294.md`. Nenhuma DLL proprietária, metadata bruta ou dado de conta publicado.
