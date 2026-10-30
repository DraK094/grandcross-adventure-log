# PASSO 960 — Análise estática de chamadas recuperadas (29/10/2026)

**PASSO 960 aprovado, PASSO 961 ainda não executado.** Verificações sobre a reconstrução integral de 14.131.200 bytes (SHA256: `60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3`), com disassembly x86-64 via objdump, sem execução do segundo estágio.

## Chamadas antes inacessíveis
- `.vdata+0x29F32` RVA `0x6AACF32`: `CALL 0x186C45E97`, destino `.vdata+0x1C2E97` (RVA `0x6C45E97`). Lá: `E9 9C 9D E5 FF` = `JMP 0x186A9FC38`, onde há `POP RBP`. Endereço de retorno teórico do CALL: `0x186AACF37`.
- `.vdata+0x29F3C` RVA `0x6AACF3C`: `CALL 0x186C26A19`, destino `.vdata+0x1A3A19` (RVA `0x6C26A19`). Lá: `E9 08 26 EA FF` = `JMP 0x186AC9026`, trecho anteriormente identificado como `POP RAX`. Endereço de retorno teórico do CALL: `0x186AACF41`.
- A cadeia é compatível com manipulação dos retornos para recuperar o ImageBase, hipótese já discutida no marco 900, **sem execução dinâmica deste segundo estágio**.

## Transferências indiretas
- RVA `0x6A90D01`: bytes `FF E6` = **JMP RSI**.
- RVA `0x6A916E0`: bytes `41 FF E6` = **JMP R14**.
- Sem estado real dos registradores RSI/R14, destinos desconhecidos.

## Limites, segurança e retomada
Nenhum arquivo do cliente foi alterado. Descompressão integral reproduzida e conferida por hash; análise dos destinos é estática. Não há CodeRegistration/MetadataRegistration localizados, segundo estágio executado ou servidor offline funcional. Arquivos proprietários não publicados.

PASSO 961 sugerido: auditar estaticamente os próximos encadeamentos e a aritmética de base, distinguindo byte comprovado, hipótese e execução real.

[Backup 957](BACKUP_TECNICO_PASSO_957.md) · [Passo 959](PASSO_959_RECONSTRUCAO_INTEGRAL.md).
