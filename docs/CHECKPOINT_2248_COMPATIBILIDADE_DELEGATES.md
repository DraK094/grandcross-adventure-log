# Checkpoint 2248 — verificando delegates entre famílias de stubs

Reanalisados oito métodos de handlers cujos nomes possuíam tríades (campo + `ProcessReceivedMessage_*`) em `SevenDSGameS2C.Stub`, não no stub declarado em seus próprios construtores.

## Resultado verificável
- **8/8:** tipo numérico de campo coincide com `byvalTypeIndex + 1` da definição de classe delegate nominal correspondente;
- **6/8:** a sequência completa de índices de tipos dos parâmetros de `Delegate.Invoke` coincide com a do handler;
- **2/8:** há divergências:
  - `Shop_PacketHandler.CG_RequestBillingRemainTROK`: o handler usa o tipo índice `50159` (`UserBuffInfo`) em `userBuffInfo`, enquanto o delegate usa índice `16088` em `userBuffInfoList`.
  - `Shop_PacketHandler.CG_RequestBillingVerifyPUOK`: o delegate inclui `missionResult` (índice `40760`, `MissionResult`) além dos parâmetros do handler.

As diferenças são **de assinatura**, não apenas de nomes. Sem prova de que os delegates sejam registrados nesses handlers, não é possível concluir que representem chamadas diretas nem afirmar causa como diferença de versões ou conversão intermediária.

Arquivos locais associados: `GrandCross_Local_CHECKPOINT_2248.md`, `GrandCross_2243_2248_evidence.json`, `gc_2243_2248.py`. Metadata IL2CPP analisado somente por leitura; nenhum binário ou segredo de usuário deve ser incluído no repositório.

**Trilha cliente:** novo filtro estrutural. **Trilha servidor jogável:** compatibilidade não demonstrada.
