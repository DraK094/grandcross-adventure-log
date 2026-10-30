# PASSO 959 — Recuperação integral da seção .vdata (29/10/2026)
**Último passo aprovado: 959. Próximo: 960, ainda não executado.**

## Evidência técnica
- DLL original analisada somente leitura: 47.199.760 bytes.
- .vdata: RVA 0x06A83000; tamanho virtual 14.131.200 bytes (~13,48 MiB).
- Descompressor implementado em Python puro encontrou seu marcador de término exatamente após gerar 14.131.200 bytes, sem usar tamanho como condição de parada.
- Bytes da fonte comprimida consumidos, a partir de .boot+0x22C: 8.059.398.
- SHA-256 dos primeiros 4 MiB preservado: b69ef8861b20e6cbc4111bc4137ac5b67b3c598054af76e53f737072280d67ac.
- **Novo SHA-256 integral:** 60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3.
- Contagens de operações de cópia: c5=480.987; 144=938.585; 18e/1a5=989.614.
- Tempo da execução final autônoma: 4,824181 segundos, resultado APROVADO.

## Limitações e retomada
- 100% significa cobertura dos bytes da seção virtual .vdata, **não** do projeto ou do backend.
- Comparação integral independente contra execução real do cliente não realizada; segundo estágio, CodeRegistration e servidor offline funcional não comprovados.
- O código em Python está em artefato separado da conversa; não versionar DLL, bytes reconstruídos ou assets proprietários.
- Passo 960: examinar estaticamente regiões anteriormente fora do prefixo de 4 MiB e destinos de JMP indireto, mantendo distinção entre análise e execução real.
- Backup anterior: docs/BACKUP_TECNICO_PASSO_957.md.