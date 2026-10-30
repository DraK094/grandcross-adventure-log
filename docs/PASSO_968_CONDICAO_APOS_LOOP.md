# PASSO 968 — Primeiro controle após a saída do laço

**Aprovado estaticamente em 29/10/2026.** A partir do alvo de sucesso do ciclo anterior RVA 0x6D80D8E, a leitura linear localizou:

```asm
0x6D80E40: TEST EDX,EDX
0x6D80E42: JE 0x6D80FA0
0x6D80E48: PUSH 0x70BF1BA9   ; primeira instrução no caminho não tomado
```
A instrução JE foi validada por bytes `0F 84 58 01 00 00`. O destino tomado é RVA `0x6D80FA0`; o fallthrough é RVA `0x6D80E48`. Sem conhecer o valor de EDX, **nenhum desses caminhos pode ser afirmado como execução real**. Próxima análise sugerida: mapear ambos os ramos em modo estático com limites explícitos, procurando convergência.

Versão validada: SHA256 integral 60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3. Nenhum servidor offline funcional.
