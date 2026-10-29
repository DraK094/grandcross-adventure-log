# ⚔️ Grand Cross Local — Adventure Log

Diário público de investigação técnica do cliente PC de **Seven Deadly Sins: Grand Cross**. Projeto independente, não afiliado à Netmarble.

## Estado atual — análise até o passo 720 (marco 700 auditado)
- **Último passo concluído: 720**.
- **Próximo passo preparado: 721 (ainda não executado)** — validar formatos compactado-4 e F0-UInt32LE com cinco constantes XXHash32.
- **Próximo relatório formal: passo 800**.
- **Marco 700 concluído** com auditoria estrutural do metadata IL2CPP.
- **Nenhum servidor offline compatível e funcional** implementado ou validado.

## Painel e comparação histórica
A página [index.html](./index.html) inclui o painel de progresso, o histórico técnico e a comparação entre os marcos 600 e 700.

| Indicador | Marco 600 | Marco 700 |
| --- | ---: | ---: |
| Progresso geral estimado | 25% | 28% |
| Diferença | — | +3 pontos percentuais |

Os percentuais são **estimativas qualitativas de acompanhamento**, não medidas objetivas de software implementado. Os **dez percentuais individuais do marco 600 não foram recuperados**; o painel apresenta os valores registrados no marco 700, sem inventar diferenças históricas por área.

### Valores registrados no marco 700

| Área | Estimativa |
| --- | ---: |
| Ambiente e ferramentas | 95% |
| Metadados IL2CPP | 90% |
| Formato PE e GameAssembly | 82% |
| Arquivos Unity e recursos | 65% |
| Protocolo e mensagens | 45% |
| Sistema de missões | 38% |
| Inicialização do boot | 35% |
| Autenticação local | 5% |
| Backend e servidor offline | 0% |
| Jogo offline funcional | 0% |

## Descobertas confirmadas até o passo 701
- Metadata IL2CPP v29: **34.451 TypeDefinitions**, **262.861 MethodDefinitions**, **240.898 parâmetros**, **200.338 campos**, **16.530 entradas de interface**, **2.800 contêineres genéricos**, **4.232 parâmetros genéricos**, **89 images** e **89 assemblies**.
- Definição **System.Collections.Generic.IEnumerator`1** identificada em **TypeDef 25068** (ByValTypeIndex **35455**); contêiner genérico **1065**, com parâmetro **T** em **1518**, posição **0**. A auditoria corrigiu uma interpretação incorreta do deslocamento do contêiner.
- **3.746 classes** com interface TypeIndex **11115** e o trio de interfaces consistente; **3.726** com padrão `d__` e **20** com padrão `c__Iterator`. A associação de TypeIndex 11115 a uma instanciação de `IEnumerator<object>` é **hipótese fortemente sustentada, não resolução direta**.
- **11 classes** de comunicação e autenticação localizadas, incluindo `NetmarbleS.SessionPlatform`, `NetmarbleS.Auth`, `WestSidePacketManager`, `RelayPacketManager` e proxies.
- **Passo 701:** **102 métodos** catalogados em sete classes de sessão, conexão e fluxo. Nomes de métodos **não comprovam a ordem real de execução**.
- Marcos anteriores preservados: **70/70** cabeçalhos UnityFS internos validados; **734** membros `TableType`; **1.165 IDs C2S** e **624 IDs S2C** catalogados.
- Análise PE anterior: `GameAssembly.dll` x64, seção `.vdata` virtual sem dados físicos e seção `.boot` RX. A origem do conteúdo de `.vdata` em execução permanece indeterminada.

## Backup para continuidade em outras conversas

**[📚 Backup técnico completo do conhecimento recuperado até o PASSO 720](./docs/BACKUP_TECNICO_PASSO_720.md)** — documentação detalhada com contexto do projeto, caminhos locais, ferramentas, estruturas IL2CPP, offsets, classes de rede, enums, constantes, validações, hipóteses e roteiro de retomada. Não inclui os 720 scripts integrais, logs completos ou binários.

**Decisão em 29/10/2026:** manter a análise técnica somente leitura até o **PASSO 800**; nesse marco, além do relatório e atualização do painel, começar a **arquitetura experimental para testes locais**. O PASSO 721 já foi entregue e aguarda saída do PowerShell. Nenhum servidor local foi implementado.

**Passos 712–720:** defaults de ConnectionState 0/1/2; testes 22/22 no passo 716; negativos confirmados 3/3 no passo 718; 46.060 defaults auditados no passo 719, 396 primeiros bytes E0–FF (227 F0); passo 720 confirmou quatro constantes XXHash32 com F0 + UInt32LE, enquanto PRIME32_5 começa com D6 e provavelmente usa formato compactado-4. Não anunciar 5/5 antes de executar 721.

## Limitações e próximas investigações
A análise estática do cliente **não equivale** a autenticação local, implementação de backend ou jogo offline funcional. A sequência real de inicialização, a semântica das mensagens e as dependências do servidor permanecem pendentes.

**Próximo passo (721):** executar o script já entregue e conferir as cinco constantes XXHash32; resultado do passo 720 foi 4/5 por pressupor incorretamente F0 universal.

## Segurança e direitos
Não publicar binários do jogo, assets proprietários, chaves, credenciais ou dados privados. Este repositório contém somente documentação técnica e um painel independente.

## Atualizações
O site é HTML/CSS/JavaScript sem dependências. Atualizações no GitHub exigem commits; executar PowerShell no computador não sincroniza automaticamente com este repositório.
