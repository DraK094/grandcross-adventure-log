# GrandCross Local — checkpoint 2230: exceções e vínculos cruzados entre famílias de stub

## Método reproduzível
Reanálise do metadata IL2CPP v29 de 49 handlers. Foram revalidadas 1.388 correspondências entre um método do handler, campo de mesmo nome no stub declarado no construtor e método `ProcessReceivedMessage_<nome>` no mesmo stub. Dos 1.448 métodos de handlers selecionados, **60 não atendem ao critério estrito**. Esses 60 foram comparados com todas as famílias de stubs `SevenDS*` presentes na tabela de tipos.

## Novo resultado
**8 dos 60** métodos sem tríade no stub esperado possuem uma tríade nominal completa em **outro stub**: o `SevenDSGameS2C.Stub`. São sete métodos de `Shop_PacketHandler` (incluindo mensagens de cobrança) e um método de `ArenaTagPvp_PacketHandler` (`CG_RequestArtifactArenaTagTeamChangeOK`). Os 52 restantes não apresentaram o padrão de campo+despachante em qualquer stub da coleção pesquisada.

Isso **corrige uma inferência anterior**: um handler pode declarar no construtor um stub específico e ainda conter nomes de métodos cuja tríade correspondente existe em outra família. Não é correto modelar todos os métodos de um handler como vinculados exclusivamente ao stub recebido no construtor.

## Estado da comprovação
Comprovado: correspondências de nomes e tipos declarados em metadata, incluindo oito correspondências entre famílias distintas.
Não comprovado: que os oito métodos realmente registrem callbacks em outro stub, que sejam invocados em execução, IDs RMI, formato de mensagens, autenticação ou compatibilidade com servidor local jogável.

**Trilha de análise do cliente:** mapa de associações corrigido, nova hipótese verificável. **Trilha de servidor funcional:** inalterada. Não subir binários proprietários, dados de contas ou segredos.
