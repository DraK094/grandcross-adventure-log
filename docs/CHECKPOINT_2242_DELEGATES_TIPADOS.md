# Checkpoint 2242 — delegates tipados no metadata IL2CPP

## Marco validado: 1.388 relações handler ↔ delegate ↔ stub
Reanálise estática do `global-metadata.dat` (IL2CPP v29). Para cada uma das **1.388 tríades** previamente verificadas (método de `PacketHandler`, campo de mesmo nome em `Stub`, método `ProcessReceivedMessage_*` correspondente), existe uma definição de classe `<NomeDaMensagem>Delegate`. Os campos de stub possuem índice de tipo numérico igual a `byvalTypeIndex+1` da respectiva definição de delegate em **1.388/1.388** casos.

As sequências **ordenadas dos índices de tipo IL2CPP** dos parâmetros de `Delegate.Invoke` e do método de `PacketHandler` correspondente são idênticas em **1.388/1.388** casos. Os nomes dos parâmetros são idênticos em **1.047** casos e diferem em **341**, embora nesses últimos os índices de tipos e sua ordem permaneçam iguais.

### Exemplo reprodutível
- Campo `SevenDSGameS2C.Stub.CG_RequestLoginOK`: tipo índice `71060`
- Classe `CG_RequestLoginOKDelegate`: `byvalTypeIndex=71059`
- `CG_RequestLoginOKDelegate.Invoke`: `remote:35126, rmiContext:44373, userInfo:40152, loginServiceInfo:40148`
- `Auth_PacketHandler.CG_RequestLoginOK`: mesma sequência de nomes e índices

Também verificado em `CG_RequestHeartBeatOK` e `CG_RequestSecurityTokenOK`.

### Limites de evidência
Demonstra estrutura tipada **declarada nos metadados**, não registro efetivo de callbacks, execução, serialização, IDs RMI, rede, autenticação ou compatibilidade com servidor local. As 52 exceções nominais anteriores não foram resolvidas por este cruzamento.

**Trilha cliente:** descoberta substancial. **Trilha servidor funcional:** nenhuma compatibilidade demonstrada. Não publicar binários comerciais nem dados de conta.
