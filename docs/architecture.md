---
title: Arquitetura
---

# Arquitetura

O sistema foi dividido em camadas para separar responsabilidades e facilitar manutenção.

## Visão geral

- `src/main.py`: interface interativa no terminal e orquestração do processo.
- `src/crawler.py`: comunicação HTTP com o portal do TRF5.
- `src/parser.py`: extração e normalização de dados HTML.
- `src/storage.py`: persistência dos resultados em JSON Lines.
- `src/services/search.py`: lógica de busca, controle de duplicidade e gravação dos dados.

## Fluxo de execução

1. `main.py` instancia `ProcessCrawler` e verifica disponibilidade do portal.
2. Se disponível, limpa o arquivo de saída com `clear_jsonl`.
3. A partir da escolha do usuário, chama `search_number`, `search_cnpj` ou `search_party_name`.
4. Cada busca obtém HTML via `ProcessCrawler`.
5. `parser.py` processa o HTML e gera estrutura de dados normalizada.
6. `storage.py` salva cada processo em `data/processos.jsonl`.

## Separação de responsabilidades

- O `crawler` concentra as requisições e isolam o restante da aplicação de mudanças no portal.
- O `parser` transforma HTML em dados estruturados.
- O `services` orquestra buscas e evita duplicação de resultados.
- O `storage` garante persistência simples e reutilizável.

## Componentes principais

### `ProcessCrawler`

- Mantém sessão HTTP com cabeçalhos padrão.
- Fornece métodos específicos para número de processo, CNPJ e nome de parte.
- Suporta paginação de resultados de CNPJ.

### `parser.py`

- Normaliza texto e extrai campos a partir de padrões do HTML.
- Identifica os envolvidos e as movimentações do processo.

### `services/search.py`

- Processa cada processo encontrado.
- Filtra processos já processados com `processed_numbers`.
- Salva metadados de origem da busca.

## Observações de design

- A escolha pelo formato JSON Lines facilita anexar resultados de execuções posteriores.
- A validação do portal no início evita sobrescrever dados quando o serviço está indisponível.
- O design modular permite melhorar a captura de dados ou a persistência sem alterar a UI do terminal.
