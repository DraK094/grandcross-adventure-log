# PASSO 1053 — Comparativo independente do diretório de exceções entre versões

**Auditoria concluída em 30/10/2026.** Ambas as seções .vdata foram reconstruídas em Python puro e os hashes integrais verificados antes de ler os diretórios PE. Próximo passo 1054 não executado.

| Métrica | DLL anterior | DLL atual |
|---|---|---|
| Exception Directory RVA | `0x7127024` | `0x718602C` |
| Tamanho | `0x388DA0` | `0x38E704` |
| RUNTIME_FUNCTION (12 bytes) | **308.856** | **310.763** |
| Registro `il2cpp_init` (índice) | 28.912 | 28.899 |
| `il2cpp_init` Begin | `0x3458B0` | `0x344B60` |
| `il2cpp_init` End (exclusivo) | `0x3458D8` | `0x344B88` |
| `il2cpp_init` UnwindRVA | `0x5A23B7C` | `0x5A710EC` |

**Diferença:** 1.907 registros a mais na DLL atual. Nas duas versões, `il2cpp_init` ocupa um intervalo de 0x28 (40) bytes conforme a tabela de unwind. Esses 40 bytes **não estão recuperados apenas porque os limites foram encontrados**. Os registros não provam execução nem indicam onde uma possível rotina exportada salta a seguir.

DLL antiga sha256 `fab18d112f6414090c4cf36c25908fae1056c87d56e6ac432c053b52e2933ddd`, .vdata hash `60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3`. DLL atual sha256 `01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624`, .vdata hash `72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231`.

**Objetivo 2: EM ANDAMENTO.** Contribuição: robusta estrutura de função exportada que pode ajudar análise futura quando código da região for legitimamente acessível. Nenhum servidor local funcional. [1048–1052](PASSOS_1048_1052_EXCEPTION_IL2CPP.md).