# PASSO 969 — Convergência linear após TEST EDX,EDX

**Aprovado — análise estática.** Do desvio em RVA 0x6D80E42, tanto a continuação linear a partir de 0x6D80E48 quanto a entrada 0x6D80FA0 alcançam a instrução comum em RVA 0x6D80FF6.

RVA 0x6D80FF4: `TEST EBX,EBX`; RVA 0x6D80FF6: `JE 0x6D811E7`; fallthrough RVA `0x6D80FFC`. Os bytes do JE foram validados em Python no .vdata reconstruído. Convergência **de endereços na desmontagem linear**, não equivalência de estados dinâmicos ou execução real.