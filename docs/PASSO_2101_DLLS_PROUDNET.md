# PASSO 2101 — Identificação PE das DLLs ProudNet

Analisadas DLLs carregadas pelo cliente 7dsgc, somente leitura:
- ProudNetClient.dll: PE x64 machine 0x8664; 6 seções; timestamp 0x68AFD3B0 (2025-08-28 03:57:36 UTC); tamanho 2.396.160 bytes; SHA256 E5B197F6F8485BE65C3156D7899A46F8CA08CA62943C4B554BFFE595CED769C9; sem FileVersion, ProductVersion, ProductName, Company.
- ProudNetClientPlugin.dll: PE x64 machine 0x8664; 6 seções; timestamp 0x68AFC66C (2025-08-28 03:01:00 UTC); tamanho 146.432 bytes; SHA256 91EF8EF7624491D1598F0F5EF31B83FA62A0E2A45A8324EBDB8B7EDB43BD845C; sem os campos de versão.

Conclusão: arquitetura confirmada e hashes consistentes com passos anteriores; **versão do SDK desconhecida**. Timestamps são indicativos, não prova de versão ou data efetiva de compilação. Referências externas: https://github.com/Nettention/ProudNet/releases e https://docs.proudnet.com/proudnet.eng/proudnet/2.setting/c. Próximo PASSO 2102: inspeção offline de marcadores de versão, sem executar DLLs nem baixar pacotes.
