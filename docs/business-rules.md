---
title: Regras de Negócio
---

# Regras de Negócio

O projeto segue regras que garantem resultados consistentes e controle durante a extração de dados.

## Regras principais

- Antes de qualquer execução, o sistema verifica se o portal do TRF5 está disponível.
- O arquivo de saída `data/processos.jsonl` é limpo antes de iniciar uma nova busca.
- Busca por número de processo permite múltiplos números separados por vírgula.
- Busca por CNPJ usa paginação e só processa até `MAX_CNPJ_PAGES` páginas.
- Busca por nome de parte normaliza caracteres especiais antes de enviar a consulta.
- Cada processo é salvo apenas uma vez por execução, mesmo se for encontrado em diferentes buscas.
- Se uma requisição falhar, o sistema registra o problema e continua sem interromper todo o fluxo.
- Processos inexistentes ou em segredo de justiça são ignorados sem gerar erros.

## Validação e controle

- A disponibilidade do portal é verificada com `ProcessCrawler.is_available()` antes de limpar os dados.
- Duplicatas são controladas com o conjunto `processed_numbers` durante a execução.
- A persistência em JSON Lines garante registros independentes por linha.

## Limitações conhecidas

- A paginação por CNPJ está limitada por `MAX_CNPJ_PAGES` e pode não recuperar todos os processos.
- A extração de dados depende da estrutura atual do HTML do portal TRF5.
- Mudanças no layout do site ou nos nomes das classes/tags podem quebrar o parser.
