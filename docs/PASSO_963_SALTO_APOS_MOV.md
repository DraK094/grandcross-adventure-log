# PASSO 963 — Salto após MOV RAX,RAX

**Análise estática aprovada. PASSO 964 ainda não executado.** Dados da .vdata integral de 14.131.200 bytes, SHA256 `60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3`.

- RVA `0x6DA5F72`: `48 89 C0` = `MOV RAX,RAX`, não altera o valor arquitetural de RAX.
- RVA `0x6DA5F75`: `E9 12 00 00 00` = `JMP RVA 0x6DA5F8C`.
- RVA `0x6DA5F8C`: `E9 61 3A F5 FF` = `JMP 0x186CF99F2` (RVA `0x6CF99F2`).
- O caminho permanece inteiramente dentro da seção recuperada; próximos saltos não executados.

**Limites:** não há demonstração de execução real, CodeRegistration/MetadataRegistration localizados ou servidor offline funcional. Nenhum binário proprietário versionado. PASSO 964 deve continuar inspeção estática antes de inferir semântica.

[PASSO 962](PASSO_962_TRAMPOLINS.md) · [PASSO 961](PASSO_961_CALCULO_IMAGEBASE.md).