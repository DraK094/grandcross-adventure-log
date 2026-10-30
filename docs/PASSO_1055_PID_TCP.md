# PASSO 1055 — Atribuição dos sockets TCP

Evidência PowerShell do usuário: PID 30012, processo `7dsgc`. Entradas: `0.0.0.0:50790` Bound; `192.168.1.106:59142 -> 43.174.218.165:23071` Established; duas pontas da mesma conexão localhost `127.0.0.1:50790 <-> 127.0.0.1:50789` ambas Established, OwningProcess 30012. Resultado: **APROVADO somente para atribuição PID/sockets**. Não identifica protocolo de aplicação, função do host remoto, nem demonstra servidor local compatível.

Próximo PASSO 1056: observação em intervalos curtos de conexões e contadores de bytes por processo, caso disponíveis, sem capturar conteúdo nem perturbar tráfego. Não publicar dados privados ou credenciais.