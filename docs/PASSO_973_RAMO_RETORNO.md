# PASSO 973 — Salto de reconexão do ramo não tomado

**APROVADO estaticamente.** No caminho de não tomada do JE em RVA 0x6D81060: a leitura linear chega a RVA `0x6D81071`, que contém `E9 0B 00 00 00` = `JMP RVA 0x6D81081`. A partir de 0x6D81081, a desmontagem linear sem outras transferências chega ao controle RVA 0x6D81492, anteriormente identificado como `JE 0x6D815BE`. Esta constatação **não comprova execução dinâmica ou estados equivalentes**.

SHA256 da reconstrução integral 60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3. Sem binários proprietários no repositório.