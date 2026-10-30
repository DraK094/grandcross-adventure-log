# PASSOS 1048–1052 — Diretório de exceções x64 e exports IL2CPP

**Data 30/10/2026. Último PASSO concluído: 1052; próximo 1053 não executado.** Evidências extraídas da DLL atualizada, sem modificar binários.

DLL SHA256: 01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624. .vdata reconstruída 14.131.200 bytes SHA256: 72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231.

1048: ocorrência literal de IAT `GetModuleHandleA` em .vdata+0xF189 não é evidência confiável de uma instrução executada. A desmontagem linear local inclui opcodes inválidos. Semântica desconhecida.

1049: exports `il2cpp_init` (RVA 0x344B60) e `il2cpp_init_utf16` (RVA 0x344B90) têm cada um um DWORD literal na saída .vdata, offsets 0x6F8AD0 e 0x6F8ADC.

1050: a vizinhança apresenta trincas de DWORDs: endereço inicial, endereço final exclusivo, RVA de unwind, compatíveis com estrutura RUNTIME_FUNCTION do Windows x64.

1051: cabeçalho PE, DataDirectory[3] / IMAGE_DIRECTORY_ENTRY_EXCEPTION: RVA **0x718602C**, tamanho **0x38E704**, offset dentro da .vdata **0x6A402C**.

1052: diretório contém **310.763 entradas de 12 bytes**. **310.763/310.763** com Begin<End e terceiro campo diferente de zero; **310.762/310.762** pares sucessivos ordenados e não sobrepostos.

Registro índice 28899: `il2cpp_init` Begin=0x344B60 End=0x344B88 UnwindRVA=0x5A710EC.

Registro índice 28900: `il2cpp_init_utf16` Begin=0x344B90 End=0x344C11 UnwindRVA=0x5D65A30.

**Conquista: Cartógrafo do Runtime — Épica.** Ligação estrutural validada entre exports IL2CPP e código reconstruído via diretório PE oficial, não inferida de assinatura isolada.

**Limites:** RUNTIME_FUNCTION indica intervalos e metadados de unwind, não os corpos das funções, execução real ou estado dos registradores. Objetivo 2 (compreensão completa da inicialização) **EM ANDAMENTO**. Não há CodeRegistration/MetadataRegistration validados nem servidor offline funcional.

PASSO 1053: mapear distribuição dos registros e comparar tabelas entre versões. Nunca versionar DLL, saída descomprimida ou arquivos proprietários.