# GrandCross Local — Errata verificada no passo 2272

Uma nova leitura da tabela de exportações do `GameAssembly.dll` corrigiu interpretações anteriores. **384/384 RVAs de exportações** pertencem à **primeira seção executável sem nome**, e **não à `.vdata`**. Destes, **28/384** possuem bytes no arquivo (parte raw da seção) e **356/384** apontam para sua porção exclusivamente virtual, sem bytes raw próprios. Exemplos: `il2cpp_domain_get` RVA `0x344720`, `il2cpp_init` `0x344B60` e `il2cpp_runtime_invoke` `0x344F80`. Primeira seção: RVA `0x1000`, VirtualSize `0x43C2BC`, RawSize `0x145800`, flags `0x60000020`.

**Corrigir checkpoints anteriores:** não é correto afirmar que as 384 exportações estão sem bytes no disco nem que seus RVAs estão em `.vdata`. O resultado anterior da consulta `VirtualQueryEx` do usuário permanece válido **apenas para as páginas consultadas em `.vdata` e `.boot`**, não para as páginas das exportações IL2CPP.

O diagnóstico continua estático, sem leitura da memória do jogo. Não comprova corpos executáveis em runtime, registro de delegates nem servidor local compatível. Script de reprodução e JSON de evidências preservados localmente: `gc_2272_export_section_validation.py`, `GrandCross_2272_export_evidence.json`.
