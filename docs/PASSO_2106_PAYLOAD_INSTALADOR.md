# PASSO 2106 — Região anexada ao instalador ProudNet

Inventário `7z l -slt` do instalador `ProudNetLibSetup-1.9.58993-master.exe`: contêiner PE, `Physical Size=436866848`, headers de 1024 bytes. Entrada `[0]` inicia no offset **140800** (`0x22600`) e mede **436715368** bytes. O arquivo também possui `CERTIFICATE` de 10680 bytes no offset 436856168, e seções convencionais de PE e recursos.

A região `[0]` representa aproximadamente **99,965%** do tamanho do arquivo. É plausível ser o payload anexo do instalador, mas **ainda não se conhece formato, compressão, estrutura ou conteúdo interno**. A presença de um overlay não prova a existência de exemplos de servidor. 7-Zip listou o contêiner externo, não os arquivos do SDK.

Análise de leitura apenas; arquivos extraídos 0; instalador não executado; arquivos do jogo inalterados. Próximo PASSO 2107: ler pequenas amostras nos limites do overlay e buscar assinaturas de formatos comuns, sem extração nem execução; observar que varreduras de assinaturas não validam o formato por si só.
