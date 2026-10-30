# GrandCross Local — PASSOS 1308–1309
## Evidência
Saída PowerShell do usuário no processo 7dsgc, PID 30012, GameAssembly base 0x7FFD00550000. O assembly foi novamente identificado como Assembly-CSharp-firstpass.dll antes das leituras.
- Offset +0x18 do objeto: endereço 0x0000026604129E71; começa com texto ASCII "Assembly-CSharp-firstpass" seguido de NUL.
- Offset +0x20: endereço 0x0000026603DAB274; quatro bytes NUL, depois "Assembly-CSharp.dll".
- Offset +0x28: endereço 0x0000026604129E8B; três bytes NUL, depois "Assembly-CSharp-firstpass.dll".
## Análise 1309
O campo +0x18 é uma referência textual exata. Os campos +0x20 e +0x28 também apontam para regiões com strings, mas seus endereços precedem em quatro e três bytes os textos encontrados. Assim, não podem ser classificados automaticamente como ponteiros para strings C iniciando no endereço apontado; podem referenciar subestruturas/valores com prefixos, e o layout permanece desconhecido. Não há evidência nova de CodeGenModule, CodeRegistration, methodPointers, ID RMI ou servidor conectado.
## Próximo passo
1310 deve consolidar resultados de 1301–1309 e disparar checkpoint decenal somente após a auditoria; evitar repetir leituras de strings sem hipótese estrutural discriminante. Não enviar binários ou metadata original.
