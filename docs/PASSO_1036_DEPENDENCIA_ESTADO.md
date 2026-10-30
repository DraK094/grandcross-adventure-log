# PASSO 1036 — Limite de evidência para o salto indireto

Análise de 30/10/2026 sobre GameAssembly atual SHA256 01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624; saída vdata SHA256 72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231.

Em RVA 0x6DF45A0 a instrução FF 20 é JMP QWORD PTR [RAX]. Preparação anterior carrega índice RBX da pilha, desloca RBX em 3 bits e usa ADD/SUB de constantes que se cancelam sobre RAX. O endereço de leitura final depende da base RAX derivada da pilha e do índice, e o destino depende do valor do QWORD nessa posição.

Simulação algébrica com três estados ARTIFICIAIS: base 0x186AE2000, index 0 => 0x186AE2000; base 0x186AE2000, index 3 => 0x186AE2018; base 0x186AE3000, index 3 => 0x186AE3018. Isso demonstra indeterminação, não destino do cliente.

PASSO 1036 aprovado só como auditoria de limitação, não resolução dinâmica. Objetivo 2 (compreender inicialização completa IL2CPP): EM ANDAMENTO. Sem execução real da cadeia, CodeRegistration, MetadataRegistration ou servidor offline funcional confirmados.

PRÓXIMO PASSO 1037 não executado. Para superar a barreira: evidência de módulo/estado de execução via métodos de diagnóstico respeitando a proteção do jogo, ou investigação estática alternativa, sem contorno de proteções. Nenhum binário proprietário publicado.