# PASSO 1065 — Contexto textual do seletor de servidores

Resultado do usuario: 3 ocorrencias `ServerSelectPopup` (inclui fonte `Assets\SevenSins\Scripts\UI\Popup\ServerSelectPopup.cs`), 3 `ItemServerSelectButton` (inclui `SelectWorld` e fonte `Assets\SevenSins\Scripts\UI\GridItems\ItemServerSelectButton.cs`), 1 `OnClickServerSelect` proxima de `PageLogin`, 1 `m_goServerSelect` proxima de `WEB_SERVER_URL_REAL`, `WEB_SERVER_URL_DEV`, `CheckNetworkConnection` e `CheckConfiguration`.

`serverIP_` e `serverPort_` perto de `ConnectToWestSideServer`, `RequestConnectToWestSideServer`, `RequestChannelJoin`, `OnWestSideInfoReceivedOK`. Separadamente, `get_ServerIP` e `get_ServerPort` perto de `get_IsReconnect` e `get_LeaderUsn`. `NetConnectionParam_serverIP_set` e `NetConnectionParam_serverPort_set` proximos da camada ProudNetClientPluginPINVOKE.

**PASSO 1065 APROVADO APENAS PARA CONTEXTO TEXTUAL.** Proximidade na string heap IL2CPP nao comprova mesma classe, fluxo, capacidade de trocar servidor, nem jogo offline. PASSO 1066 pendente: fazer pesquisa direcionada em tabelas estruturadas ou nomes completos, visando mapear tipos e metodos com evidencias, sem alterar cliente.
