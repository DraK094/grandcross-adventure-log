# GrandCross Local — checkpoint 2274: proteção das páginas IL2CPP

Saída fornecida pelo usuário, processo `7dsgc` PID 27460, módulo `GameAssembly.dll` base `0x7FFCE9F90000`, consultado com `VirtualQueryEx` sem leitura de bytes.

As páginas que contêm os RVAs `0x344720` (`il2cpp_domain_get`), `0x344B60` (`il2cpp_init`) e `0x344F80` (`il2cpp_runtime_invoke`) retornaram `State=0x1000` (MEM_COMMIT), `Protect=0x20` (PAGE_EXECUTE_READ) e `Type=0x1000000` (MEM_IMAGE). As duas amostras na primeira seção (`RVA 0x1000` e `0x43C000`) retornaram as mesmas características.

Isso demonstra proteção executável e mapeamento de imagem para os endereços consultados. **Não demonstra bytes válidos, execução efetiva, implementação de callbacks, registro de delegates ou compatibilidade com servidor local.** O `RegionSize` refere-se ao intervalo contínuo a partir do endereço-base da região correspondente e não identifica implementação de função. A conclusão anterior de que as exportações estavam em `.vdata` foi corrigida no checkpoint 2272.

Trilha análise do cliente: evidência nova do runtime. Trilha servidor local funcional: compatibilidade ainda não demonstrada. Nenhum binário proprietário incluído.