# GrandCross Local — PASSO 1205: amostra .vdata coincidente

A amostra de 16 bytes lida no processo `7dsgc.exe` em `0x7FFD07032000` foi `DC-75-7A-EB-9E-60-AC-D5-E2-4A-82-C1-10-37-77-AC`. Reexecutado o descompactador independente no `GameAssembly(2).dll` atual (tamanho 47294480), produzindo 14131200 bytes da `.vdata` e SHA256 `72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231`. Os primeiros 16 bytes foram exatamente `DC-75-7A-EB-9E-60-AC-D5-E2-4A-82-C1-10-37-77-AC`.

**Conclusão validada**: correspondência exata 16/16 entre amostra de memória e início da `.vdata` reconstruída offline. **Limites:** a comparação inicial NÃO comprova identidade de toda a seção, `CodeRegistration`, implementação de serializadores, IDs RMI ou handshake.

Próximo passo 1206: avaliar evidências estáticas de código e possíveis referências sem presumir apontadores nativos. Nenhum binário do jogo publicado.