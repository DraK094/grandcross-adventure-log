# PASSO 974 — Caminhos para a transferência indireta

**APROVADO estaticamente.** No ramo não tomado do JE em RVA 0x6D81492, a desmontagem linear chega ao novo site em `0x6D81526`, com `JE RVA 0x6D81573`. Continuando pelo destino tomado `0x6D81573`, o primeiro controle registrado é em `0x6D8161C`, `JMP QWORD PTR [RAX]`, mesmo site identificado no PASSO 972 ao seguir o ramo tomado de 0x6D81492.

**Ponto de bloqueio de interpretação:** o endereço do ponteiro e seu destino real dependem de `RAX`, `RBX` e possíveis efeitos sobre pilha/memória ao longo do caminho real. Mapeamento linear não equivale a execução. Não foi localizado CodeRegistration nem demonstrado servidor funcional.

Reproduzido com `grandcross_audit_966_967.py`, arquivo Python de auditoria mantido como artefato separado de conversa. Fonte: 14.131.200 bytes .vdata, SHA256 60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3.