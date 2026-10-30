# PASSO 1005 — Unificação comprovada dos estudos 942–950 e 1001–1004

**PASSO 1005 APROVADO por cálculo exato de endereços e confronto com backup histórico, 30/10/2026. Próximo 1006 ainda não executado.**

A seção .vdata possui RVA `0x06A83000`. Portanto, `RVA = 0x06A83000 + OFFSET_DA_VDATA`.

| Local | Offset histórico .vdata | RVA moderno | Identidade |
|---|---|---|---|
| JE anterior ao loop (PASSO 944) | 0x2FE492 | **0x6D81492** | Igual ao PASSO 1001 |
| Início do loop (PASSO 942) | 0x2FE523 | **0x6D81523** | Igual ao PASSO 1003 |
| Saída do loop | 0x2FE573 | **0x6D81573** | Igual à saída local |
| Início do despacho (PASSO 943) | 0x2FE5BE | **0x6D815BE** | Igual à entrada estudada no PASSO 1004 |
| JMP indireto (PASSO 950) | 0x2FE61C | **0x6D8161C** | Igual ao PASSO 972/991 |

**Descoberta histórica:** o contador EBX=1652 demonstrado estaticamente no PASSO 1002 é o **mesmo laço** cujas 1652 iterações foram emuladas com estado sintético no PASSO 942 — não apenas uma coincidência numérica. O PASSO 950 usou destinos fabricados; NÃO identificou os destinos reais do cliente. O PASSO 1005 conecta a análise estática atual à emulação sintética antiga e amplia o grau de confiança sobre a interpretação do trecho, **mas não valida execução real com estado do jogo**.

SHA-256 da reconstrução integral usada em 1001–1004: `60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3`.

**Objetivo 2: EM ANDAMENTO.** Para completá-lo, ainda é necessário comprovar o encadeamento completo de entrada, os estados de registradores e pilha, e transição para inicialização real IL2CPP. `global-metadata.dat` será útil na etapa de registros, porém não substitui estado dinâmico. Nenhum servidor offline funcional demonstrado.

[Experimentos anteriores: backup 957](BACKUP_TECNICO_PASSO_957.md) · [1001–1004](PASSOS_1001_1004_CONTADOR_1652.md).
