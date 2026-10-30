# PASSOS 1221–1223 — Registro IL2CPP e relocações

Análise reproduzível do `GameAssembly(2).dll` versão atual (SHA256 `01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624`).

1221: auditoria do diretório PE de relocação: RVA `0x8008000`, tamanho **16 bytes**, offset bruto 47294464.
1222: único bloco `IMAGE_BASE_RELOCATION` com página RVA `0x6ae1000`; três entradas DIR64 (tipo 10) nos offsets `0x18`, `0x20`, `0x28`, além de um preenchimento de tipo zero. As entradas correspondem à região TLS, não a `CodeRegistration`.
1223: metadata declara 89 imagens, com `Assembly-CSharp-firstpass.dll` no índice 1; texto ASCII com este nome não apareceu na DLL bruta. **O nome e os RID dos métodos não demonstram localização do CodeGenModule ou da tabela methodPointers.**

Resultados: CodeGenModule **não localizado**; quatro RVAs nativos de login **não localizados**; nenhuma mensagem RMI reconstruída. A pequena tabela de relocações reforça a necessidade de analisar fixups/preparação em execução, mas não prova mecanismo concreto. Próximo passo 1224 pendente.