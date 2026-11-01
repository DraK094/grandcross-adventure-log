# Checkpoint 2277 — aliases de exportações PE

Auditoria reproduzível e somente leitura do `GameAssembly.dll` SHA256 `01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624`.

Foram examinadas **384 exportações nomeadas**: **356** endereços estão na porção virtual sem bytes raw no arquivo, e **28** exportações apresentam bytes raw mapeáveis. As 28 exportações com bytes distribuem-se por **somente seis RVAs distintos**: `0x3310` (1 nome), `0x40F0` (20 nomes), `0x12720` (1), `0x55AE0` (2), `0x55AF0` (1) e `0x5EFB0` (3). Ex.: `il2cpp_class_is_valuetype` e `mono_class_is_valuetype` compartilham `0x55AE0`. Não equivale a seis implementações funcionais distintas: os bytes não foram validados como instruções completas, e os aliases não demonstram semântica da rotina.

Reforça a errata de 2272: as exportações apontam para a **primeira seção sem nome** e não para `.vdata`. O diagnóstico 2274 confirmou que três exportações IL2CPP consultadas pertencem a páginas MEM_IMAGE, MEM_COMMIT, PAGE_EXECUTE_READ no processo, mas não examinou bytes de código.

Não confirma despacho de delegates, implementação de IL2CPP em memória, protocolo, autenticação ou servidor funcional. Próxima prova requer método de inspeção independente e consentido; não há necessidade de repetir consultas de proteção.
