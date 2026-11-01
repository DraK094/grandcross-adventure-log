# GrandCross Local — Checkpoint 2432

Análise estática somente leitura da biblioteca ProudNetClientPlugin.dll. Foram cruzados 17 setters nativos de eventos (offsets +0x18..+0x98) com entradas na região de ponteiros .rdata 0x101E8..0x10290 e com instruções de trampolins.

**Resultado: 16 dos 17 offsets** de callback têm correspondência exata com saltos indiretos em trampolins, incluindo a rotina 0x12B0 que ajusta o argumento de 16 bits e salta via +0x90. O offset +0x68, associado ao setter Exception, ainda não foi comprovado; a rotina 0x1170 (referenciada na região) tem código complexo e requer análise própria. **Não assumir 17/17.**

As rotinas simples carregam contexto a partir do campo +0x10 e utilizam salto indireto por um dos offsets de callback. Isso estabelece uma correlação de layout e instruções de leitura, **não demonstra chamada efetiva pelo Grand Cross**. Não foram obtidos IDs RMI, protocolo, autenticação ou servidor local jogável.

SHA256 da DLL auditada: 91ef8ef7624491d1598f0f5ef31b83fa62a0e2a45a8324ebdb8b7edb43bd845c.
Evidências derivadas locais: gc_2425_2432_trampoline_map.py, GrandCross_2425_2432_trampoline_map.json, GrandCross_Local_CHECKPOINT_2432.md. Nenhum binário proprietário publicado. Próximo passo: investigar a semântica da rotina 0x1170.