# GrandCross Local — checkpoint 2424: auditoria de setters de eventos

Auditoria estática em cópia de ProudNetClientPlugin.dll, sem execução ou alteração do jogo. A tabela PE contém **17 exportações** `CSharp_NetClientEvent_SetCallback*`. Para todas as 17, bytes nativos confirmam instruções de armazenamento de segundo argumento x64 em campo do objeto, seguidas de retorno. Os offsets são **17 posições consecutivas de 8 bytes entre +0x18 e +0x98**, dentro do tamanho `0xA0` solicitado pelo construtor `CSharp_NativeToNetClientEventWrap_New` (RVA 0x9A10).

**Errata de exclusividade dos setters:** três exports de RmiStub compartilham **exatamente o mesmo RVA de código** com setters NetClientEvent: `GetRmiIDList` ↔ `P2PMemberJoin` (0x9C00), `GetRmiIDListCount` ↔ `P2PMemberLeave` (0x9C10), `ProcessReceivedMessage` ↔ `ChangeP2PRelayState` (0x9C20). Reutilização de implementação de escrita em offset **não demonstra que os objetos ou usos do jogo sejam os mesmos**.

**Status:** contratos nativos de 17/17 campos verificados, com três aliases de endereço identificados. Não foi observada utilização real pelo Grand Cross, serialização de mensagens, autenticação, handshake ou servidor local funcional. Sem binários proprietários publicados.

Materiais reproduzíveis locais: `gc_2417_2424_event_setter_audit.py`, `GrandCross_2417_2424_event_setters.json`, `GrandCross_Local_CHECKPOINT_2424.md`.