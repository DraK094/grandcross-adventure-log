# PASSO 1040 — Base relocations TLS da DLL atual

**PASSO 1040 aprovado por parsing em Python.** Próximo 1041 ainda não executado; objetivo 2 continua EM ANDAMENTO.

- SHA256 DLL atual: `01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624`.
- Diretório .reloc RVA `0x8008000`, tamanho `0x10`, offset bruto `0x2D1A800`.
- Bloco `PageRVA=0x6AE1000`, `SizeOfBlock=16`.
- Entradas: `0xA018`, `0xA020`, `0xA028` são tipo 10 (`IMAGE_REL_BASED_DIR64`), RVAs `0x6AE1018`, `0x6AE1020`, `0x6AE1028`, campos `TLS.StartAddressOfRawData`, `TLS.EndAddressOfRawData`, `TLS.AddressOfIndex`.
- Entrada `0x0000` é tipo 0 (`ABSOLUTE`), padding.
- Não se observam outras correções no diretório PE convencional. **Não significa que o código não realize suas próprias correções** ou que o fluxo real tenha sido executado.
- Evidência somente estática, sem DLL modificada, sem servidor offline funcional demonstrado.

Próximo PASSO 1041: investigar estaticamente eventuais rotinas próprias de ajuste de endereços e relação com o runtime IL2CPP.