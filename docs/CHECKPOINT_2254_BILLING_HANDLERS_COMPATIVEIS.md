# GrandCross Local — Checkpoint 2254

Análise estática de metadados IL2CPP v29, sem execução do jogo.

Foram comparados os métodos `CG_RequestBillingRemainTROK` e `CG_RequestBillingVerifyPUOK` nas classes `Shop_PacketHandler`, `Billing_PacketHandler` e respectivos `*Delegate.Invoke`.

**Resultado:** ambas as assinaturas de `Billing_PacketHandler` são idênticas à sequência de tipos de seus `Delegate.Invoke`. O método RemainTR contém 13 parâmetros idênticos em tipos e ordem; VerifyPU contém 16. As variantes em `Shop_PacketHandler` divergem: RemainTR apresenta um parâmetro de tipo diferente; VerifyPU possui 15 parâmetros e não recebe `missionResult`.

A associação de construtores é: `Billing_PacketHandler..ctor(s2cStub: SevenDSGameS2C.Stub)` (índice 46857) e `Shop_PacketHandler..ctor(s2cStub: SevenDSGameS2C_Shop.Stub)` (índice 46863).

Conclusão sustentada: existe um candidato estrutural diretamente compatível com os delegates de cobrança em `Billing_PacketHandler`. Não há prova de registro ou invocação dos callbacks, adaptador, versão, formato de mensagens, autenticação nem servidor jogável.

Dados derivados do arquivo de metadata com SHA256 `eea7a31712bfca44caaa85cee3874ae9092a035556fcdef10f6c6a1fe156448b`. Nenhum binário proprietário nem segredo incluído. Trilha cliente: novo marco estrutural. Trilha servidor: não demonstrada.
