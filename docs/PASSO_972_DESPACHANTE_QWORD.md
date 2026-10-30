# PASSO 972 — Redução algébrica de despachante indireto

**Aprovado estaticamente em bytes reconstruídos**. Controle em RVA `0x6D8161C`: bytes `FF 20` = `JMP QWORD PTR [RAX]`.

Trecho anterior:
```asm
0x6D815E5: SHL RBX,3
0x6D815E9: ADD RAX,0x7F9D07D3
0x6D815EF: ADD RAX,0x6FEB7ADF
0x6D815F5: ADD RAX,0x3AC71834
0x6D815FB: SUB RAX,0x7E7729EF
0x6D81601: ADD RAX,RBX
0x6D81604: ADD RAX,0x7E7729EF
0x6D8160A: SUB RAX,0x3AC71834
0x6D81610: SUB RAX,0x6FEB7ADF
0x6D81616: SUB RAX,0x7F9D07D3
0x6D8161C: JMP QWORD PTR [RAX]
```
As constantes de ADD/SUB se cancelam, portanto em ausência de efeitos colaterais/aliasing a expressão simplifica para `RAX_final = RAX_inicial + 8 * RBX_inicial` (módulo 2^64) a partir de 0x6D815E5, e a instrução final lê o ponteiro de 8 bytes nesse endereço. **A base RAX, o índice RBX e o ponteiro final real são desconhecidos; tabela de despacho é uma hipótese, não dado confirmado.** Nenhuma execução real da cadeia.

SHA-256 integral da saída `.vdata`: `60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3`. Os bytes proprietários não foram versionados.