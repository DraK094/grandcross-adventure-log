# GrandCross Local — Checkpoint 1310
**Tipo de marco:** auditoria documental dos passos 1301 a 1309 e fechamento do passo 1310.
## Conclusões verificadas nas saídas fornecidas pelo usuário
1. A coleção referenciada pela API il2cpp_domain_get_assemblies possui 89 entradas naquela execução.
2. O primeiro elemento liga-se ao nome Assembly-CSharp.dll; o segundo, a Assembly-CSharp-firstpass.dll.
3. O segundo objeto tem endereço 0x0000026500251A48; referência principal 0x0000026500250088; o campo de retorno aponta de volta para o objeto.
4. O campo +0x18 aponta para texto "Assembly-CSharp-firstpass".
5. O campo +0x20 aponta quatro bytes antes do texto "Assembly-CSharp.dll"; o campo +0x28 aponta três bytes antes do texto "Assembly-CSharp-firstpass.dll".
6. O espaçamento observado entre objetos e referências não constitui prova de tamanho ou layout de Il2CppAssembly/Il2CppImage.
## Pendências
Não foi localizado CodeRegistration, CodeGenModule associado a Assembly-CSharp-firstpass.dll, tabela methodPointers validada, endereços dos quatro serializadores, mensagem RMI real nem conexão do cliente com o backend local.
## Próxima estratégia
A partir do passo 1311, evitar leitura redundante de textos e priorizar comparação com estruturas públicas IL2CPP ou artefatos de metadata verificados, distinguindo hipótese de implementação nativa de fato observado. Consultas read-only limitadas quando necessárias; não alterar cliente ou contornar restrições.
## Estado do progresso
Este marco avança a identificação de assemblies em memória; não mede progresso funcional do servidor. Preservar backups a cada 10 passos, sem anunciar êxito do Actions até execução verificada.
