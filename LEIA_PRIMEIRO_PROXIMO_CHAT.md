# LEIA PRIMEIRO — GRANDCROSS LOCAL

> **ATUALIZAÇÃO 30/10/2026 — LEIA ANTES DAS NOTAS HISTÓRICAS ABAIXO:** o manual antigo parou em 1174, mas o histórico foi recuperado até o **PASSO 1288** (auditoria documental); **1289 está preparado, não executado**. O backend do laboratório ainda não está conectado ao cliente. Consulte [checkpoint recuperado](Copias_de_seguranca_relatorios_e_scripts_backup/relatorios/CHECKPOINT_RECUPERACAO_1175_1288_2026-10-30.md) e [política de backup a cada 10 passos](Copias_de_seguranca_relatorios_e_scripts_backup/relatorios/POLITICA_BACKUP_CADA_10_PASSOS.md). **Próximo marco: 1290 concluído.** Não retomar do 1175. Os marcos só são publicados quando concluídos, e cada commit deve ser confirmado.

**Manual de continuidade entre chats — 30/10/2026.**

> O projeto já tem **1174 passos concluídos**. **PASSO 1175 AINDA NÃO EXECUTADO.** Não é um projeto novo. Antes de anunciar descoberta, execute teste real e preserve evidências.

## Missão
Construir servidor local independente para cliente PC **Seven Deadly Sins: Grand Cross**, com identidade local e progresso/inventário persistente (inspiração arquitetural LunarCore), buscando login e entrada na taverna. Preservar jogo oficial; não publicar DLLs, metadata original ou credenciais.

**IMPORTANTE:** o backend HTTP/SQLite de laboratório funciona em testes independentes; **NÃO EXISTE comprovação de cliente oficial conectado, autenticação compatível, handshake ProudNet, RMI real decodificado ou taverna local jogável**.

## Passos e próximo foco
- Último **PASSO 1174**: correspondências entre índices dos parâmetros dos handlers de login e métodos `CommonPacket.Marshaler.Write` / `Read`.
- **PASSO 1175 PENDENTE**: investigar implementação/ordem/bytes dos marshalers de login, depois IDs RMI numéricos verdadeiros, mensagens e handshake.
- Checkpoint formal a cada 100 passos: próximo **1200**. Diferenciar progresso de pesquisa de progresso do emulador funcional.

## Material analisado
Versão **atual**: `/mnt/data/GameAssembly(2).dll` (47.294.480 bytes, SHA256 `01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624`) e `/mnt/data/global-metadata(2).dat` (IL2CPP v29, SHA256 `eea7a31712bfca44caaa85cee3874ae9092a035556fcdef10f6c6a1fe156448b`).
Versão **antiga**: `GameAssembly(1).dll` SHA256 `fab18d112f6414090c4cf36c25908fae1056c87d56e6ac432c053b52e2933ddd`, `global-metadata(1).dat` SHA256 `1fa69d945210e27b2ca6195ef975da386fe11de044e764069986717ac3d577c9`.
Esses caminhos são do laboratório e **não estão garantidos em outro chat**. Verificar presença e hash, não presumir.
Instalação PC usuário: `E:\JOGOS\Netmarble Game\7dsgb\`; metadata em `7dsgc_Data\il2cpp_data\Metadata\`.

## Descobertas importantes
- `WorldInfo` possui `m_name,m_worldId,m_region,m_ip,m_port`; `WorldInfoManager` tem lista/seleção e `AddWorldInfo(name,worldId,region,ip,port,chatkitSetting)`, `SetMyWorldInfo`. **Não comprovado adicionar terceiro servidor ou redirecionar um existente no cliente.**
- `PageLogin.GameServerConnect(worldInfo)`, `WestSidePacketManager.ConnectToWestSideServer(ip,port)`; `Auth_PacketHandler.CG_RequestLoginOK(remote,rmiContext,userInfo,loginServiceInfo)` são métodos declarados, não fluxo de execução comprovado.
- ProudNet `RmiProxy`, `RmiStub`, `RmiContext`, `RmiID`, `NativeNetClient` e classe de jogo `RmiMessage` identificados. `RmiMessage` tem `remotes,rmiContext,msg,rmiID,rmiName`. `RmiProxy.GetRmiIDList()` / `RmiStub.get_GetRmiIDList` existem, mas **nenhum ID RMI numérico Grand Cross recuperado**.
- PIDL define IDs RMI; **tokens e índices IL2CPP NÃO são IDs RMI**. `CommonPacket.Marshaler` tem **1592 Write + 1592 Read** adjacentes; isso **não** significa 1592 mensagens de rede interpretadas.
- `userInfo` índice 40152 → `Write` token `0x600328c` → `Read` `0x600328d`.
- `loginServiceInfo` índice 40148 → `Write` `0x6003292` → `Read` `0x6003293`.
- `sendDailyReset` índice 50187 → `Write` `0x600343e` → `Read` `0x600343f`.
- `CG_RequestNetmarbleAuthOK.info` índice 41435 → `Write` `0x600327a` → `Read` `0x600327b`.
Essas são correlações estruturais; **não** estabelecem bytes, ID RMI, layout, ordem de chamadas ou autenticação. Índice de tipo do parâmetro não é automaticamente índice de TypeDefinition.

## Backend experimental
Python HTTP loopback + SQLite, conta/sessão local, renovação e token inválido. Testes anteriores: 5/5 dados e 7/7 HTTP. **Não conectado ao Grand Cross oficial**.

## GitHub / backups
Repositório: https://github.com/DraK094/grandcross-adventure-log
Central: https://github.com/DraK094/grandcross-adventure-log/tree/main/Copias_de_seguranca_relatorios_e_scripts_backup
Subpastas `relatorios/`, `scripts/`, `evidencias/`, `logs/`. PASSOS 1170–1174 possuem pacote recuperado após falha original (relatório, script, evidências e log, commits confirmados). Pesquisas anteriores em `docs/`.
**Política:** publicar relatórios/scripts/evidências próprios sanitizados após avanços; confirmar SHA retornado. Caso bloqueie, deixar pendente e tentar novamente nos próximos passos. Não alegar sucesso sem commit.

## Regras de trabalho
Português do Brasil, parceria entusiasmada mas precisão científica. Prosseguir autonomamente com arquivos existentes. Só pedir PowerShell no Windows quando indispensável, com script completo e instruções. Nunca reiniciar numeração. Relatórios formais a cada 100 passos, conquistas de raridade somente para marcos verificados. Nunca confundir estudo de código com cliente oficial conectado. Não prometer trabalho assíncrono. Explicitar hipóteses, evidências e bloqueios.

## Como reiniciar após troca de chat
1. Ler este arquivo e o relatório mais recente na central do GitHub.
2. Conferir se há passos posteriores ao **1174** e atualizar o próximo número.
3. Verificar presença/hashes dos arquivos locais antes de análises.
4. Retomar pelo primeiro passo pendente (**1175** nesta revisão).
5. Priorizar reconstrução verificável de uma estrutura RMI real e testes de interoperabilidade, evitando IDs inventados.
6. Commitar documentação própria e confirmar resultado.

**Lema técnico: uma descoberta só é uma conquista funcional quando houver teste real e reproduzível.**
