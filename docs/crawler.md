---
title: Crawler
---

# Crawler

O módulo `crawler.py` é responsável por fazer as requisições HTTP ao portal do TRF5 e recuperar o HTML necessário para a extração dos dados.

## `ProcessCrawler`

A classe `ProcessCrawler` encapsula a comunicação com o portal e mantém uma sessão HTTP persistente.

### Atributos principais

- `self.delay`: intervalo em segundos entre requisições para evitar sobrecarga.
- `self.session`: instância de `requests.Session` com cabeçalhos padrão.

### URLs utilizadas

- `BASE_URL`: página inicial do portal TRF5.
- `CP_BASE_URL`: base para consultas adicionais de resultados de CNPJ.
- `SEARCH_URL`: endpoint usado para buscar processos por número, CNPJ ou nome da parte.

## Métodos

### `is_available()`

Verifica se o portal está disponível, fazendo uma requisição GET para `BASE_URL`.

Retorna `True` se o portal responder com sucesso; caso contrário, registra warning e retorna `False`.

### `search_process(search_type, value)`

Faz uma requisição POST para `SEARCH_URL` com os dados necessários para cada tipo de busca.

Parâmetros:

- `search_type`: tipo de busca (`xmlproc`, `xmlcpf`, `xmlnomparte`).
- `value`: termo de busca (número do processo, CNPJ ou nome da parte).

### `search_process_number(process_number)`

Busca o HTML de um processo por número.

### `search_process_cnpj(cnpj)`

Busca o HTML de um processo por CNPJ.

### `search_process_party_name(party_name)`

Busca o HTML de um processo por nome da parte.

### `search_process_cnpj_page(cnpj, page)`

Busca a página de resultados paginados para um CNPJ específico.

O CNPJ é normalizado para apenas dígitos antes de construir a URL.

## Observações

- O módulo centraliza a lógica de interação com o portal, isolando os detalhes de requests do restante do sistema.
- Em caso de falha de conexão, o método retorna string vazia para indicar erro na busca.
