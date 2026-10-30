# PASSOS 1031–1035 — Bifurcações e despachante, versão atual

Data 30/10/2026. Cinco verificações estáticas aprovadas. Último 1035; próximo 1036 ainda não executado.

SHA256 da saída vdata integral: 72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231.

1031: TEST EDX,EDX RVA 0x6DF3E2C; JE RVA 0x6DF3E2E, tomado 0x6DF3F79, não tomado 0x6DF3E34.

1032: ambos caminhos na desmontagem linear atingem JE comum RVA 0x6DF3FB2; alvo 0x6DF418B, fallthrough 0x6DF3FB8. Sem equivalência dinâmica provada.

1033: 0x6DF402F JE 0x6DF4045; 0x6DF43F0 JE 0x6DF4544.

1034: 0x6DF4040 JMP 0x6DF4050; caminho 0x6DF4045 atinge 0x6DF43F0; 0x6DF44A0 JE 0x6DF44DC; 0x6DF45A0 JMP QWORD PTR [RAX].

1035: antes do salto indireto, valores originam de [RSP+0x88] e índice RBX, SHL RBX,3; constantes ADD/SUB em RAX cancelam-se. Expressão local RAX_após_pilha + 8×RBX_índice, módulo 64 bits. Conteúdo e destino real da tabela não determinados.

Somente Python/objdump sobre bytes reconstruídos da DLL fornecida, sem execução real. Inicialização completa IL2CPP não demonstrada. Objetivo 2 EM ANDAMENTO. Próximo 1036: rastrear valores de pilha e ramos alternativos. Não subir DLL/saída proprietária.