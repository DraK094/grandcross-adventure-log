# PASSO 966 — CALL rel32 zero e início da sequência de pilha

**Aprovado estaticamente em 29/10/2026.** .vdata reconstruída: 14.131.200 bytes; SHA256 60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3.

Entrada RVA `0x6D80A55`: bytes `E8 00 00 00 00` = CALL à próxima instrução `0x6D80A5A`. Uma CALL x86-64 empilha o endereço de retorno de 64 bits, mesmo quando o alvo é a instrução seguinte. Em `0x6D80A5A` há `PUSH RCX`, seguido por `PUSH RSP; POP RCX` e operações com pilha; assim, a hipótese de manipulação proposital de endereços e estado de pilha é consistente com os bytes, mas **sem validação dinâmica do estado**.

O bloco é mais longo do que a janela inicial de desmontagem, e requer evitar conclusões sobre o fluxo até a primeira transferência de controle. Nenhuma alteração feita na DLL. Nenhuma evidência de CodeRegistration ou servidor funcional.
