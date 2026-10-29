# BACKUP TÉCNICO — Grand Cross Local — 29/10/2026 — PASSO 720
> Documento de continuidade entre conversas. Fonte: saídas de PowerShell fornecidas pelo pesquisador e registros consolidados até o passo 720. NÃO é backup dos binários, dos scripts integrais dos 720 passos, nem de logs completos. Não contém credenciais ou assets do jogo.

## Acordo de trabalho / objetivo
- Objetivo de longo prazo: avaliar e eventualmente desenvolver ambiente/servidor local em rede doméstica para Seven Deadly Sins: Grand Cross PC, sem depender dos serviços oficiais.
- **Nenhum servidor local funcional, autenticação local, backend compatível, cliente modificado ou gameplay offline foi construído ou validado.**
- Até o **PASSO 800**: continuar **somente análise técnica**. No checkpoint 800: produzir relatório de 100 passos, atualizar README e index.html e **iniciar desenho da arquitetura para testes**. Não antecipar a implementação.
- Fluxo: um único PASSO por vez, script PowerShell **5.1**, integral, autossuficiente, copiável, **somente leitura**, validar magic/versão, limites, contagens, sem rede, sem execução de métodos, sem modificar arquivos. Usuário cola saída; interpretá-la antes do próximo passo. Não confundir hipótese com fato.
- **PASSO 720 é o último executado. PASSO 721 já foi preparado e entregue, mas ainda não foi executado.** Retomar solicitando a saída do PASSO 721; não saltar etapas.
- Ao atingir marcos 800, 900, etc., atualizar README.md e index.html no GitHub; manter marcos históricos e estimativas honestas.

## Ambiente e artefatos locais (não versionados)
- Windows 10, PowerShell 5.1, projeto local `GrandCross_Local` com subpastas `Analise`, `Ferramentas`, `Resultado`.
- Metadata oficial: `E:\JOGOS\Netmarble Game\7dsgb\7dsgc_Data\il2cpp_data\Metadata\global-metadata.dat`, **31.786.920 bytes**.
- Cópia de `GameAssembly.dll` ~47.199.760 bytes, cópia conferida com SHA256; Unity **2022.3.27f1**, IL2CPP metadata **v29** (Cpp2IL reportou 29.1), PE32+ x64 (Machine 0x8664), ImageBase 0x180000000.
- Ferramentas tentadas: Cpp2IL 2022.0.7.0 falhou `Failed to find pCodegenModules`; versão 2022.1.0-development instalada (plugins listados), sem dump completo comprovado. Il2CppDumper x64/x86 com ForceDump true: custom PE loader e Win32Exception 126. Não supor extração nativa completa.

## Inventário IL2CPP validado
- Magic metadata bytes AF 1B B1 FA, versão 29.
- TypeDefinitions **34.451**, MethodDefinitions **262.861**, ParameterDefinitions **240.898**, FieldDefinitions **200.338**, FieldDefaultValues **46.060**, GenericContainers **2.800**, GenericParameters **4.232**, NestedTypes **17.316**, Interfaces **16.530**, Images **89**, Assemblies **89**.
- Header: pares `offset,size`, ambos int32 little-endian; regiões:
```text
header  start      bytes     significado / registro
0x18    0x179CA0   5679156   Strings UTF8 NUL
0x30    0x7E6058   8411552   MethodDefinitions / 32
0x40    0x1005264   552720   FieldDefaultValues / 12
0x48    0x108C178  1643404   DefaultValueData / bytes
0x58    0x1249A84  2890776   Parameters / 12
0x60    0x150B69C  2404056   Fields / 12
0x68    0x1756574    67712   GenericParameters / 16
0x78    0x17681D4    44800   GenericContainers / 16
0x80    0x17730D4    69264   NestedTypes / 4
0x88    0x1783F64    66120   Interfaces / 4
0xA0    0x194397C  3031688   TypeDefinitions / 88
0xA8    0x1C27C04     3560   Images / 40
0xB0    0x1C289EC     5696   Assemblies / 64
```
- TypeDefinition 88 bytes: +0 nameIndex, +4 namespaceIndex, +8 byvalTypeIndex, +12 declaringTypeIndex (17.316 nested relations verified), +20 parentIndex **provisional semantic** (enum profile 37739, managers sometimes self-reference), +24 genericContainerIndex, +28 flags UInt32, +32 fieldStart, +36 methodStart, +40 eventStart, +44 propertyStart, +48 nestedTypesStart, +52 interfacesStart, +56 vtableStart, +60 interfaceOffsetsStart, +64 methodCount UInt16, +66 propertyCount UInt16, +68 fieldCount UInt16, +70 eventCount UInt16, +72 nestedTypeCount UInt16, +74 vtableCount UInt16, +76 interfacesCount UInt16, +78 interfaceOffsetsCount UInt16, +80 bitfield, +84 token.
- MethodDefinition 32B: +0 nameIndex, +4 declaringType, +8 returnTypeIndex, +12 parameterStart, +16 genericContainerIndex, +20 token, +24 flags UInt16, +26 iflags UInt16, +28 slot UInt16, +30 parameterCount UInt16.
- FieldDefinition 12B: +0 nameIndex, +4 typeIndex, +8 token.
- ParameterDefinition 12B: +0 nameIndex, +4 token, +8 typeIndex.
- GenericContainer 16B: +0 ownerIndex, +4 typeArgCount, +8 isMethod, +12 genericParameterStart.
- GenericParameter 16B: +0 ownerContainerIndex, +4 nameIndex, +8 constraintsStart, +10 constraintsCount UInt16, +12 number UInt16, +14 flags UInt16.
- FieldDefaultValues 12B: +0 fieldIndex, +4 defaultTypeIndex, +8 dataIndex (relativo à região 0x48).
- 34.451 ByValTypeIndex únicos; índices de tipos dos campos não equivalem diretamente aos ByValTypeIndex de TypeDefinitions: **não presumir resolução de Il2CppType**.

## Comunicação e sessão — resultados 688–711
- PASSO 688: 23/23 assinaturas de métodos de `NetmarbleS.ISession` coincidem com `NetmarbleS.SessionPlatform`, mais construtor.
- PASSO 689: `SessionPlatform` TypeDef1878 ByVal45175 implementa `ISession` TypeDef3446 ByVal36280.
- PASSO 690: 11.337/16.530 interfaces resolvidas diretamente por ByValTypeIndex; 5.193 não resolvidas; 1.304 índices distintos.
- PASSOS 691–695: TypeIndex11115 presente em **3.746** classes de iteradores; todas têm `System.Collections.IEnumerator` TypeIndex35450 e `System.IDisposable` TypeIndex35398 e métodos MoveNext/Dispose/Reset/get_Current; 3.726 padrões `<...>d__N` e 20 `c__Iterator`. Interpretação como `IEnumerator<object>` **hipótese, não prova**.
- PASSOS 696–699: `System.Collections.Generic.IEnumerator`1` TypeDef25068 ByVal35455, get_Current MethodDef195382. GenericContainer1065 owner25068, TypeArgCount1, IsMethod0, GenericParameterStart1518; parâmetro1518 `T` número0 flags0x0001. Corrigido erro anterior: índice do generic container está em TypeDef+24, não +28.
- PASSO 700: auditoria 11 classes de rede; nenhum servidor.
- PASSO 701: 102 métodos catalogados em 7 classes:
```text
TypeDef1463  ServerFlowService           MethodStart12133 Count24
TypeDef1878  NetmarbleS.SessionPlatform MethodStart15446 Count24
TypeDef2263  ChannelConnect             MethodStart18398 Count2
TypeDef3483  NetmarbleS.Auth            MethodStart28269 Count6
TypeDef4151  WestSidePacketManager      MethodStart33787 Count14
TypeDef5586  LoginDevAssistant          MethodStart45103 Count17
TypeDef8944  RelayPacketManager         MethodStart72576 Count15
```
- Exemplos de métodos: SessionPlatform.SignIn/ConnectToChannel/GetGameToken/ResetSession; WestSidePacketManager.ConnectToWestSideServer/ReConnectToWestSideServer/OnPacketReceived; RelayPacketManager.ConnectToRelayServer/OnPacketReceived; Auth.LoadWithCredential/GetCurrentPlayer. **Nomes não demonstram fluxo ou chamadas reais**.
- PASSO 702: 27 campos nessas 7 classes; WestSide m_WestSideClient TypeIndex53005, m_ConnectionState78288, IP46707, port49637; Relay m_relayClient52979, IP46707, port49637; Auth.auth35201; SessionPlatform sem campos.
- PASSO 703: 12 índices de tipos de campos de rede, 0 correspondências diretas com ByValTypeIndex.
- PASSO 704: 76 TypeDefs de rede (24 WestSide, 38 Relay, 8 ConnectionState, 5 TCP, 1 Auth).
- PASSOS 705–711: enums aninhados `ConnectionState`:
```text
TypeDef4149  ByVal78287 DeclaringTypeIndex51357 ParentIndex37739 flags0x00000102
  FieldDef26548 value__ TypeIndex37761
  FieldDef26549 DisConnected TypeIndex78289
  FieldDef26550 Connecting TypeIndex78289
  FieldDef26551 Connected TypeIndex78289
TypeDef16508 ByVal58890 DeclaringTypeIndex34437 ParentIndex37739 flags0x00000102
  FieldDef109342 value__ TypeIndex37761
  FieldDef109343 DisConnected TypeIndex58892
  FieldDef109344 Connecting TypeIndex58892
  FieldDef109345 Connected TypeIndex58892
```
- Managers:
```text
TypeDef4151 WestSidePacketManager ByVal51357 FieldStart26542 Count6:
 m_Instance51359, m_WestSideClient53005, m_ConnectionState78288,
 m_reconnectTryCount37740, m_westSideServerIP46707, m_westSideServerPort49637.
TypeDef16510 GuildPacketManager ByVal34437 FieldStart109336 Count6:
 m_Instance34439, m_GuildClient53093, m_ConnectionState58891,
 m_reconnectTryCount37740, m_relayserver_ip46707, m_relayserver_port49637.
TypeDef8944 RelayPacketManager ByVal43921 FieldStart56585 Count5:
 m_Instance43923, m_relayClient52979, m_IsWaitingResponse27593,
 m_relayserver_ip46707, m_relayserver_port49637.
```
- 89 Images cobrem 34.451 tipos sem lacunas. Os enums e managers citados estão em `Assembly-CSharp.dll` ImageIndex0. 17.316 relações nested verificadas, 0 divergências.
- 1.557 TypeDefs compartilham ParentIndex37739, flags0x00000102 e campo `value__`, evidência forte de perfil de enum.

## FieldDefaultValues — PASSOS 712–720
- PASSO 712: defaults de ConnectionState: WestSide FieldDefs26549/50/51, DefaultTypeIndex37739, DataIndex31894/31895/31896, bytes 00/02/04; Guild FieldDefs109343/44/45, DataIndex1018728/29/30, bytes 00/02/04.
- PASSO 713: candidatos zigzag 0,1,2.
- PASSO 714: `System.DayOfWeek` TypeDef23670, domingo0–sábado6, 7/7 decodificados, bytes 00 02 04 06 08 0A 0C.
- PASSO 715: `System.AttributeTargets` TypeDef23654, 16 constantes de valores 1..32767 (Assembly1, Module2, Class4, Struct8, Enum16, Constructor32, Method64, Property128, Field256, Event512, Interface1024, Parameter2048, Delegate4096, ReturnValue8192, GenericParameter16384, All32767).
- PASSO 716: 22/22 testes de decoder (16 AttributeTargets e 6 ConnectionState) sem divergência; 12 de 1 byte, 7 de 2 bytes, 3 de 4 bytes. **Para inteiros assinados** zigzag: U par -> U/2; U ímpar -> -(U+1)/2. Prefixo <0x80: U=byte (1B); 0x80–0xBF: U=((byte0 & 0x3F)<<8)|byte1 (2B); 0xC0–0xDF: U=((byte0 & 0x1F)<<24)|(byte1<<16)|(byte2<<8)|byte3 (4B). Para UInt32 **não aplicar zigzag**.
- PASSO 717: de 46.060 defaults, 32.683 com DefaultTypeIndex37739. Primeiro byte 01=142,03=13,05=9,07=7; 33 candidatos em tipos com perfil de enum, 138 em outros tipos; 0 sem declarador. Exemplos: `Sign.Negative`, `CompressionLevel.DEFAULT_COMPRESSION` = candidato -1, `Result.ErrorAlreadyInProgress` = -2.
- PASSO 718: 3/3 verificações de valores negativos conhecidos; 0 divergências. `Sign` TypeDefs23574 e32648, ambos Negative=-1 byte01, Zero=0 byte00, Positive=1 byte02. `CompressionLevel` TypeDef33218: BEST_COMPRESSION9 byte12, BEST_SPEED1 byte02, DEFAULT_COMPRESSION=-1 byte01, NO_COMPRESSION0 byte00, DEFLATED8 byte10. 14 campos, 11 defaults, 3 `value__` sem default.
- PASSO 719: **46.060** defaults válidos, **396** começam em E0–FF; **214** dos 396 têm DefaultTypeIndex37739. **F0=227** no total, **196** no tipo37739; FE=15 (9 tipo37739); FF=56 (9 tipo37739). Prefixos E0–EF não apareceram no tipo37739; outros tipos podem conter valores IEEE754 etc. **Não presumir que todo byte E0–FF é prefixo de inteiro**. Exemplos `XXHash.XXHash32` TypeDef2946, FieldDef19238..19242, DataIndex23800,23805,23810,23815,23820.
- PASSO 720: testou equivocadamente F0 como obrigatório em todos os cinco UInt32 XXHash. Quatro acertos:
```text
PRIME32_1 2654435761 0x9E3779B1 [F0 B1 79 37 9E]
PRIME32_2 2246822519 0x85EBCA77 [F0 77 CA EB 85]
PRIME32_3 3266489917 0xC2B2AE3D [F0 3D AE B2 C2]
PRIME32_4  668265263 0x27D4EB2F [F0 2F EB D4 27]
PRIME32_5  374761393 0x165667B1 [D6 56 67 B1] (o quinto byte 00 pertence a dados subsequentes)
```
- Interpretação do PASSO 720: PRIME32_5 provavelmente usa forma compactada C0–DF com 4 bytes: ((0xD6&0x1F)<<24)|(0x56<<16)|(0x67<<8)|0xB1 = 374761393. A discrepância **4/5** é erro de hipótese do teste (F0 universal), não evidência de metadata corrompido. **PASSO 721 script já fornecido, NÃO executado:** testa seletor por prefixo, `C0–DF` compactado sem zigzag para UInt32, `F0` + UInt32 little-endian, espera 5/5; aguardar resultado do usuário. F0 para signed, E0–EF, F1–FF e significado de FE/FF continuam sem prova.

## Marcos históricos anteriores
- PASSO 384: **1.165 IDs C2S** e **624 IDs S2C** catalogados; **não** significa protocolo completo.
- PASSO 400: `QuestProgressInfo` com ID, estado, contadores, flags. PASSO 406 métodos de requisição/resposta de progresso de missão. PASSO 439 `DBQuestRow` 75 campos/79 métodos. PASSO 441 `TableIndexerQuest` e `DBQuestRow`; dados de missões não extraídos. PASSO 448 **734 membros TableType** 0..733; Quest513, QuestExtra518, QuestSound524, QuestTalk525, StageQuest657.
- PASSOS 450–456: inventário **35.245 arquivos**, 35.167 sem extensão; 70/70 amostras de wrapper UnityArchive/UnityFS com header UnityFS interno, versão 8, editor 2022.3.27f1, flags579 (0x243), compressão tipo3; não confundir cabeçalhos com extração de conteúdo.
- PASSOS 585–601: 384 exportações PE nomeadas, 239 `il2cpp_`; 14 seções; .vdata virtual sem bytes físicos, .boot RX, .vdata RWX; EntryPoint 0x077FD058, CALL inicial para 0x077FD1DF, alvo 0x06A9FC32 em .vdata sem bytes no arquivo; TLS sem callbacks; importações 10 DLLs/10 funções, 3 DIR64 TLS relocations; flags DYNAMIC_BASE/HIGH_ENTROPY_VA declaradas, NX_COMPAT/GUARD_CF não declaradas. **Não inferir conteúdo de .vdata em execução nem fluxo real sem prova**.

## Progresso e GitHub
- Repositório: https://github.com/DraK094/grandcross-adventure-log, branch main, `index.html` painel e `README.md` resumo. Marco 700 documentado; esta cópia técnica atualiza contexto até 720.
- Marco 600: estimativa geral **25%**; marco 700: **28%**; estimativas qualitativas, **não** porcentagem de backend pronto; não criar nova porcentagem sem auditoria.
- Dez áreas no marco 700: ambiente/ferramentas95, metadados90, PE82, Unity65, protocolo45, missões38, boot35, autenticação5, backend0, jogo offline0. Não inventar valores individuais do marco 600.
- PASSO 800: produzir arquitetura experimental separando cliente, autenticação, sessão, estado de jogador, dados/missões, transporte; critérios de teste e lacunas; **somente começar arquitetura quando chegar a 800**, conforme decisão expressa.
- **Retomada em nova conversa:** abrir este arquivo, README e painel, dizer “Retome o GrandCross Local do PASSO 721; o PASSO 720 terminou 4/5, o 721 foi enviado mas ainda não executado; mantenha scripts PowerShell 5.1 integrais, read-only, e arquitetura somente no PASSO 800.” Para detalhes não contidos aqui, solicitar logs/scripts originais, não inventar.
- Segurança: não versionar binários, dados proprietários, credenciais, chaves, tokens, logs pessoais ou assets. Esta documentação **não** constitui backup total dos arquivos locais; manter backup local separado se desejado.
