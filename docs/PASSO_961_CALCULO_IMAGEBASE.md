# PASSO 961 — Auditoria da cadeia de retorno e ImageBase

**Aprovado em análise estática.** PASSO 962 ainda não executado. DLL fornecida analisada read-only. Reconstrução integral: 14.131.200 bytes e SHA256 `60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3`.

## Bytes e fluxo decodificados
- `.vdata+0x1CC32`: `PUSH RBP`; +0x1CC33 `JMP .vdata+0x29F32`.
- `.vdata+0x29F32`: `CALL .vdata+0x1C2E97`; lá `JMP .vdata+0x1CC38`; neste local `POP RBP`.
- `.vdata+0x1CC39`: `JMP .vdata+0x4502C`; lá `SUB RBP, 0x29F37` e `JMP .vdata+0x29F3C`.
- `.vdata+0x29F3C`: `CALL .vdata+0x1A3A19`; lá `JMP .vdata+0x46026`; neste local `POP RAX`.
- `.vdata+0x46027`: `JMP .vdata+0x5A86B`; lá `SUB RAX,0x6AACF41` seguido por `JMP .vdata+0x30E789`; este último endereço agora recuperado e contém `JMP RVA 0x6ABF4B0`.
- Sete transferências de controle diretas do caminho foram verificadas por decodificação de `E8/E9 rel32` e cálculo aritmético dos destinos. Outras instruções e transições observadas via `objdump`.

## Propriedade matemática
- CALL de +0x29F32 colocaria na pilha o endereço `0x186AACF37`. `POP RBP; SUB RBP,0x29F37` resultaria em **base da seção .vdata `0x186A83000`**, sob os pressupostos de pilha intacta.
- CALL de +0x29F3C colocaria na pilha `0x186AACF41`. `POP RAX; SUB RAX,0x6AACF41` resultaria em **ImageBase PE `0x180000000`**, sob os pressupostos de pilha intacta.
- Os alvos de ambas as CALLs antes inacessíveis são stubs `JMP`, não corpos convencionais de função; os retornos podem ser consumidos em outro ponto da cadeia.

## Limites e retomada
As relações são **estáticas e condicionais ao estado da pilha**, não evidência de execução do segundo estágio nem de CodeRegistration, MetadataRegistration ou servidor jogável. Não foram escritos arquivos proprietários no repositório.

PASSO 962 recomendado: rastrear a cadeia de JMP a partir do RVA `0x6D91789`, com controle de ciclos e limites, e observar até a primeira instrução não-JMP, sem executar código.

[960](PASSO_960_CHAMADAS_RESOLVIDAS.md) · [959](PASSO_959_RECONSTRUCAO_INTEGRAL.md) · [backup 957](BACKUP_TECNICO_PASSO_957.md).