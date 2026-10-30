# PASSO 965 — Auditoria do bloco de pilha (29/10/2026)

**Passo 965 aprovado em análise estática. PASSO 966 ainda não executado.**

## Evidências
- DLL original lida somente leitura. Reconstrução integral da .vdata (14.131.200 bytes): SHA256 `60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3`, validado na execução local.
- Entrada RVA `0x6DAB5AE`: `9C` = PUSHF.
- Três `POP RSP` em RVAs `0x6DAB65B`, `0x6DAB69A` e `0x6DAB6D6`. O passo anterior mencionava dois, a varredura expandida identificou o terceiro.
- `objdump` decodificou **99 instruções em sequência linear** até a primeira transferência explícita encontrada.
- RVA `0x6DAB6FF`: bytes `E9 51 53 FD FF` = `JMP RVA 0x6D80A55` (VA `0x186D80A55`).
- Bloco tem operações PUSH, POP, XCHG e MOV de endereços relativos à pilha, exigindo valores iniciais para determinar efeitos.
- Auditoria reproduzível via `grandcross_audit_965.py` no ambiente de análise. Nenhum executável ou dado proprietário versionado.

## Limites
A leitura é **estática linear**: não prova que o cliente real execute as 99 instruções, nem determina valores na pilha. O JMP foi decodificado mas não executado. CodeRegistration/MetadataRegistration, execução do segundo estágio e servidor offline funcional **ainda não demonstrados**.

## Retomada
PASSO 966 sugerido: inspecionar estaticamente o bloco em RVA `0x6D80A55`, encontrar a próxima transferência de controle e validar byte a byte, sem presumir execução real.

[PASSO 964](PASSO_964_PILHA_OFUSCADA.md) · [PASSO 959](PASSO_959_RECONSTRUCAO_INTEGRAL.md).