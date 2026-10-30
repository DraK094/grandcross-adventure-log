# PASSO 1204 — Mapeamento de regiões do GameAssembly

Processo `7dsgc.exe`, PID 30012 (instantâneo desta execução). `GameAssembly.dll` base `0x7FFD00550000`, hash em disco conferido no passo 1202: `01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624`.

Consultas somente de metadados de memória via `VirtualQueryEx`, sem leitura de bytes:

- `.vdata` início `0x7FFD07032000`: State `0x1000` (MEM_COMMIT), Protect `0x40` (PAGE_EXECUTE_READWRITE), Type `0x1000000` (MEM_IMAGE), RegionSize 14131200.
- `.vdata` meio `0x7FFD076F0000`: `0x1000`, `0x40`, `0x1000000`, RegionSize 7061504 (a região retornada começa na posição consultada dentro do intervalo maior).
- `.boot` início `0x7FFD07DAC000`: `0x1000`, `0x20` (PAGE_EXECUTE_READ), `0x1000000`, RegionSize 8044544.
- `.boot` entrada `0x7FFD07DAC058`: `0x1000`, `0x20`, `0x1000000`, RegionSize 8044544.

Concluído: `.vdata` e `.boot` são regiões comprometidas com permissões executáveis no processo. **Não** estão confirmados conteúdos de código, `Il2CppCodeRegistration`, IDs RMI, RVAs de marshalers ou compatibilidade do emulador.

Próximo: passo 1205, comparar amostra mínima da região carregada com a seção reconstruída offline, somente se acesso somente leitura for permitido, sem alteração nem contorno de proteção.