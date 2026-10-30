# PASSO 970 — Primeiros controles dos dois ramos da condição em 0x6D80FF6

**Aprovado — análise estática.**
- Tomado: início 0x6D811E7, próximo controle em `0x6D81492`: `JE 0x6D815BE`.
- Não tomado: início 0x6D80FFC, próximo controle em `0x6D81060`: `JE 0x6D81076` (fallthrough 0x6D81066).
- As instruções foram identificadas na desmontagem e destinos JE recalculados a partir dos bytes. Nenhum desses caminhos foi executado com estado do cliente.