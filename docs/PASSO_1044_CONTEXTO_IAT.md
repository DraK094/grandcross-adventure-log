# PASSO 1044 — Contexto da referência literal à IAT

**Concluído como exame de bytes, não classificação semântica.** Último passo 1044; próximo 1045 não executado. Data 30/10/2026.

Na saída reconstruída da nova .vdata (SHA256 72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231), offset 0xF189 contém DWORD little-endian `60 02 AE 06` = RVA 0x06AE0260, o RVA da célula IAT de GetModuleHandleA na DLL atualizada. O byte anterior na janela é 0x00, e os quatro bytes seguintes são zeros.

**Alinhamento:** offset 0xF189 não é múltiplo de 4 ou 8, portanto não se deve classificar a sequência automaticamente como ponteiro QWORD convencional. A janela inclui bytes de possíveis instruções e dados intercalados; uma coincidência literal também é possível. Nenhuma leitura dinâmica ou referência de código a esse endereço foi demonstrada.

Janela de bytes confirmada em .vdata+0xF180: `42 68 68 00 E9 1D 1B 68 00 60 02 AE 06 00 00 00 00 0A 49 C7 C0 00 00 00 00 49 89 EA ...`.

A associação de valor RVA com IAT é objetiva; o significado funcional da ocorrência permanece hipótese. Objetivo 2 permanece EM ANDAMENTO. Não inferir inicialização IL2CPP nem contorno de restrições do processo.

Próximo passo 1045: verificar fronteiras de código e eventual referência estática ao offset por análise de fluxo; se não houver evidência suficiente, considerar a observação sem interpretação funcional.