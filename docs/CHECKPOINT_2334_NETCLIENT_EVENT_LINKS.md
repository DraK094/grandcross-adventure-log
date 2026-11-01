# Checkpoint 2334 — associação tipada de eventos ProudNet

Leitura estática do metadata IL2CPP v29 (SHA256 eea7a31712bfca44caaa85cee3874ae9092a035556fcdef10f6c6a1fe156448b).

**Achados confirmados:**
- `Nettention.Proud.NetClient` contém 17 campos de eventos terminados em `Handler`, todos resolvidos por índice IL2CPP como classes delegate nomeadas. Ex.: `joinServerCompleteHandler` -> `JoinServerCompleteDelegate`; `receivedUserMessageHandler` -> `ReceiveUserMessageDelegate`.
- `NetClient.m_native_NetClientEvent` (índice 41249) refere-se a `Nettention.Proud.NativeInternalNetClientEvent` (byvalTypeIndex 41248).
- `NetClient.m_native_NetClient` (índice 41266) refere-se a `Nettention.Proud.NativeNetClient` (byvalTypeIndex 41265).
- `NativeInternalNetClientEvent..ctor(netclient)` recebe o tipo `Nettention.Proud.NetClient` (índice 41376), e a classe também declara `m_netclient` (41377) e `GetNativeNetClientEvent`.

Essa associação tipada complementa os 17 contratos de `Delegate.Invoke` do checkpoint 2328. **Não comprova** execução do construtor, armazenamento efetivo de callbacks em runtime, fluxos de chamada, protocolos do jogo, autenticação ou servidor jogável.

Trilha análise do cliente avançou; trilha servidor local funcional não demonstrada. Scripts e evidências derivadas foram preservados localmente como `gc_2329_2334_links.py` e `GrandCross_2329_2334_netclient_links.json`. Nenhum binário comercial publicado.