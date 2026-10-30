# PASSO 1026 — Trampolins após cálculo do ImageBase, versão atual

**PASSO 1026 aprovado estaticamente; PASSO 1027 ainda não executado.** DLL atualizada hash SHA256 `01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624`; saída .vdata hash `72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231`.

- `.vdata+0xCF0AB` → `JMP .vdata+0x1BD44`.
- `.vdata+0x1BD44` → `JMP .vdata+0x1B2F10`.
- `.vdata+0x1B2F10`: `MOV RAX,RAX`; `.vdata+0x1B2F13`: `JMP .vdata+0xF4FAC` (VA `0x186BD6FAC`).
- Destinos calculados a partir dos bytes `E9 rel32` decodificados. São **vínculos estáticos**; não se conhece pilha nem estado real, ou handoff a IL2CPP.
- Próximo PASSO 1027: examinar a região `.vdata+0xF4FAC` com controle de saltos e ciclos.

**Objetivo 2: EM ANDAMENTO**; não publicar código proprietário nem afirmar execução real. [Passos 1023–1025](PASSOS_1023_1025_BOOT_VDATA_ATUAL.md).