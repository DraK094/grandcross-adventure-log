# GrandCross Local — checkpoint 2388: setters e saltos indiretos

Auditoria estática, somente leitura, de ProudNetClientPlugin.dll (SHA-256 91ef8ef7624491d1598f0f5ef31b83fa62a0e2a45a8324ebdb8b7edb43bd845c).

Foram validados nove padrões de instruções x64 diretamente nos bytes raw da seção .text.

Setters de callbacks RmiStub: RVA 0x9C00 grava rdx em [rcx+0x28], 0x9C10 em [rcx+0x30] e 0x9C20 em [rcx+0x38], e retornam.

Novo resultado: duas famílias de rotinas com saltos indiretos pelos mesmos deslocamentos. Grupo A: RVAs 0x10F0, 0x1100 e 0x1110, carregam o contexto a partir de [rcx+0x10] e saltam indiretamente via [objeto+0x28/0x30/0x38]. Grupo B: 0x1370, 0x1380, 0x1390, carregam contexto de [rcx+0x20] e saltam via [objeto+0x28/0x30/0x38].

**Comprovado:** instruções de armazenamento e de salto indireto nestes offsets na DLL. **Não comprovado:** identidade da estrutura dos setters com a estrutura dos despachantes, execução das rotinas pelo jogo, destinos reais dos callbacks, IDs RMI, autenticação ou compatibilidade do servidor local.

Trilha de análise do cliente: marco de implementação nativa. Trilha servidor jogável: sem compatibilidade demonstrada. Materiais derivados locais: gc_2383_2388_indirect_dispatch.py, GrandCross_2383_2388_callback_dispatch_evidence.json e GrandCross_Local_CHECKPOINT_2388.md. Nenhum binário proprietário publicado.