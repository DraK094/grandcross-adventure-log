# PASSO 1020 — Divergência de tamanho da DLL instalada

Resultado fornecido pelo usuário em 30/10/2026:
- Cópia de GameAssembly.dll usada nas análises 958–1019: **47.199.760 bytes**.
- Instalação atual em `E:\JOGOS\Netmarble Game\7dsgb\GameAssembly.dll`: **47.294.480 bytes**, modificado em **27/10/2026 01:35:53**.
- **Diferença exata: +94.720 bytes**, portanto os binários não são idênticos.
- O output do usuário não trouxe SHA-256 da instalação atual. Não atribuir hash nem assumir versão específica.
- RVAs e hashes da reconstrução de .vdata continuam válidos somente para a cópia anterior. Não inferir que a seção atual tenha os mesmos dados.
- **1020: divergência de tamanho verificada; equivalência de versão rejeitada.** Próximo teste: pedir SHA-256 explícito e cópia atual se o usuário puder enviar; refazer auditoria de PE e endereços antes de examinar o cliente atualizado.
- **Objetivo 2 — EM ANDAMENTO**, sem handoff real IL2CPP comprovado. Não publicar binários proprietários.