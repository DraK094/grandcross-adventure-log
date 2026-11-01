# Checkpoint 2364 — Cobertura de oito eventos sem setters públicos

Análise estática e reprodutível do metadata IL2CPP v29. Foram cruzados os campos de eventos de `NetClient`, seus métodos `set_*Handler`, os métodos `On*` de `NativeInternalNetClientEvent`, as declarações `NetClientEvent_SetCallback*` e as assinaturas `Delegate_*.Invoke`.

**Resultado:** 17 campos de eventos; nove setters nominais; oito campos sem setter nominal na classe `NetClient`. Os oito casos sem setter apresentam **8/8** métodos correspondentes de evento, declaração nativa de registro por P/Invoke e delegate com assinatura exata do método `On*`. O campo `receivedUserMessageHandler` corresponde a `OnReceiveUserMessage` (diferença de flexão no nome), tratada como equivalência explícita, não correspondência aproximada arbitrária.

Os oito campos são `noRmiProcessedHandler`, `receivedUserMessageHandler`, `p2pMemberJoinHandler`, `p2pMemberLeaveHandler`, `changeP2PRelayStateHandler`, `changeServerUdpStateHandler`, `p2pMemberOfflineHandler` e `p2pMemberOnlineHandler`.

**Conclusão permitida:** ausência de setter público nominal não implica ausência de interface nativa tipada. **Ainda não demonstrado:** registro, chamada ou inicialização efetiva dos callbacks, protocolo específico do jogo, autenticação ou compatibilidade do servidor local. Nenhum arquivo proprietário publicado.

Scripts e resultados locais: `gc_2359_2364_audit.py`, `GrandCross_2359_2364_event_tiers.json`, `GrandCross_Local_CHECKPOINT_2364.md`.