# Política de evidência, dados e publicação — marco 2400

## Níveis de certeza
1. **Observado e reproduzido:** bytes/instruções, assinaturas ou respostas do sistema verificadas com origem e método.
2. **Corroboração documental:** APIs descritas pelo fornecedor; não significa uso pelo jogo.
3. **Hipótese:** fluxo inferido entre componentes que ainda não foi observado.

Não misturar evidência de um SDK genérico com evidência específica do Grand Cross. Não converter "método existe" em "método executado". Manter trilhas separadas: análise do cliente versus servidor local funcional.

## Proibições de publicação
Nunca publicar binários comerciais, metadata integral proprietário, ativos do jogo, chaves/tokens/credenciais, identificadores de contas, endereços privados, capturas de tráfego sensível ou dumps de memória. Publicar somente relatórios derivados e ferramentas próprias devidamente revisadas. Conferir licenças ProudNet e software do jogo antes de redistribuir qualquer elemento.

## Reprodutibilidade e backup
Toda descoberta relevante deve indicar checkpoint, arquivo analisado e SHA256, método, resultado, limites e próximo passo. Guardar scripts próprios sanitizados e evidências resumidas quando permitido. Verificar existência do arquivo no GitHub e SHA do commit; operação bloqueada ou falha **não conta** como publicação. Não inventar números de passos nem revisões não executadas.

## Erratas
A [ERRATA 2272](CHECKPOINT_2272_ERRATA_EXPORTS.md) prevalece sobre afirmações incompatíveis de checkpoints anteriores sobre a localização dos exports do GameAssembly. Se houver divergência futura, registrar correção explícita e preservar o histórico.
