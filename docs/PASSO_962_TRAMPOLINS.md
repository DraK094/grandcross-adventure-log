# PASSO 962 — Trampolins diretos após cálculo de ImageBase

**Status:** aprovado estaticamente; PASSO 963 ainda não executado.

Reconstrução integral reproduzida, SHA256 `60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3`. Rastreamento byte-a-byte sem executar o segundo estágio:

1. RVA `0x6D91789`: bytes `E9 22 DD D2 FF` = `JMP 0x6ABF4B0`.
2. RVA `0x6ABF4B0`: bytes `E9 BD 6A 2E 00` = `JMP 0x6DA5F72`.
3. RVA `0x6DA5F72`: bytes começam por `48 89 C0` = `MOV RAX,RAX`, depois `E9 12 00 00 00` = JMP. A busca limitada a JMP na primeira instrução para aqui; próximo passo deverá tratar o MOV e o JMP posterior, sem inferir execução.

**Resultado:** 2 transferências JMP diretivas sucessivas confirmadas, parada no primeiro opcode não-JMP. Salto real do cliente não executado. Não há CodeRegistration, backend ou servidor jogável confirmado. Sem binários proprietários no GitHub.

[PASSO 961](PASSO_961_CALCULO_IMAGEBASE.md) · [PASSO 959](PASSO_959_RECONSTRUCAO_INTEGRAL.md).