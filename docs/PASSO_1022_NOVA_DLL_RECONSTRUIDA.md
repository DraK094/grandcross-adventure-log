# PASSO 1022 — DLL atualizada validada e recuperada

**Concluído** na análise local de 30/10/2026. Próximo 1023 não executado.

Nova GameAssembly.dll: 47.294.480 bytes, SHA256 `01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624`, confere com hash enviado pelo usuário.

Antiga DLL: 47.199.760 bytes, SHA256 `fab18d112f6414090c4cf36c25908fae1056c87d56e6ac432c053b52e2933ddd`. Diferença 94.720 bytes.

Nova .vdata: RVA `0x6AE2000`, tamanho virtual 14.131.200 bytes. Antiga: `0x6A83000`. Nova .boot RVA `0x785C000`, raw offset `0x256EE00`, raw size 8.043.008 bytes.

Descompressão com implementação Python pura anterior ajustada ao layout novo: marcador final encontrado; 14.131.200 bytes recuperados. SHA256 integral novo `72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231`; primeiros 4MiB `c301a732451a228bc67f0710cd763dd6ec3df12d3c22276c11a3ee6efaa62ea1`. Fonte consumida: 8.042.078 bytes. A saída não foi escrita em arquivo.

Nova EAT: 384 exports, 239 contendo il2cpp. `il2cpp_init` RVA `0x344B60` (antigo `0x3458B0`); `il2cpp_init_utf16` `0x344B90`; `il2cpp_domain_get` `0x344720`; `il2cpp_runtime_invoke` `0x344F80`.

Objetivo 2 — compreender a inicialização completa: EM ANDAMENTO. Nenhuma execução real do segundo estágio ou backend funcional comprovados. Próximo PASSO 1023: examinar cadeia .boot → .vdata na nova DLL sem reutilizar offsets antigos.