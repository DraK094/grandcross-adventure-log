# GrandCross Local — PASSO 1242

Amostra fornecida do processo: RVA 0x5A710EC; bytes iniciais `01 06 02 00 06 32 02 30`.

Decodificacao Windows x64 UNWIND_INFO: versao 1, flags 0, prolog size 6, 2 unwind slots, frame register 0. Slot `06 32`: CodeOffset 6, UWOP_ALLOC_SMALL=2, OpInfo=3, tamanho `(3*8)+8=32` bytes. Slot `02 30`: CodeOffset 2, UWOP_PUSH_NONVOL=0, OpInfo=3 (RBX). Isso corresponde ao prologo `40 53` (push rbx) e `48 83 EC 20` (sub rsp,0x20) encontrado na amostra de codigo do PASSO 1240. A funcao RUNTIME_FUNCTION associada e RVA 0x20B2740–0x20B27C7.

Conclusao validada: consistencia entre bytes de codigo em memoria e registro de unwind do mesmo RVA. NAO identifica o nome do metodo, CodeRegistration, serializer de login ou IDs RMI. Passo seguinte 1243 pendente. Outros bytes apos 8 iniciais pertencem a dados seguintes e nao foram interpretados como parte deste primeiro registro.