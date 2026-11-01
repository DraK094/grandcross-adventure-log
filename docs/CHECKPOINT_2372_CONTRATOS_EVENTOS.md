# GrandCross Local — Checkpoint 2372

Inspeção estática do metadata IL2CPP v29: quatro eventos que não possuem setters nominais em NetClient têm declarações `NetClientEvent_SetCallback*`, classes `Delegate_*` e assinaturas `Invoke` correspondentes aos métodos `NativeInternalNetClientEvent.On*`.

- `OnReceiveUserMessage` / `Delegate_7`: `(IntPtr obj, Int32 sender, IntPtr rmiContext, IntPtr payload, Int32 payloadLength)`.
- `OnNoRmiProcessed` / `Delegate_12`: `(IntPtr obj, Int32 rmiID)`.
- `OnP2PMemberJoin` / `Delegate_9`: `(IntPtr obj, Int32 memberHostID, Int32 groupHostID, Int32 memberCount, IntPtr message)`.
- `OnChangeServerUdpState` / `Delegate_12`: `(IntPtr obj, Int32 reason)`.

Conferidos 4/4 contratos. Os nomes `payload` e `payloadLength` demonstram uma interface que declara ponteiro e comprimento, **não** revelam formato de pacotes, se a API é usada pelo Grand Cross, nem comprovação de callback executado. `rmiID` é o nome de um parâmetro, não um identificador de mensagem recuperado. Não foi demonstrada sequência de inicialização ou integração do servidor local. Nenhum binário ou dado de conta foi publicado.

Arquivos derivados locais: `GrandCross_Local_CHECKPOINT_2372.md`, `GrandCross_2365_2372_event_contracts.json` e `gc_2365_2372_event_contracts.py`.