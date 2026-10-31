> ATUALIZAÇÃO 31/10/2026: **PASSO 2081 executado e validado**, substituindo o estado anterior de pendente. State.m_dicPackageMissionData, offset 0x1D8, aponta Dictionary`2. [Nota técnica 2081](./PASSO_2081_DICIONARIO_MISSOES.md). A reunião de consolidação continua; **PASSO 2082 ainda não emitido**. Os trechos históricos abaixo descrevem o snapshot anterior da pausa 2080 e não representam o estado atual.

# GUIA OFICIAL DE RETOMADA — GRAND CROSS LOCAL — PASSO 2080

**LEIA ANTES DE CONTINUAR.** Último PASSO EXECUTADO com log recebido: **2080**. **PASSO 2081** já foi fornecido e está **PENDENTE DE EXECUÇÃO/RESULTADO**. Não iniciar 2082 até revisar o log 2081. A anotação no GitHub antes da reunião estava em passos 2013–2016; os passos 2017–2060 permanecem lacuna documental neste pacote.

## Documentos de continuidade
- [Registro técnico detalhado de 2061–2080](./DIARIO_2017_2080.md)
- [Relatório e comparação histórica da reunião](./RELATORIO_REUNIAO_2080.md)
- [Checkpoint 2080 estruturado](../checkpoints/PASSO_2080.json)
- README mantém histórico de marcos anteriores.

## Ambiente
Windows, jogo 7dsgc PC, Unity 2022.3.27f1, metadata IL2CPP v29, x64; processo observado no log PID **30012**, GameAssembly.dll base VA **0x7FFD00550000**. VAs dinâmicos de objetos e PID só válidos na sessão em que foram lidos. RVAs devem ser revalidados se binário/versão mudar. Não há servidor offline funcional comprovado.

## Principais referências
1. CG_RequestLoginOK RVA 0x29F5200; LoginUserResultInfo TypeDef global 21837, 114 campos; registration RVA 0x57E33E0.
2. Campo isShowWebShopBuy +0x310 → GameDataContainer.m_state +0x38 → State.m_packageItemManager +0x98 → PackageItemManager.IsShowWebBuy +0x75.
3. Campo battleEncounter +0x2D0 → setter RVA 0x1C19850 → State.m_battleEncounter +0x2FC.
4. userPackageMissionInfoList +0x240 → processador de lista 0x1C169E0 → item 0x1C16C20. Consulta +0x1D8; wrapper 0x3612580 despacha indiretamente. Destino real ainda desconhecido.
5. userNpcList → 0x1C14500; userEventBingoInfo → 0x1105D00.
6. Estado de rede: sem framing/handshake ProudNet/local login aceito. Não confundir conhecimento com funcionalidade.

## Próximas ações
- Receber a **saída real do PASSO 2081**, que inspeciona o campo State+0x1D8 e o tipo do objeto apontado. Se VAs expiraram, reconstruir via singleton, nunca assumir ponteiros antigos.
- Identificar tipo/offset e revisar o processador de missão sem modificar dados.
- Não inventar texto dos logs 2017–2060. Recuperar originais antes de afirmar progresso nesses passos.
- Publicar notas de marcos verificados regularmente. Em 2100 preparar checkpoint formal e comparar com 2080.

## Convenções obrigatórias
- Scripts PowerShell completos, **um passo por vez**, read-only, com comentários visuais de início AZUL e fim VERMELHO; banners Write-Host coloridos no início e fim.
- Validar nomes, offsets e limites de instruções. Separar fatos, hipóteses e pontos desconhecidos.
- Conquistas com nome e raridade só para marco realmente comprovado; trilhas separadas análise do cliente versus servidor funcional.
- Formalização a cada 100 passos. Percentuais são estimativas subjetivas de conhecimento e só podem ser alterados com método e justificativa; servidor funcional segue sem demonstração.
- Repositório público: NÃO subir binários/dumps/metadata original, assets privados, chaves, credenciais ou dados de contas.
