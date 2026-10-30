# GrandCross Local — PASSOS 1302–1303

Teste somente leitura informado pelo usuário, PID 30012. Duas referências QWORD0 conduzem a estruturas que apontam de volta ao objeto original em seu terceiro campo de 64 bits.

Objeto 0 em `0x00000265002519F0` → referência `0x0000026500250040` → QWORD2 `0x00000265002519F0`. Objeto 1 em `0x0000026500251A48` → referência `0x0000026500250088` → QWORD2 `0x0000026500251A48`.

QWORD1 das estruturas associadas são `0x000002650024C9A0` e `0x000002650024C9C0` (distância 32 bytes). QWORD3 são 0x4E6E e 0x0D5E. O padrão é estruturalmente consistente, mas não prova que sejam objetos Il2CppAssembly nem que os outros endereços contenham nomes. Próxima verificação: leitura pequena e limitada dos candidatos a texto para identificar seu tipo. Não foram encontrados CodeGenModule, ponteiros dos serializadores ou protocolo RMI.
