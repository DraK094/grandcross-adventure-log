# PASSO 1058 — Bibliotecas carregadas no cliente oficial

**APROVADO — listagem de módulos carregados, não validação de protocolo.**

O usuário executou PowerShell `Get-Process -Name 7dsgc` com PID 30012, consultou `Modules` e obteve `ProudNetClientPlugin.dll` e `ProudNetClient.dll` ambos em `E:\JOGOS\Netmarble Game\7dsgb\7dsgc_Data\Plugins\x86_64\`; também `UnityPlayer.dll`, `GameAssembly.dll`, `WININET.dll` e bibliotecas Windows de rede. Isto **confirma carregamento das DLLs**, não uso específico do protocolo ProudNet na conexão TCP remota `43.174.218.165:23071`.

Próximo passo 1059 sugerido: inspecionar apenas metadados PE, versão, assinatura e exports das DLLs oficiais em disco, sem editar ou injetar no cliente. Guardar hashes SHA-256 e preservar binários privados fora do repositório público.

**Servidor local compatível: não demonstrado.**