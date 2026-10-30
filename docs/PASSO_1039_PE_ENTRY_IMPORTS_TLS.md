# PASSO 1039 — Auditoria PE: ponto de entrada, imports e TLS

**Aprovado por parsing direto em Python da DLL atualizada.** Próximo 1040 ainda não executado. Objetivo 2 — inicialização completa IL2CPP: EM ANDAMENTO.

- SHA256 da DLL: `01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624`.
- ImageBase PE: `0x180000000`; AddressOfEntryPoint RVA `0x785C058`.
- Seção `.boot` começa em RVA `0x785C000`; logo o PE declara como entrada `.boot+0x58`, exatamente a entrada estudada na cadeia de reconstrução.
- Seção `.vdata` RVA `0x6AE2000`, tamanho virtual 14.131.200 bytes, RawSize zero.
- Import directory RVA `0x6AE0182`, tamanho `0x184`; dez bibliotecas nos descritores: kernel32.dll, USER32.dll, ADVAPI32.dll, ole32.dll, OLEAUT32.dll, SHELL32.dll, WS2_32.dll, IPHLPAPI.DLL, dbghelp.dll, baselib.dll. Um thunk de importação em disco por descritor, sem afirmar ausência de resolução dinâmica adicional.
- TLS directory RVA `0x6AE1018`, tamanho `0x28`; `AddressOfCallBacks = 0` no arquivo; TLS raw data `0x186AE1000..0x186AE1008`, AddressOfIndex `0x186AE1008`. Não há lista de callbacks indicada por esse campo.
- Diretório de reloc RVA `0x8008000`, tamanho `0x10`.

**Interpretação:** confirma vínculo estrutural da entrada PE com `.boot`, mas não prova execução dinâmica de toda a cadeia nem inicialização IL2CPP. Não identifica CodeRegistration/MetadataRegistration; sem servidor local funcional. Nenhum binário proprietário versionado.

**Próximo PASSO 1040:** auditar diretório de relocations e demais elementos pertinentes da inicialização PE, sem acesso à memória protegida.
