# GrandCross Local — PASSOS 1265–1268

Leituras de memoria fornecidas pelo usuario: duas amostras de 48 bytes (funcoes RVA 0x421794 e 0x347DE0), e 32 bytes da referencia RVA 0x508CD3F. Disassembly x64 confirma `call rel32` na primeira funcao RVA 0x4217A5 apontando para RVA **0x42DB50**, sem cobertura bruta da secao 0. Na segunda funcao, `lea r12,[rip+0x5FDBE98]` no RVA 0x347E01 aponta para RVA **0x6323CA0**, secao 3, sem cobertura bruta. A amostra termina no meio da proxima instrucao; nao se atribui destino sem dados adicionais.

A referencia de memoria em RVA 0x508CD3F exibe byte NUL seguido pelo prefixo ASCII `Cannot marshal field 'socket' o`, enquanto os bytes do PE bruto no RVA correspondente sao diferentes. Nao e comprovacao de CodeGenModule ou MethodPointer. Nao ha ainda codigo dos serializadores de login ou IDs RMI.

Scripts e relatorios locais gerados: `grandcross_steps_1265_1268.py`, `GrandCross_PASSOS_1265_1268_Relatorio.md`, `GrandCross_PASSOS_1265_1268_Evidencias.json`. Os alvos citados sao candidatos a novas verificacoes, nao identificacoes semanticas.