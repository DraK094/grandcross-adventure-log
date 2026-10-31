# PASSO 2105 — Inspeção pré-instalação ProudNet

Relatório do usuário: Authenticode `Valid`, `SignatureType=Authenticode`, assinatura por `Nettention Inc`, emissor da assinatura visto no passo anterior. Certificado de assinatura válido entre 2024-12-15 e 2026-01-13; certificado de timestamp presente, `DigiCert SHA256 RSA4096 Timestamp Responder 2025 1`, com janela 2025-06-03 a 2036-09-03. Presença de certificado de timestamp não informa, isoladamente, o instante de assinatura.

7-Zip encontrado, `7z l -slt` retornou exit code 0 e 22 caminhos, incluindo seções PE `.text`, `.itext`, `.data`, `.rdata`, recursos `.rsrc`, `CERTIFICATE` e `[0]`. A listagem não demonstrou nenhuma pasta `Server`, `Sample` ou arquivo `.lib`/`.dll` interno. O caminho `[0]` pode representar um fluxo anexado, mas **sem prova de seu formato ou conteúdo**. O sucesso do 7-Zip apenas mostra que reconheceu o contêiner PE; não que o instalador seja um arquivo descompactável com toda a árvore do SDK.

Nenhum arquivo extraído, instalador não executado, cliente Grand Cross não alterado. Próximo PASSO 2106: examinar metadados do contêiner e natureza do fluxo anexado de modo não executável, ou proceder com instalação oficial somente após licença e destino serem avaliados.
