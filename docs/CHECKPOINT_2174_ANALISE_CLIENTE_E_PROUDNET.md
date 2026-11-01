# Checkpoint técnico — GrandCross Local — passos 2142–2174

**Origem:** análise independente de cópias dos arquivos do cliente PC e testes locais relatados pelo usuário. **Estado:** evidências estáticas e testes do protótipo; **não** há servidor compatível/jogável validado. Registro adicionado para preservar o histórico após o checkpoint 2081.

## Evidência do cliente atual

- Instalação local relatada: `E:\JOGOS\Netmarble Game\7dsgb`.
- `GameAssembly.dll`: 47.294.480 bytes, SHA-256 `01761332EA33C2FF2C88B3FEA8DA924CD8482D7DFA86B5B02C1C1CB6F1660624`; PE32+ x64, 14 seções, EntryPoint RVA `0x0785C058`, TLS RVA `0x06AE1018`.
- Entrada `.boot`: RVA `0x0785C000`, raw `0x0256EE00`; CALL rel32 do entrypoint aponta para `0x0785C1DF` (raw `0x0256EFDF`). Na rotina, `B9 58 A0 D7 00` e `B8 3E A1 00 00` fundamentam o cálculo `0x0785C058 - 0x00D7A058 + 0xA13E = 0x06AEC13E`, dentro da seção virtual `.vdata` (RVA `0x06AE2000`, virtual size 14.131.200, raw size 0). Finalidade da rotina **não demonstrada**.
- As cópias de `ProudNetClient.dll` (2.396.160 bytes, SHA-256 `E5B197F6F8485BE65C3156D7899A46F8CA08CA62943C4B554BFFE595CED769C9`) e `ProudNetClientPlugin.dll` (146.432 bytes, SHA-256 `91EF8EF7624491D1598F0F5EF31B83FA62A0E2A45A8324EBDB8B7EDB43BD845C`) são idênticas às cópias antigas em `Analise/ProudNet_1771`.
- Importações PE: `ProudNetClientPlugin.dll` importa diretamente `ProudNetClient.dll`. O `GameAssembly.dll` **não** importa diretamente ProudNet em sua tabela convencional; carregamento dinâmico não foi descartado.

## Metadados e arquitetura de comunicação (2162–2174)

- `global-metadata.dat` da cópia atual: 31.876.664 bytes; cabeçalho IL2CPP v29. Interpretação estruturada das tabelas encontrou **34.488 tipos** e **263.448 registros de métodos**. Números associados ao layout/stride usado no parser, não necessariamente código executável recuperado.
- Tipos em namespace `Nettention.Proud`: `NetClient`, `RmiProxy`, `RmiStub`, `IRmiHost`, `NetConnectionParam`. `NetClient` inclui métodos chamados `AttachProxy`, `AttachStub`, `Connect`, `Disconnect`, `FrameMove`.
- Tipos de comunicação do jogo: `PacketManager`, `GuildPacketManager`, `WestSidePacketManager`, `RelayPacketManager`, e `GameProxy`, `GuildProxy`, `WestSideProxy`, `RelayProxy`. Métodos como `ConnectToGameServer`, `OnPacketReceived`, `RmiSend` e campos de IP/porta constam nos metadados. O vínculo de chamadas real permanece **hipótese**.
- `Auth_PacketHandler` traz nomes como `CG_RequestNetmarbleAuthOK`, `CG_RequestLoginOK`, `CG_RequestHeartBeatOK`, `CG_RequestSecurityTokenOK`; `Gacha_PacketHandler`, `RelayPacketHandler`, `RealTimePvpPacketID` também identificados. **49** tipos terminam exatamente em `_PacketHandler`. Os nomes não provam transporte, formato de pacotes nem lógica de autenticação.
- `RmiMessage` contém `remotes`, `rmiContext`, `msg`, `rmiID`, `rmiName`. Ainda não foram obtidos valores numéricos nem serialização específica do jogo.
- A busca por nomes exatos `GameStub`, `GuildStub`, `WestSideStub`, `RelayStub` foi negativa na tabela inspecionada; outras implementações ainda são possíveis.
- **Marcos:** integração nominal do ProudNet gerenciado/nativo e arquitetura segmentada de mensagens do cliente. **Nenhum marco de funcionamento do servidor foi alcançado**.

## Testes do servidor experimental (2142–2146)

- Três suítes Python locais, fornecidas pelo projeto, terminaram com código de saída zero e reportaram 6/6, 8/8 e 9/9 cenários, respectivamente (**23/23 reportados**). Os testes V2 usam `check()` que lança `AssertionError` quando uma condição falha.
- O teste de expiração exige HTTP 401 e remoção do estado em memória. `SESSION_TTL=3600`; sessões guardadas em dicionário protegido por lock.
- Esses testes são de **HTTP Python independente**, não do handshake, login real ou RMI do Grand Cross. Não indicam capacidade de jogar offline.

## Limites e próximos pontos de verificação

1. Estabelecer a associação concreta entre `PacketManager`, proxies, `RmiMessage` e handlers, sem inferir apenas pelos nomes.
2. Separar fluxo de autenticação Netmarble/SDK de sessões de jogo ProudNet; não publicar endereços de produção, credenciais, tokens ou dumps proprietários.
3. Priorizar testes reproduzíveis com dados sintéticos e provas observáveis de compatibilidade; **não** declarar servidor compatível até teste real independente.
4. Manter trilhas separadas: análise do cliente versus servidor local funcional. Preservar checkpoints e hashes em texto; **não** subir DLLs, metadados proprietários ou dados de conta.

**Proveniência:** saídas dos passos 2142–2156 compartilhadas pelo usuário, quatro cópias enviadas no chat e relatório estático da rodada 2162–2174. Os passos 2175–2200 ainda não devem ser declarados concluídos. O roadmap é hipótese/plano, não execução.
