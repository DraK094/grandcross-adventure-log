# PASSOS 1010–1012 — Entradas IL2CPP e lacuna dos bytes de código

**Data:** 30/10/2026. **Aprovados: 1010–1012** em verificações estáticas. **Próximo: 1013, ainda não executado.** Objetivo 2 segue **EM ANDAMENTO**.

## 1010 — Exports PE
A GameAssembly.dll enviada possui tabela de exportação com **384 nomes / 384 RVAs**; **239 nomes** contêm `il2cpp`. RVAs obtidos via associações da EAT, Name Pointer Table e Ordinal Table:

| Nome | RVA |
|---|---|
| `il2cpp_init` | `0x3458B0` |
| `il2cpp_init_utf16` | `0x3458E0` |
| `il2cpp_domain_get` | `0x345470` |
| `il2cpp_runtime_invoke` | `0x345CD0` |
| `il2cpp_set_config_dir` | `0x345D50` |

## 1011 — Lacuna entre endereços virtuais e dados brutos
**356/384** RVAs de exports caem em porções virtuais **sem correspondência direta no conteúdo armazenado no arquivo**, restando apenas **28/384** com bytes diretamente mapeáveis.

A primeira seção executável do PE inicia em RVA `0x1000`, tamanho virtual `0x43CFFC`, tamanho bruto `0x145800`; `il2cpp_init` no offset relativo `0x3448B0` está muito além do limite bruto. Assim, localizar a exportação nominal **não recupera o corpo de código na DLL em disco**. Isso não exclui materialização na memória em tempo de execução.

## 1012 — Cruzamento de fontes
O `global-metadata.dat` recebido tem magic `0xFAB11BAF`, versão 29, 34.451 tipos e 89 imagens/assemblies (PASSOS 1007–1009). A interface IL2CPP existe nos exports da DLL, mas **CodeRegistration/MetadataRegistration, corpo de `il2cpp_init` e a cadeia dinâmica real não estão identificados**.

A busca literal na saída completa `.vdata` de 14.131.200 bytes, SHA-256 `60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3`, encontrou zero correspondências exatas para `il2cpp_init`, `global-metadata.dat`, `CodeRegistration`, `MetadataRegistration` e `Assembly-CSharp`; isso não prova ausência de código ou dados transformados.

## Próximo passo e limite
Investigar a possível materialização de regiões virtuais durante a execução e as dependências do carregamento. Se a análise somente leitura não bastar, pedir dados controlados sobre **endereços de memória e seções mapeadas**, sem coletar dados de login nem publicar dumps proprietários. **Objetivo 2: EM ANDAMENTO**, sem servidor offline validado.

[1006](PASSO_1006_HANDOFF_BOOT_VDATA.md) · [1007–1009](PASSOS_1007_1009_AUDITORIA_METADATA.md) · [1000](CHECKPOINT_1000.md).