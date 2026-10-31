# Checkpoint 1870

Foi confirmada a chamada virtual RmiSend: objeto de contexto em [r15+8], vtable do objeto, slot +0x40. RTTI enumerou 93 vtables candidatas contendo codigo no slot +0x40, incluindo tres vtables diferentes de CNetClientImpl. Nao foi resolvido qual vtable o objeto live usa. Dados offline reproduziveis em gc_proud_vtable_slot40_1861.py e grandcross_slot40_1861.json. Nao ha framing ou login funcional.
