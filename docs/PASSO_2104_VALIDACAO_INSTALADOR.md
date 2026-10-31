# PASSO 2104 — Verificação do instalador oficial ProudNet

Arquivo local `ProudNetLibSetup-1.9.58993-master.exe`, tamanho 416,63 MiB, assinatura MZ válida. SHA-256 `8FA26CA99696CFE90D01142217D4D2B80F693A6F5B3DA0895204A29B2CB44215`. `Get-AuthenticodeSignature`: **Valid**. Signer subject `CN=Nettention Inc, O=Nettention Inc, L=Gangnam-gu, S=Seoul, C=KR, ...`; emissor `DigiCert Trusted G4 Code Signing RSA4096 SHA384 2021 CA1`; certificado NotAfter 2026-01-13 20:59:59 (data informada por Windows, não confundir com validação do timestamp de assinatura). Recursos FileVersion e ProductName vazios. Hash oficial independente ainda não comparado. Instalador **não executado**; sem arquivos do jogo modificados.

Próxima etapa 2105: verificar dados de assinatura incluindo timestamps e obter manifesto externo/opções de inspeção sem executar instalador. Não concluir segurança total a partir de Authenticode isoladamente. Antes de instalar, examinar licença, destino e requisitos do SDK.
