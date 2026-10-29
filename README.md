# ⚔️ Grand Cross Local — Adventure Log

Diário público de investigação técnica do cliente PC de **Seven Deadly Sins: Grand Cross**. Projeto independente, não afiliado à Netmarble.

## Estado atual — marco 700 auditado
- **Último passo concluído: 701**.
- **Próximo passo preparado: 702** — análise estática dos campos de sete classes de sessão e conexão.
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

## Limitações e próximas investigações
A análise estática do cliente **não equivale** a autenticação local, implementação de backend ou jogo offline funcional. A sequência real de inicialização, a semântica das mensagens e as dependências do servidor permanecem pendentes.

**Próximo passo (702):** inspecionar campos declarados em sete classes selecionadas, de forma local e somente leitura, sem executar o jogo, interceptar tráfego ou modificar arquivos.

## Segurança e direitos
Não publicar binários do jogo, assets proprietários, chaves, credenciais ou dados privados. Este repositório contém somente documentação técnica e um painel independente.

## Atualizações
O site é HTML/CSS/JavaScript sem dependências. Atualizações no GitHub exigem commits; executar PowerShell no computador não sincroniza automaticamente com este repositório.
