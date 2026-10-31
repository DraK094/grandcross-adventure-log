# PASSO 2102 — Versão do ProudNet identificada

Log do usuário, leitura binária local:

- `ProudNetClient.dll` (2.396.160 bytes): string `@1.9.58993-master` no offset 0x00118AD7 e caminho `E:\engine\main_417\Release-1.9.58993-master\ProudNet\lib\x64\dll\Release\ProudNetClient.pdb` no offset 0x002017E0; outro caminho do código fonte no offset 0x001200A0.
- `ProudNetClientPlugin.dll` (146.432 bytes): caminho `E:\engine\main_417\Release-1.9.58993-master\ProudNet\srcNative\Bin\x64\ProudNetClientPlugin.pdb` no offset 0x0000FFF8.
- Os dois cabeçalhos PE apresentam timestamp 2025-08-28 UTC. Identificação forte do **build 1.9.58993-master**.
- Verificação pública: release oficial `ProudNetLibSetup-1.9.58993` datada 2025-08-29: https://github.com/Nettention/ProudNet/releases/tag/ProudNetLibSetup-1.9.58993 . Esta release descreve correção dos bindings C# PIDL para rmiID.

**Limites:** indicação forte de mesmo ramo/build; hashes e ABI da distribuição pública ainda não comparados; servidor e client ProudNet não demonstraram handshake. A release oficial ter o mesmo número não prova binários iguais. Próximo passo 2103 inventariar artefatos da release e requisitos/licenciamento, sem download automático.
