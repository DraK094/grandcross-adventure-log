# PASSOS 1187–1188 — Validação da seção nativa reconstruída

**1187:** Reconstrução da seção .vdata no GameAssembly atual foi reproduzida com 14.131.200 bytes, SHA256 `72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231`. Buscas ASCII de quatro nomes textuais deram zero resultados; isso não prova ausência de registro codegen. Primeira tentativa de decodificação foi corrigida para usar parâmetros da versão atual.

**1188:** Diretório de exceções PE em RVA `0x718602c`, 310.763 registros RUNTIME_FUNCTION validados, todos ordenados e sem sobreposição. Entradas explícitas para `il2cpp_init` RVA `0x344b60` e `il2cpp_init_utf16` RVA `0x344b90`.

**Limites:** Nenhum CodeRegistration, CodeGenModule ou endereço nativo dos quatro métodos Marshaler de login foi validado; não foram reconstruídos bytes reais de mensagens ou IDs RMI do jogo. Passo 1189 pendente.
