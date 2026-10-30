# GrandCross Local: passos 1289 e 1290

**Passo 1289** — o usuario executou PowerShell somente-leitura no Windows. Resultados:

- `GameAssembly.dll`: 47294480 bytes, SHA-256 `01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624`, cabeçalho MZ, hash igual ao baseline.
- `global-metadata.dat`: 31876664 bytes, SHA-256 `eea7a31712bfca44caaa85cee3874ae9092a035556fcdef10f6c6a1fe156448b`, cabeçalho `AF 1B B1 FA 1D 00 00 00` (IL2CPP magic e versão 29), hash igual ao baseline.
- O script gerou um erro de conversão do literal hexadecimal para UInt32 **após** verificar o hash e ler o cabeçalho do metadata. A informação de integridade permanece válida.

**Passo 1290** — conferência documental da correspondência entre os dois hashes e os baselines registrados, com correção conceitual do erro de comparação do cabeçalho; não houve nova inspeção de memória.

**Limites** — o passo 1290 não identifica CodeRegistration, CodeGenModule, methodPointers, bytes RMI, login compatível ou servidor conectado. Os arquivos binários originais não são publicados.

O manifesto em `checkpoints/PASSO_1290.json` deve disparar a primeira validação do workflow. O relatório documental não é prova de que o workflow já rodou.
