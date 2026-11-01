# Scripts e reprodutibilidade — situação em 01/11/2026

O validador versionado aqui, [validate_checkpoint.py](validate_checkpoint.py), verifica manifestos `checkpoints/PASSO_NNNN.json` e os arquivos derivados referenciados. O manifesto do [passo 2400](../checkpoints/PASSO_2400.json) foi publicado, mas **uma execução aprovada do GitHub Actions precisa ser conferida separadamente**; publicar o manifesto não constitui prova de sucesso do workflow.

Relatórios e scripts de análise executados em conversas anteriores podem existir como anexos locais, mas **não são automaticamente enviados** ao repositório. Não alegar reprodução completa a partir daqui sem conferir cada script e suas dependências. Arquivos comerciais (GameAssembly, global-metadata, ProudNet DLLs) não devem ser publicados.

Para saber o estado real do projeto e os próximos testes, consultar [STATUS ATUAL 2400](../docs/STATUS_ATUAL_2400.md), [ROADMAP PÓS-2400](../docs/ROADMAP_POS_2400.md) e [POLÍTICA DE EVIDÊNCIA](../docs/POLITICA_DADOS_E_EVIDENCIAS_2400.md).
