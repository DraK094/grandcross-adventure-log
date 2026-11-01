# GrandCross Local — Checkpoint 2408: revisão das tabelas ProudNet

**Análise estática reproduzível de ProudNetClientPlugin.dll; somente leitura.** A análise dos passos 2401–2408 corrige a interpretação anterior de que a região do grupo A em RVA `0x10248` seria uma tabela independente de três entradas.

- Os três endereços `0x10F0`, `0x1100`, `0x1110` ocupam os slots `0x10248`, `0x10250`, `0x10258` de uma sequência **mais extensa** de 15 ponteiros de código validados em `0x10220..0x10290`. Não está comprovado onde começam/terminam as estruturas lógicas ou quem as inicializa.
- A função construtora do wrapper em `0x9AA0` associa o endereço de `.rdata` `0x10298` ao offset `+0x0` e **também** a tabela `0x102E0` ao offset `+0x18`. Isso foi conferido nos bytes das instruções em RVAs `0x9AD9`, `0x9AE0`, `0x9AE3` e `0x9AEA`. Os slots `+0x28`, `+0x30` e `+0x38` são zerados na mesma rotina.
- A rotina RVA `0x1320` usa a tabela `0x10298` no offset `+0` e uma **outra** tabela `0x100E8` no offset `+0x18`, indicando variantes estáticas de inicialização, **não** identidade comprovada de instância.
- Auditoria reproduzida: 15 ponteiros consecutivos e 11 sequências de instruções verificadas, sem execução do cliente.

**Limites:** contiguidade não prova uma vtable única, não foi demonstrado construtor do grupo A, chamada real pelo Grand Cross, formato RMI, login, servidor local compatível ou jogabilidade. Sem publicação de binários proprietários.

Arquivos derivados locais: `gc_2401_2408_tables_revision.py`, `GrandCross_2401_2408_evidencias.json`, `GrandCross_Local_CHECKPOINT_2408.md`.

O próximo passo é inspecionar a região `0x10220` no contexto de RTTI/relocações e identificar, se possível, referências efetivas ao objeto que contém seus slots.