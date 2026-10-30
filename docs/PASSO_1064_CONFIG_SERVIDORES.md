# PASSO 1064 — Inventário textual de configuração de servidores

**APROVADO somente para busca textual.** O usuário encontrou referências no `global-metadata.dat` a `ServerSelectPopup`, `ItemServerSelectButton`, `OnClickServerSelect`, `m_goServerSelect`, e caminhos `Assets\\SevenSins\\Scripts\\UI\\Popup\\ServerSelectPopup.cs` e `Assets\\SevenSins\\Scripts\\UI\\GridItems\\ItemServerSelectButton.cs`.

Outros termos: `serverIP` 11 correspondências, `serverPort` 16, `protocolVersion` 13, `ServerInfo` 57, `ServerList` 1 (somente `DnsServerList`), `ServerConfig` 0, `ServerSelect` 8, `Region` 717, `Endpoint` 170, `NetworkManager` 1, `NetConnectionParam` 12 e `ProudNetClientPluginPINVOKE` 1. Números representam coincidências textuais, não entidades únicas.

**Interpretação:** o cliente contém indícios de UI de seleção de servidor e interface genérica de configuração de IP/porta. Isso não comprova que se pode adicionar uma região, apontar para localhost ou que há backend próprio implementado. Próxima etapa: contextualizar especificamente nomes de seleção/servidores e identificar se pertencem ao código do jogo.

Servidor local: não demonstrado. PASSO 1065 pendente.