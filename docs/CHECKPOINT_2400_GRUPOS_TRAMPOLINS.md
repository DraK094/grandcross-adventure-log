# GrandCross Local — Marco 2400

Auditoria estática de ProudNetClientPlugin.dll: as tabelas `.rdata` em RVA 0x10248 (grupo A) e 0x10298 (grupo B) contêm, cada uma, três ponteiros validados para trampolins nativos. Grupo A: 0x10F0/0x1100/0x1110. Grupo B: 0x1370/0x1380/0x1390.

Varredura de três padrões de `LEA` com endereçamento RIP-relative na seção `.text` encontrou **duas referências diretas** ao grupo B, RVAs 0x132A e 0x9AD9, e **nenhuma correspondência desse tipo** para o grupo A. Isso NÃO prova que o grupo A não tenha referências por outros mecanismos. O checkpoint 2399 já relacionou a inicialização de um wrapper de 64 bytes à tabela B e a campos de callback em +0x28/+0x30/+0x38.

Marco de análise do cliente: tabelas e mecanismos nativos estáticos mais bem delimitados; falta comprovação do uso desses callbacks na execução do Grand Cross. Marco do servidor funcional: **sem handshake, login, jogabilidade ou compatibilidade demonstrados**. Não é justificável atribuir porcentagens exatas ao servidor a partir de números de passos.

Verificação reproduzível: `gc_2400_verify.py` e `GrandCross_2400_evidence.json` (arquivos derivados locais). SHA-256 da DLL analisada: 91ef8ef7624491d1598f0f5ef31b83fa62a0e2a45a8324ebdb8b7edb43bd845c. Nenhum binário ou dado de conta publicado.