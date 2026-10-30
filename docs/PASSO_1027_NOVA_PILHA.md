# PASSO 1027 — Nova entrada de manipulação de pilha

**Aprovado por leitura estática. PASSO 1028 ainda não executado.** Na nova .vdata (SHA256 `72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231`):

- `.vdata+0xF4FAC`: `JMP .vdata+0xF4FA7` (salto para trás cinco bytes).
- `.vdata+0xF4FA7`: `JMP .vdata+0x2E5CAF`.
- `.vdata+0x2E5CAF`: `PUSHF; PUSH RDI; PUSH RDI; MOV RDI,[RSP]; PUSH R13; MOV R13,RSP; ADD R13,8; ADD R13,8; XCHG [RSP],R13; POP RSP; ...`.
- A presença de `POP RSP` impede inferir estado posterior sem rastrear o layout da pilha. Este passo para antes de identificar o próximo controle.
- O objetivo 2 continua EM ANDAMENTO; nenhuma execução real do cliente ou inicialização IL2CPP foi demonstrada.

Próximo PASSO 1028: ampliar desmontagem do bloco com limites, inventariar possíveis transferências de controle e propriedades da pilha. Nenhum binário proprietário versionado.
