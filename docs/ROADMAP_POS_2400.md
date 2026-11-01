# Roteiro técnico — após o marco 2400

**Próximo passo 2401: pendente.** A lista abaixo descreve prioridades, **não resultados já executados**.

## Prioridade 1 — Resolver o papel do grupo A
- Verificar referências à tabela em RVA 0x10248 por padrões adicionais (ponteiros indiretos, referências não-RIP relativas, inicializadores), sem concluir ausência por falta de um padrão.
- Comparar com o construtor do grupo B em RVA 0x9AA0, seus três ponteiros de trampolins e offsets 0x28/0x30/0x38.
- Separar correspondência de layout de prova de identidade de objeto e prova de invocação.

## Prioridade 2 — Estabelecer evidência de chamadas
- Determinar que trechos da implementação nativa realmente registram/consomem callbacks no SDK; quando autorizado, considerar exemplo sintético independente sem usar credenciais ou tráfego de produção.
- Não inferir que o cliente Grand Cross usa uma função só porque a biblioteca a expõe.

## Prioridade 3 — Protocolo e servidor funcional
- Obter origem verificável para IDs RMI e formatos de mensagens, respeitando licenças e controles de acesso.
- Definir testes de integração com critérios de aprovação explícitos: conexão, handshake, autenticação em ambiente legitimamente controlado, estado de jogo persistente.
- **Estado atual: nenhum desses critérios foi comprovado para o Grand Cross.** Não declarar porcentagem do servidor.

## Procedimentos
- Ao iniciar novo chat: ler README e STATUS_ATUAL_2400 antes de notas antigas; conferir cópias e hashes.
- Documentar provas com SHA256, offsets, comandos executados, resultados observados e limites. Diferenciar análise estática, teste sintético e teste de interoperabilidade real.
- Checkpoint formal a cada 100 passos; conquistas apenas para novos marcos comprovados.
- Atualizar README, manual de retomada, status e índice ao alcançar novo marco.
- Não subir DLLs, metadata integral, tokens, contas, segredos, dumps de memória ou assets protegidos.
