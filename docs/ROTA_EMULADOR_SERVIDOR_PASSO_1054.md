# GRANDCROSS LOCAL — ROTA DO EMULADOR DE SERVIDOR

**Planejamento, NÃO implementação validada.** Último passo de análise comprovado: 1053. O PASSO 1054 é a próxima coleta de evidências, pendente da execução do usuário.

Objetivo: um emulador de servidor local, com cliente oficial de PC como consumidor, usando respostas/protocolo compatíveis em localhost. A recuperação de `.vdata` e a leitura dos metadados IL2CPP **não** estabelecem compatibilidade de rede.

Ordem técnica: (1) observar apenas metadados de conexões TCP associados a `7dsgc.exe`, sem contas/senhas; (2) identificar o transporte e a sequência de entrada e separar serviços auxiliares; (3) especificar mensagens e respostas de maneira fundamentada; (4) implementar backend local com testes próprios; (5) verificar se o cliente permite apontar para serviço local de forma autorizada; (6) validar estado e entrada na taverna. Não afirmar que a conexão local está estabelecida, nem que existe servidor jogável.

PASSO 1054 proposto: PowerShell `Get-Process -Name 7dsgc` e `Get-NetTCPConnection` filtrado por `OwningProcess`, retornando LocalAddress, LocalPort, RemoteAddress, RemotePort e State. Não inclui UDP nem todo tráfego de processos filhos; resultado ainda não coletado.

Nenhum binário do jogo, credencial, conteúdo de comunicação ou contorno de proteção publicado.