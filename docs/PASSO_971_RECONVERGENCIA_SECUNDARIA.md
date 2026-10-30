# PASSO 971 — Desdobramentos da segunda condição

**Aprovado em análise estática, com limites.**
- RVA 0x6D81060: `JE 0x6D81076`; fallthrough 0x6D81066.
- A trilha linear a partir da entrada tomada `0x6D81076` alcança o controle já identificado em `0x6D81492`, verificando compartilhamento de endereço com a outra saída do desvio em 0x6D80FF6.
- Na trilha não tomada a partir de 0x6D81066, observou-se um `JMP` em `0x6D81071`, destino RVA `0x6D81081`; ainda não se percorreu esta transferência.
- Essa análise não comprova fluxo real, convergência dinâmica nem igualdade de registradores.