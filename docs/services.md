---
title: Services
---

# Services

O módulo `services/search.py` orquestra as buscas e a persistência dos dados extraídos.

## Fluxo geral

1. Recebe a estratégia de busca do usuário.
2. Executa a consulta por meio de `ProcessCrawler`.
3. Extrai os números de processo retornados.
4. Para cada processo, busca os detalhes, normaliza e salva em JSON Lines.

## Funções principais

### `process_and_save(crawler, process_number, processed_numbers, search_origin, search_term)`

Responsável por:

- buscar os detalhes de um processo específico
- extrair dados via `process_identification`
- verificar se o processo já foi processado
- adicionar metadados de origem da busca
- salvar o JSON no arquivo `data/processos.jsonl`

Se o processo não existir ou estiver em segredo de justiça, o fluxo é interrompido para esse item.

### `search_number(crawler, numbers, processed_numbers)`

Processa uma ou mais buscas por número de processo.

- `numbers`: lista de números de processo informados pelo usuário.
- `processed_numbers`: conjunto usado para evitar duplicação.

### `search_cnpj(crawler, cnpj, processed_numbers)`

Busca processos por CNPJ utilizando paginação.

- itera até `MAX_CNPJ_PAGES`
- usa `search_process_cnpj_page` para buscar cada página
- converte o HTML em lista de números com `process_list`
- salva cada processo encontrado

### `search_party_name(crawler, party_name, processed_numbers)`

Busca por nome da parte ou advogado.

- normaliza o termo com `normalize_party_name`
- executa a busca com `search_process_party_name`
- extrai os números de processo e processa cada um

## Controle de duplicidade

A variável `processed_numbers` garante que um mesmo processo não seja salvo duas vezes, mesmo se aparecer em buscas diferentes.

## Limites e comportamento

- A busca por CNPJ é limitada por `MAX_CNPJ_PAGES`.
- Se uma requisição falhar ou gerar HTML vazio, a função termina a busca nessa rota.
