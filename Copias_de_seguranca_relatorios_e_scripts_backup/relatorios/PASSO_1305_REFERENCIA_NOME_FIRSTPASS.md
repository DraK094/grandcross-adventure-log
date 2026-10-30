# GrandCross Local — PASSO 1305

O PowerShell leu a referência interna do elemento identificado como `Assembly-CSharp-firstpass.dll` (PID 30012). O objeto `0x0000026500251A48` apontava para estrutura `0x0000026500250088`; QWORD1 dessa estrutura era `0x000002650024C9C0`.

Os 32 bytes obtidos nesse destino começam com texto ASCII `Assembly-CSharp-firstpass` e byte nulo. Logo, quatro QWORDs derivados desses bytes representam caracteres, **não quatro ponteiros da estrutura**. O teste confirma uma segunda forma textual do nome, não CodeGenModule ou ponteiro nativo de método. Próximo passo: investigar os campos da estrutura após o bloco inicial já validado, sem presumir layout Il2CppImage.
