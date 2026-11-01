# GrandCross Local — Checkpoint 2393: referências de trampolins em .rdata

Auditoria estática, somente leitura, do `ProudNetClientPlugin.dll` (SHA-256 `91ef8ef7624491d1598f0f5ef31b83fa62a0e2a45a8324ebdb8b7edb43bd845c`). Foram localizadas **seis referências de ponteiro de 64 bits** na seção `.rdata`, cada uma contendo exatamente `ImageBase + RVA` de um dos seis trampolins de salto indireto previamente identificados.

| Grupo | RVA do código | RVA da referência em `.rdata` |
|---|---|---|
| A | 0x10F0, 0x1100, 0x1110 | 0x10248, 0x10250, 0x10258 |
| B | 0x1370, 0x1380, 0x1390 | 0x10298, 0x102A0, 0x102A8 |

Os ponteiros são contíguos em cada grupo, dando evidência de tabelas estáticas de funções/trampolins; **não** está comprovado que as estruturas referenciadas por essas tabelas sejam as mesmas nas quais os setters RMI gravam callbacks em offsets 0x28/0x30/0x38. Também não está demonstrado registro ou execução pelo Grand Cross, protocolo, autenticação ou servidor jogável.

Reprodução local: `gc_2389_2393_pointer_tables.py` e `GrandCross_2389_2393_pointer_tables.json`. Nenhum binário proprietário publicado. Trilha análise do cliente: avanço de organização de referências nativas. Trilha servidor funcional: inalterada.