# PASSOS 1007–1009 — Auditoria da cópia de metadados

Passos 1007 a 1009: testes locais aprovados. Próximo 1010 não iniciado. Objetivo 2 continua EM ANDAMENTO.

- Arquivo recebido: 31.786.920 bytes; SHA-256 `1fa69d945210e27b2ca6195ef975da386fe11de044e764069986717ac3d577c9`.
- Assinatura `0xFAB11BAF`, versão IL2CPP 29.
- Cabeçalho: 31 pares offset/tamanho dentro dos limites físicos.
- Pool de nomes: offset 1.547.424, tamanho 5.679.156 bytes.
- Definições de tipos: 34.451 (registros de 88 bytes).
- Imagens: 89 (registros de 40 bytes).
- Assemblies: 89 (registros de 64 bytes).
- Primeira imagem `Assembly-CSharp.dll`: 20.065 tipos.
- Segunda `Assembly-CSharp-firstpass.dll`: 3.397 tipos.
- Soma dos 89 campos typeCount: 34.451, igual à quantidade de definições.

Conclusão: metadados estruturalmente coerentes e parcialmente interpretados. Não confirma CodeRegistration, MetadataRegistration, execução da inicialização IL2CPP ou servidor funcional. DLL original e cópia dos metadados não foram modificados. Próximo passo 1010: correlacionar definições e rastreamento do runtime.
