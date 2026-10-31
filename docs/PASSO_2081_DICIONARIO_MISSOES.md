# PASSO 2081 — Estado das missões de pacotes (31/10/2026)

**EXECUTADO E VALIDADO** mediante saída PowerShell do usuário. Processo observado: 7dsgc PID 30012; memória lida, não modificada; funções do jogo executadas pelas sondas: 0.

## Cadeia observada
- GameDataContainer VA 0x000002673287BC00, classe VA 0x0000026502F396B0.
- `GameDataContainer.m_state`, offset **0x38**, ponteiro **0x0000026786C59A80**.
- Objeto **State**, classe VA 0x00000265047D4CE0, 108 campos declarados.
- Campo `State.m_dicPackageMissionData` ordinal 62, offset **0x1D8**, FieldInfo TYPEPTR **0x00007FFD05D9D458**. Controle offset encontrado.
- Valor no campo **0x0000026786BF8300**.
- Objeto apontado: **System.Collections.Generic.Dictionary`2**, classe VA **0x0000026503D3DED8**, 14 FieldInfo listados.
- Campos de instância: _buckets +0x10, _entries +0x18, _count +0x20, _freeList +0x24, _freeCount +0x28, _version +0x2C, _comparer +0x30, _keys +0x38, _values +0x40, _syncRoot +0x48. Há quatro campos de nome de serialização com offset 0, não tratá-los como dados de instância.
- Os tipos concretos de chave/valor **não foram recuperados**. Tampouco foram lidos count/entries, nem verificada mutação durante a execução do login.

## Relação com os passos 2078–2080
O processador de item de pacote RVA **0x1C16C20** lê uma estrutura via +0x38 e +0x1D8. A identificação independente de State+0x1D8 como `m_dicPackageMissionData` corrobora o propósito de dados de missões; a identidade do objeto `RCX` no contexto dinâmico do callback **ainda não foi capturada**. Não afirmar gravação do dicionário só pela presença de chamadas a wrappers/delegates.

## Conclusão
**Novo marco verificado de análise do cliente:** existe um dicionário interno de missão de pacotes em State. **Servidor offline/login local:** não há progresso funcional demonstrado. VAs/pid são transitórios e devem ser revalidados após reinício.

**Reunião continua; PASSO 2082 ainda NÃO emitido nem executado.** Próxima pauta: identificar `Dictionary<TKey,TValue>` fechado e sua contagem de entradas, com leitura cuidadosa, somente após aprovar a direção técnica.
