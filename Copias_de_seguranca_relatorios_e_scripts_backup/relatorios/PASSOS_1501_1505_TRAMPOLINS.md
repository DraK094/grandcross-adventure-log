# GrandCross Local — passos 1501–1505

Fonte: bytes x64 do PASSO 1501 fornecidos pelo usuario, desmontados offline com objdump.

- `0x3BE9A0`: `E9 DB 8D FA FF`, salto incondicional para `0x367780`. A entrada vizinha `0x3BE9B0` move RDX para RCX e salta ao mesmo destino; nao confundir com a entrada principal.
- `0x3BEA30`: `mov edx, edx; jmp 0x36E690`. Portanto a criacao observada nos Common.ccctor depende do alvo 0x36E690.
- `0x412F170`: verifica RCX nulo, chama 0x3078510 com RDX e R8 zerados, e sob condicao salta para `0x3C13E0`. Nao classificar esta funcao definitivamente como inicializacao ou preenchimento de lista.
- O bloco de 96 bytes de cada funcao pode abranger funcoes vizinhas apos os bytes CC. Os argumentos 6/14 dos Common.ccctor continuam nao identificados como contagens RMI.

Proxima leitura direcionada: inicio dos destinos 0x367780, 0x36E690 e 0x3C13E0, sem execucao de codigo ou modificacao de memoria. Nenhum ID RMI numerico confirmado e nenhum login local funcionando.
