# GrandCross Local — Checkpoint 2216: vínculos tipados entre handlers e stubs

## Marco novo, confirmado por análise estática

Na cópia do `global-metadata.dat` (IL2CPP v29), os **49** tipos terminados em `_PacketHandler` têm exatamente um construtor identificado na tabela de métodos, com **um argumento**. O índice de tipo deste argumento foi resolvido pelo campo `byvalTypeIndex` da tabela `Il2CppTypeDefinition`.

**49/49 associações de construtor resolvidas nominalmente**, distribuídas em oito famílias de stub:

| Tipo real do argumento do construtor | Handlers |
| --- | ---: |
| `SevenDSGameS2C.Stub` | 29 |
| `SevenDSRelayR2C.Stub` | 8 |
| `SevenDSGameS2C_Pvp.Stub` | 5 |
| `SevenDSGameS2C_Shop.Stub` | 3 |
| `SevenDSGameS2C_Weapon.Stub` | 1 |
| `SevenDSWestS2C.Stub` | 1 |
| `SevenDSGameS2C_Guild.Stub` | 1 |
| `SevenDSGameS2C_Stage.Stub` | 1 |

Exemplo central: `Auth_PacketHandler..ctor(s2cStub)` tem índice de tipo **46857**, resolvido diretamente como `SevenDSGameS2C.Stub`. Essa informação, combinada com o checkpoint 2210 (24/24 correspondências nominais entre handlers de autenticação e `ProcessReceivedMessage_*`), estabelece uma **associação estrutural tipada** entre a classe de autenticação e a família de stub de mensagens S2C.

A assinatura dos métodos de processamento de stub inclui `__msg: Nettention.Proud.Message`, `pa: Nettention.Proud.ReceivedMessage`, `hostTag: System.Object` e `remote: Nettention.Proud.HostID`, de acordo com índices de tipo resolvidos por metadata.

## Limitações explícitas
- Declarações de construtor e correspondências nominais não comprovam que os métodos chamem uns aos outros em execução; não confirmamos registro de callbacks, IDs RMI ou formatos de pacote.
- Não se inferem servidores reais ou conexões simultâneas a partir das oito famílias de stub.
- Índices 24537 (`remotes`) e 13538 (`apInfoList`) continuam sem resolução nominal por `byvalTypeIndex`; demandam outros dados do runtime.
- O servidor Python continua um protótipo HTTP **não validado** com o cliente Grand Cross.

## Próxima prova de maior valor
Comprovar o registro ou chamada de handlers pelo stub no código compilado, ou obter uma demonstração independente de despacho local com dados sintéticos. Publicar apenas evidências derivadas e analisadores próprios, nunca binários ou metadata bruta.

**Trilhas:** análise do cliente — marco estrutural comprovado; servidor local funcional — nenhuma compatibilidade demonstrada.
