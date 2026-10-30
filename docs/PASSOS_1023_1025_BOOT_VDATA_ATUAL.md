# PASSOS 1023–1025 — Revalidação da cadeia de entrada na DLL atualizada

**1023–1025 aprovados com bytes e disassembly estático. Objetivo 2: EM ANDAMENTO.**

DLL atualizada SHA256 `01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624`; `.vdata` RVA `0x6AE2000`, 14.131.200 bytes reconstruídos, SHA256 `72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231`; `.boot` RVA `0x785C000`.

PASSO 1023: `.boot` calcula base virtual `0x186AE2000` e aponta para novo offset `.vdata+0xA13E` (RVA `0x6AEC13E`), em vez de antigo `+0x1CC32`. As instruções de cálculo e `JMP RAX` foram conferidas nos bytes do PE.

PASSO 1024: `.vdata+0xA13E` começa `PUSH RBP; JMP .vdata+0xCF0BF`. O código de destino é recuperado pelo decoder sem mudança de hash.

PASSO 1025: cadeia de CALL/JMP/POP/SUB verificada: CALL em `+0xCF0BF` e retorno teórico `+0xCF0C4`; `SUB RBP,0xCF0C4` resulta base virtual da `.vdata` se pilha intacta. CALL em `+0xCF0C9`, retorno teórico `0x186BB10CE`; `POP RAX; SUB RAX,0x6BB10CE` resulta ImageBase PE `0x180000000`. São demonstrações estáticas condicionais, **não** execução real.

Próximo PASSO 1026: analisar `.vdata+0xCF0AB` e destino seguinte sem assumir estados. Não foram encontrados registros IL2CPP nem comprovado servidor offline. Nenhuma DLL/asset proprietário incluído.