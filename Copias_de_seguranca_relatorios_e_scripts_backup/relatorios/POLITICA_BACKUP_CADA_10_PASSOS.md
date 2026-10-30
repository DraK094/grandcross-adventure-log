# GrandCross Local — política de backup por marco de 10 passos

**Vigência: 2026-10-30.** Regra de continuidade obrigatória durante o trabalho assistido.

## Gatilho
Quando um passo efetivamente **concluído e documentado** atingir múltiplo de dez (1290, 1300, 1310 etc.), preparar e publicar um checkpoint no repositório, antes de iniciar a próxima dezena. O marco 1300 também terá relatório de progresso de 100 passos.

## Procedimento automático durante sessões ativas
1. Atualizar resultados e distinguir **executado, preparado, não verificado, bloqueado e hipótese**.
2. Preparar relatório Markdown, JSON de evidências sanitizadas e scripts próprios reproduzíveis; incluir hashes, resultados negativos e próximos experimentos.
3. Conferir duplicação e arquivos existentes no GitHub; preservar histórico sem sobrescrever evidências anteriores.
4. Fazer commits via conexão GitHub disponível; conferir SHA do commit e, quando possível, reler arquivo gravado.
5. Informar ao usuário link, SHA e qualquer falha. Não anunciar backup confirmado após gravação bloqueada.
6. Se não houver conexão ou permissão de escrita, gerar pacote local e registrar o checkpoint como **pendente**; tentar publicar quando a conexão voltar.

## Limitação operacional
Este gatilho é **orientado a evento nos passos conduzidos com o assistente**, não é um agendamento permanente nem um processo que roda com o chat fechado. Para execução completamente independente, será necessário instalar um workflow no GitHub Actions ou outro serviço e definir qual evento/arquivo marca um passo como concluído. Nunca prometer commits futuros sem um processo realmente implantado.

## Segurança, escopo e auditoria
Não enviar binários do jogo, metadata original, informações de contas, credenciais, tokens, dumps sensíveis ou material de terceiros. Apenas análises e códigos próprios. Checkpoints de pesquisa não significam interoperabilidade com o cliente. Priorizar diretório Copias_de_seguranca_relatorios_e_scripts_backup/{relatorios,evidencias,scripts,logs}. A cada fechamento, atualizar manual LEIA_PRIMEIRO_PROXIMO_CHAT.md. Um backup falho não altera o último passo comprovado.

## Estado inaugural
O checkpoint recuperado até 1288 foi publicado no commit a6b9e28447e37f65d7d143d2812a58b37d447443. PASSO 1289 preparado, não executado. Próximo gatilho automático em sessão ativa: **1290 concluído**.
