# GrandCross Local — PASSO 1293: triagem das ancoras de introspeccao

Auditoria derivada de `GrandCross_PASSOS_1281_1284_Evidencias.json` e do relatorio 1291–1292. **Nao houve nova leitura de GameAssembly.dll ou memoria do processo.**

## Diferenca que orienta a proxima tentativa
- `il2cpp_init` — RVA `0x344B60`: exportacao sem alias no conjunto auditado, coincide com inicio de RUNTIME_FUNCTION; amostra real de 48 bytes foi lida anteriormente (passo 1262).
- `il2cpp_domain_get_assemblies` — RVA `0x344730`: exportacao sem alias, coincide com inicio de RUNTIME_FUNCTION, **mas ainda nao ha amostra de bytes validada em runtime** neste conjunto.
- `il2cpp_method_get_name` — RVA `0x3444D0`: 6 nomes no mesmo endereco, sem cobertura RUNTIME_FUNCTION e sem bytes brutos nesse endereco.
- `il2cpp_method_get_from_reflection` — RVA `0x3444C0`: 9 nomes no mesmo endereco, sem cobertura RUNTIME_FUNCTION e sem bytes brutos.
- `il2cpp_method_get_token` — RVA `0x344CD0`: 2 nomes (aliases mono/il2cpp), sem cobertura RUNTIME_FUNCTION e sem bytes brutos.
- `il2cpp_class_get_methods` — RVA `0x3444B0`: 2 nomes (mono/il2cpp), sem cobertura RUNTIME_FUNCTION e sem bytes brutos.

## Decisao
**Priorizar uma inspecao read-only de `il2cpp_domain_get_assemblies`**: ao contrario das APIs com aliases heterogeneos, e uma ancora com endereco de exportacao nao compartilhado e limite de funcao documentado. Confirmar bytes reais, disassembly, saltos, referências e somente entao inferir se a API pode ajudar a localizar assemblies e MethodInfo. Exportacao unica e RUNTIME_FUNCTION nao provam assinatura, semantica nem capacidade de introspeccao.

## Limites
CodeRegistration, CodeGenModule para Assembly-CSharp-firstpass.dll, os quatro ponteiros de login, IDs RMI e bytes de mensagem **continuam desconhecidos**. Nao usar chamada de API no cliente oficial: apenas inspecao limitada autorizada se necessaria. Proxima etapa 1294 depende de nova amostra de memoria ou artefato de codigo reconstruido. Nao fazer request invasiva ou contornar bloqueios.
