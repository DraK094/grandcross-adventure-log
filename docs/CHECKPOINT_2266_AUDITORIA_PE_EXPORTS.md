# Checkpoint 2266 — auditoria PE32+ e limite de análise estática

Auditoria somente-leitura da cópia de `GameAssembly.dll`, PE32+ com 14 seções, entrada `RVA 0x0785C058` na seção `.boot`.

**Comprovado por leitura da tabela PE:** o arquivo possui **384 exportações nomeadas**, incluindo **239** com prefixo `il2cpp_`. O diretório de exportações `.edata` é legível, porém **384/384 endereços de implementação exportados recaem na faixa virtual não representada pelos bytes raw de sua seção**. Isso inclui `il2cpp_init`, `il2cpp_domain_get` e `il2cpp_runtime_invoke`.

O diretório PE de tratamento de exceções `RVA 0x0718602C` encontra-se em `.vdata`, seção cujo tamanho raw é zero. O ponto de entrada na `.boot` tem bytes armazenados.

**Interpretação:** os endereços exportados existem no mapa da imagem, mas os corpos correspondentes **não podem ser extraídos diretamente dos bytes dessa cópia em disco**. Não demonstramos como a imagem é materializada em execução nem que exista um empacotador específico. Essas evidências não comprovam o vínculo real de delegates aos handlers.

**Trilha do cliente:** barreira estática delimitada. **Servidor local:** compatibilidade com o Grand Cross não demonstrada. Não publicar binários proprietários ou dados de conta. Reprodutibilidade local: `gc_2261_2266_pe_audit.py`, `GrandCross_2261_2266_PE_evidence.json`, `GrandCross_Local_CHECKPOINT_2266.md`.
