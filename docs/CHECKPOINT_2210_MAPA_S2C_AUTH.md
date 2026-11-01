# GrandCross Local — Checkpoint 2210: correspondência estrutural de mensagens recebidas

## Marco validado

Inspeção **somente leitura** do metadata IL2CPP v29 enviado pelo usuário. Comparação sistemática dos nomes de métodos de `Auth_PacketHandler` com os métodos `ProcessReceivedMessage_*` de `SevenDSGameS2C.Stub`.

- `Auth_PacketHandler`: 26 métodos (24 handlers com nomes de mensagens, um construtor e um auxiliar).
- `SevenDSGameS2C.Stub`: 631 métodos.
- **24 de 24 handlers de mensagens de autenticação possuem correspondência nominal exata** com um método `ProcessReceivedMessage_` do stub.
- Exemplos de pares: `CG_RequestLoginOK`, `CG_RequestNetmarbleAuthOK`, `CG_RequestHeartBeatOK`, `CG_RequestSecurityTokenOK`, `CG_RequestLoginInstantlyOK`, `GC_NotifySecurity`.
- O construtor do handler recebe parâmetro `s2cStub`, que fortalece a hipótese de vinculação entre essas classes.
- Os métodos `ProcessReceivedMessage_*` compartilham assinatura nominal de entrada com `__msg`, `pa`, `hostTag` e `remote` no conjunto examinado.

## Interpretação e limitações

Esta correspondência completa de nomes fornece **um mapa estrutural específico de mensagens de autenticação** e um alvo melhor para a investigação. Não comprova chamada em execução, formatos serializados, IDs RMI, uso de transporte, bypass de autenticação ou compatibilidade do cliente com servidor local.

**Trilha de análise do cliente:** marco estrutural novo. **Trilha do servidor funcional:** inalterada, não demonstrada. Próximos testes: validar o papel concreto do parâmetro `s2cStub` e localizar a relação no código compilado sem pressupor o fluxo.

Não incluir binários comerciais, dumps proprietários, credenciais nem endereços de produção neste repositório.
