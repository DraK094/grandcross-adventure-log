# GrandCross Local — checkpoint 2233 (classificação das exceções)

## Escopo da revisão

A análise anterior cobria 1.448 métodos de 49 tipos terminados em `_PacketHandler`; 1.388 possuem tríade nominal com o stub declarado no construtor, 8 têm tríade apenas em outra família de stub, e **52** continuam sem tríade em todas as famílias `SevenDS*.Stub` examinadas.

## Resultado novo — classificação das 52 exceções

A partir da lista estruturada preservada em `GrandCross_2229_exceptions.json`, classificação baseada em convenção nominal:

- **21 métodos de nomes auxiliares/internos**, sem prefixo de mensagem reconhecido (por exemplo, `ProcessGacha`, `RefreshFate`, `StageStartOKCommonHandlerBegin`, `UpdateEventStagePlayCountsByDailyReset`).
- **31 métodos com nomes semelhantes a mensagens**, com prefixo `CG_`, `GC_` ou `RC_`, porém **sem campo de mesmo nome e sem método `ProcessReceivedMessage_<nome>`** em nenhuma das famílias de stubs pesquisadas.
- Os 31 incluem: 10 de `ArenaRealTimePvp_PacketHandler`, 5 de `Skin_PacketHandler`, 4 de `Lobby_PacketHandler`, 3 de `Stage_PacketHandler` e 9 distribuídos entre outros handlers.

**Limite metodológico:** “auxiliar/interno” é classificação por **nome**, não função confirmada. A ausência de correspondência nas famílias `SevenDS*.Stub` **não prova** que uma mensagem seja código morto, nem descarta um despacho alternativo, gerações de protocolos diferentes ou diferenças de versão entre classes.

## Interpretação prudente
A divisão dos 52 métodos em dois conjuntos verificáveis fornece uma lista de lacunas priorizadas, mas **não representa** um avanço de funcionalidade do servidor. Prioridade seguinte: conferir os identificadores de mensagens dos stubs gerados e estabelecer prova de chamadas/associação real, sem inventar serialização ou fazer conexão a serviços de produção.

## Rastreabilidade
Dados derivados de `global-metadata.dat` IL2CPP v29, com parser das tabelas de tipos, métodos e campos. Nenhum binário proprietário ou segredo incluído.

**Trilhas:** análise do cliente — classificação melhorada; servidor local jogável — sem compatibilidade comprovada.
