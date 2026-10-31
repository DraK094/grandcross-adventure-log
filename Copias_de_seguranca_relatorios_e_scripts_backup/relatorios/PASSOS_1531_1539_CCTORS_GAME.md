# GrandCross Local — passos 1531–1539

Leitura do usuario no GameAssembly carregado, PID 30012, base 0x7FFD00550000. Os construtores Common/GameC2S e Common/GameS2C foram mapeados pela methodPointers Firstpass.

GameC2S.Common .cctor token 0x0600494A: RVA 0x7E2830, argumento 0x498=1176 em chamada de alocação de array; a classe declara 1177 campos. GameS2C.Common .cctor token 0x060049B4: RVA 0x7E27A0, argumento 0x274=628; a classe declara 629 campos. Em ambos há criação de objeto, chamada subsequente que recebe objeto e referência a dados/FieldInfo e armazenamento do ponteiro em static_fields. Isso é compatível com uma inicialização de array a partir de valores compilados, mas ainda NÃO identifica conteúdo, tipo exato nem ID numérico da mensagem. Para S2C, os operandos RIP-relativos confirmam global de classe RVA 0x5FB6B08, referência de tipo usada para criar o array 0x60682D0 e referência de dados/FieldInfo RVA 0x6038130.

Não deduzir `ID == índice` a partir da ordem dos campos, nem confundir comprimentos 1176/628 com IDs de protocolo. Próxima observação mais útil: checar se a global 0x5FB6B08 já foi resolvida e se o primeiro campo estático aponta para array gerenciado; se não, parar e avaliar extração estática, sem execução de código do jogo. Sem servidor local funcional verificado.
