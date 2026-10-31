# GrandCross Local — PASSOS 1506–1509

Fonte: 128 bytes de cada rotina, coletados somente para leitura no GameAssembly carregado, PID 30012, base 0x7FFD00550000.

- Em RVA 0x367780, `E9 3B 21 09 00` faz `jmp 0x3F98C0` (salto relativo assinado calculado).
- RVA 0x36E690 tem prólogo e usa o argumento RDX, verifica limite 0x7FFFFFFF, multiplica quantidade por tamanho de elemento da classe (`[rax+0x104]`), soma 0x20 para cabeçalho e segue por vias de alocação; comportamento compatível com alocação de array gerenciado, mas assinatura sem símbolos ainda não confirmada.
- RVA 0x3C13E0 contém verificações de tipo/estado e várias chamadas auxiliares; nenhuma operação RMI específica demonstrada.
- O destino 0x3F98C0 ainda não foi dissecado; não prolongar recursão em wrappers genéricos sem conexão com ID RMI.

Avaliação: valores 6 e 14 nos construtores Common são compatíveis com comprimentos de arrays, ainda não IDs nem valores de elementos. Para chegar ao objetivo, investigar a representação de dados dos arrays `Common` e o método de associação ID-nome; evitar interpretar metadata token como RMI. Nenhum ID numérico de login demonstrado, nenhuma autenticação local.
