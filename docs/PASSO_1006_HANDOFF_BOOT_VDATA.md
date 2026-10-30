# PASSO 1006 — Handoff estático .boot → .vdata verificado

**30/10/2026. PASSO 1006 aprovado em auditoria estática de bytes, NÃO execução dinâmica.** Passo seguinte reservado: 1007 (não executado).

## Código verificado na DLL original, .boot
- `.boot+0x58` CALL `.boot+0x1DF` (rel32).
- `.boot+0x1DF` POP RAX, que pode recuperar retorno `0x1877FD05D`.
- `.boot+0x1E6..0x1F2`: `MOV RBX,RAX; SUB RBX,5; MOV ECX,0xD7A058; SUB RBX,RCX` => **RBX=0x186A83000** (=VA base .vdata), sob endereço de carregamento de referência.
- `.boot+0x1F6..0x201`: `MOV EAX,0x1CC32; ADD RAX,RBX; CMP DWORD [RAX],0; JE .boot+0x206`. Caso região não zero, desvia da chamada ao decoder; caso zero, constrói argumentos e `CALL RAX` em `.boot+0x219`.
- `.boot+0x21C..0x22A`: `MOV EAX,0x1CC32; ADD RAX,RBX; POP RBP/RDI/RSI/RDX/RCX/RBX; JMP RAX`. **Destino calculado: 0x186A9FC32 = .vdata+0x1CC32**.
- Auditoria Python `grandcross_auditoria_1006.py` passou verificações por bytes e aritmética, não emulou o cliente. DLL inalterada.

## Significado e limitações
É a primeira validação direta do **encaminhamento estático condicional a partir do estágio .boot para a entrada da região .vdata**. Os ramos e o local de handoff foram demonstrados com bytes; não foram demonstrados sucesso de mapeamento/execução real, estados corretos de pilha, conclusão do caminho ofuscado, registros IL2CPP ou servidor offline.

**Objetivo 2 — Compreender a inicialização do código reconstruído: EM ANDAMENTO.** Para check verde falta investigar do ponto .vdata+0x1CC32 até o runtime inicializado, resolver os controles indiretos e a relação com estruturas IL2CPP.

[PASSO 1005](PASSO_1005_UNIFICACAO_LOOP_942.md) · [PASSOS 1001–1004](PASSOS_1001_1004_CONTADOR_1652.md) · [CHECKPOINT 1000](CHECKPOINT_1000.md).
