# PASSO 964 — Trampolim e prólogo com manipulação de pilha
**Aprovado em análise estática. PASSO 965 ainda não executado.**
- DLL original 47.199.760 bytes lida somente leitura. .vdata integral reconstruída: 14.131.200 bytes, SHA-256 `60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3`.
- RVA `0x6CF99F2`: bytes `E9 B7 1B 0B 00` = `JMP RVA 0x6DAB5AE`.
- RVA `0x6DAB5AE`: byte `9C` = `PUSHF`. Segue código com PUSH, POP, MOV [RSP], SUB RSP, XCHG [RSP] e POP RSP, consistente com manipulação de pilha potencialmente ofuscada.
- Exemplos: RVA `0x6DAB5EE` MOV RCX,0x6AC8038; `0x6DAB5F8` MOV [RSP+8],RCX; `0x6DAB65B` POP RSP; `0x6DAB69A` POP RSP.
- Literal 0x6AC8038 não é prova de destino executado. Nenhuma emulação dinâmica deste bloco; sem evidência de CodeRegistration/MetadataRegistration ou backend offline funcional.
- **Próximo passo 965:** avaliar controle de fluxo e efeitos sobre pilha de forma limitada e estática. Não pedir mais arquivos enquanto DLL for suficiente.
- Não publicar DLL nem bytes proprietários.