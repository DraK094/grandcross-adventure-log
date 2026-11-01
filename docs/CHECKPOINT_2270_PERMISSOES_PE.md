# Checkpoint 2270 — características das seções PE

Fonte: saída do PowerShell fornecida pelo usuário em 2026-10-31/2026-11-01, extraída do arquivo `GameAssembly.dll` associado ao processo `7dsgc`.

- `.vdata`: RVA `0x6AE2000`, `VirtualSize 0xD7A000`, `RawSize 0`, características `0xE0000060` (leitura, escrita e execução declaradas).
- `.boot`: RVA `0x785C000`, `VirtualSize 0x7ABA00`, `RawSize 0x7ABA00`, características `0x60000060` (leitura e execução declaradas, não escrita).
- Primeiras duas seções sem nome: características `0x60000020` (leitura/execução).
- `.idata`: características `0xC0000040` (leitura/escrita, sem execução declarada).

**Confirmação:** são características de seções inscritas no cabeçalho PE. Não representam necessariamente permissões efetivas em páginas da memória e não provam que `.vdata` foi preenchida com código, que exportações são executáveis, nem a associação em execução dos callbacks do jogo.

Próximo teste proposto: consultar *apenas metadados de proteção de páginas* de alguns endereços via API do Windows, sem ler conteúdo da memória ou alterar o processo, sujeito às restrições do ambiente do usuário. A compatibilidade de um servidor local jogável permanece não demonstrada.
